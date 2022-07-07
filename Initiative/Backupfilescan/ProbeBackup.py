import requests
#from conf import config
import queue
import threading
from urllib import error
import urllib.request
from urllib.parse import quote # urllib请求url里面带中文就会报错用这个抱住就可以了
from lib.Auxiliary import current_time
from conf import config # 配置文件

# choose_color_2  随机颜色 UseStyle指定颜色
from lib.choose import UseStyle,choose_color_2


count = 1 # 记录请求多少次

schedule=0 # 数数
pl=0 # 记录批量扫描的数量

# 批量扫描
def Batch_scan(path):
    Batch=[]
    i = 1
    # 叫文件内容变成
    search_url=queue.Queue()
    thefile=open(path, encoding="UTF-8")

    # 统计有多少行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        i += buffer.count('\n')

    print(UseStyle(f"{'-'*20}文件一共有"+str(i)+f"条目标{'-'*20}",fore='yellow'))
    # 叫每一行内容都保存到search_url中
    for i in open(path, encoding="UTF-8"):
        Batch.append(i.rstrip())

    return Batch

# 读取字典文件内容
def Read_dictionary(path):
    global schedule

    # 叫文件内容变成
    search_url=queue.Queue()
    thefile=open(path, encoding="UTF-8")

    # 统计有多少行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        schedule += buffer.count('\n')

    print(UseStyle("文件一共有"+str(schedule)+"条",fore='yellow'))
    # 叫每一行内容都保存到search_url中
    for i in open(path, encoding="UTF-8"):
        search_url.put(i.rstrip())

    return search_url


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['ProbeBackup'], 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

# 单位换算
def covertFukeSize(size):

    size=int(size)

    kb = 1024
    mb = kb * 1024
    gb = mb * 1024
    tb = gb * 1024

    if size >= tb:
        return "文件小%.1f TB" % float(size / tb)
    if size >= gb:
        return "文件小%.1f GB" % float(size / gb)
    if size >= mb:
        return "文件小%.1f MB" % float(size / mb)
    if size >= kb:
        return "文件小%.1f KB" % float(size / kb)
    else:
        return '文件小于1kb'



def ask(url,url_exists,proxies):
    HeadersConfig = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    global count
    while not url_exists.empty():
        searchurl=url_exists.get()


        #print(current_time() + f"进度: {count}/{schedule}", "\r", end='')
        try:

            print(f"\r{current_time()} 进度: {count}/{schedule}",  end="\r")
            back = urllib.request.Request(url=url+quote(searchurl), headers=config.HeadersConfig,method='GET')

            # 是否使用代理
            if proxies != None:

                # 使用选择的代理构建代理处理器对象
                httpproxy_handler = urllib.request.ProxyHandler(proxies)

                # 通过 urllib.request.build_opener(),创建自定义opener对象
                opener = urllib.request.build_opener(httpproxy_handler)

                #发送代理请求
                response = opener.open(back, timeout=7) # 代理请求

            else:
                response = urllib.request.urlopen(back, timeout=7)

            if response.status == 200:
                count += 1
                content = response.headers['content-length']
                content=covertFukeSize(content)
                print(UseStyle(f"\t\t\t\t\t\n{'*'*20}\n请求这个备份文件存在：" +url+ searchurl+f'文件大小：\t{content}\n{"*"*20}\n', fore='green'))
                Searchresults(url+searchurl+f'\t\t文件大小：{content}')

        except Exception as cw:
            if str(cw) in "HTTP Error 404: Not Found":  # 报错404的
                count += 1
            if str(cw) in "<urlopen error [Errno 113] No route to host>":  # 报错超时的
                print('\n目标未7响应时间超时了！')
                break

# 设置线程
def Thread(url,url_exists,T,proxies):

    threadpool = []
    for _ in range(int(T)):
        Threads = threading.Thread(target=ask, args=(url,url_exists,proxies, ))
        threadpool.append(Threads)
    for th in threadpool:
        th.start()
    for th in threadpool:
        threading.Thread.join(th)


def splicing(url,url_s,segmentation,T,proxies):
    url_exists = queue.Queue()
    dictionary = ['index.php.txt',
                  'backup.zip',
                  'website.zip',
                  'web.zip',
                  'index.zip',
                  'wwwroot.zip',
                  'faisunzip.zip',
                  'wwwroot.rar',
                  'wwwroot.tar.gz',
                  'wwwroot.gz',
                  'wwwroot.sql.zip',
                  'back.zip',
                  'wwwroot.sql',
                  'www.zip',
                  'backup.zip',
                  'bbs.zip',
                  'www.tar.gz',
                  "我的.txt"]
    small = [chr(i) for i in range(97,123)] # a-z
    calltaxi = [chr(i) for i in range(97, 123)]  # A-Z
    number = [str(i) for i in range(0, 10)] # 0-9

    suffix = ['.zip',
              '.rar',
              '.tar.gz',
              '.sql.gz',
              '.7z',
              '.sql',
              '.tar.tgz',
              '.tar.bz2',
              '.gz',
              '.tar.xz',
              '.log.gz',
              '.log.bz2',
              '.log.xz',
              '.wim',
              '.lzh',
              '.bak',
              '.txt',
              '.old',
              '.jar',
              '.temp']

    for i in small:  # a-z
        for Extract_4 in suffix:
            url_exists.put(i+Extract_4)

    for i in calltaxi:  # A-Z
        for Extract_5 in suffix:
            url_exists.put(i + Extract_5)

    for i in number:  # 0-9
        for Extract_6 in suffix:
            url_exists.put(i + Extract_6)

    for Extract_1 in dictionary:# 默认字典
        url_exists.put(Extract_1)

    for i in suffix: # 分割拼接
        for Extract_2 in segmentation:
            url_exists.put(Extract_2+i)

    for Extract_3 in suffix:# 域名拼接
        url_exists.put(url_s+Extract_3)

    global schedule
    schedule = str((len(url_exists.queue)))

    Thread(url,url_exists,T,proxies)


def fix(url,T,document,proxies):

    # 自动添加协议头
    if url.startswith('http://') or url.startswith('https://'):
        if 'http://' in url:
            http = 'http://'
        elif 'https://' in url:
            http = 'https://'
    else:
        try: # 判断目标是不是目标是不是https
            http='https://'
            url=http+url.strip()
            r = requests.get(url=url,headers=config.HeadersConfig)
        except requests.exceptions.SSLError:
            http = 'http://'
            url=url.replace('https://', http)


    url_s = url.replace(http, '')
    if url[-1] != '/':
        url += '/' # 查看最后一个是否有/没有添加/

    if ':' in url_s:
        url_s=url_s.split(':')[0]
        segmentation=url_s.split('.')

    else:
        segmentation=url_s.split('.')
    if document==None:
        splicing(url,url_s,segmentation,T,proxies)
        return
    else:
        document_=Read_dictionary(document)
        print("使用的字典是"+document+"\n\n")
        Thread(url,document_,T,proxies)




def Interface(args):

    args.url=args.PB
    args.many=args.PBm
    args.thread = args.PBt
    args.document = args.PBd
    args.proxies = args.PBp #代理

    global pl
    if args.url !=None or args.many != None:
        if args.thread==None:
            args.thread=1

        # 设置代理
        if args.proxies != None:
             args.acting=args.proxies
             args.proxies= {
                "http": "http://" +args.acting ,
                "https": "http://" + args.acting
            }

        # 是否批量扫描
        if args.many == None:
            print(choose_color_2("扫描结果会保存到：result/ProbeBackup/文件夹里面\n你输入的目标地址是: " +
                                 args.url +
                                 '\n线程数是：' +
                                 str(args.thread) +
                                 "\n使用自动生成字典扫描！"+
                                 f'\n\033[0;33m {"—" * 60}\033[0m'))

            fix(args.url,args.thread,args.document,args.proxies)
        else:
            #print(Batch_scan(args.many))
            Many_Batch=Batch_scan(args.many) # 批量扫描
            for url in Many_Batch:
                count = 1  # 记录请求多少次
                schedule =1 # 重置字典的数量
                pl += 1  # 记录批量扫描的数量
                print(choose_color_2(
                                     f"\n\n扫描结果会保存到result/ProbeBackup/文件夹里面\n正在扫描：{url} 第{str(pl)}个目标"+
                                     f"\n线程数是：{str(args.thread)}"))
                fix(url,args.thread,args.document,args.proxies)