import requests
#from conf import config
import queue
import threading
from urllib import error
import urllib.request
from urllib.parse import quote # urllib请求url里面带中文就会报错用这个抱住就可以了
from lib.Auxiliary import current_time
from lib.choose import UseStyle
from lib.choose import choose_color_2


count = 1 # 记录请求多少次

schedule=0 # 数数
save = None #保存开关


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

    print(UseStyle("文件一共有"+str(i)+"条目标",fore='yellow'))
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
    global save
    Searchresults_document = open(save, 'a')  # 打开文件写的方式
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
        return "%.1f TB" % float(size / tb)
    if size >= gb:
        return "%.1f GB" % float(size / gb)
    if size >= mb:
        return "%.1f MB" % float(size / mb)
    if size >= kb:
        return "%.1f KB" % float(size / kb)
    else:
        return '文件小于1kb'



def ask(url,url_exists):
    HeadersConfig = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    global count
    global save
    while not url_exists.empty():
        searchurl=url_exists.get()


        #print(current_time() + f"进度: {count}/{schedule}", "\r", end='')
        try:

            print(current_time() + f"进度: {count}/{schedule}" + f"正在探测: {url + searchurl}","\r", end='', flush=True)
            back = urllib.request.Request(url=url+quote(searchurl), method='GET')
            response = urllib.request.urlopen(back, )
            if response.status == 200:
                count += 1
                content = response.headers['content-length']
                content=covertFukeSize(content)
                print()
                print(current_time() + UseStyle(f"请求第[{str(count)}]这个备份文件存在：" + searchurl+f'文件大小：{content}', fore='green'))
                if save != None:
                    Searchresults(url+searchurl+f'\t\t文件大小：{content}')

        except:
            count+=1
            # print(UseStyle(f'请求第[{str(schedule)}][*]这个地址不存在：',fore='yellow')+UseStyle(url+searchurl+'\t\t\t\t\t[*]'+"状态码："+str(e.code),fore='red'))
            #print("\r",current_time() + f"正在探测: {searchurl}"+ f"进度: {count}/{schedule}",  end='')

def Thread(url,url_exists,T):

    for i in range(int(T)):
        Threads = threading.Thread(target=ask, args=(url,url_exists, ))
        Threads.start()
def splicing(url,url_s,segmentation,T):
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

    Thread(url,url_exists,T)


def fix(url,T,document,save_):



    global save
    save=save_
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
            r = requests.get(url=url)
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
        splicing(url,url_s,segmentation,T)
        return
    else:
        document_=Read_dictionary(document)
        Thread(url,document_,T)




def Interface(args):

    if args.thread==None:
        args.thread=1
    if args.many == None:
        print(choose_color_2(
            "\n你输入的目标地址是: " + args.b + '\n线程数是：' + str(args.thread) + f'\n\033[0;33m {"—" * 60}\033[0m'))
        fix(args.b,args.thread,args.document,args.save)
    else:
        #print(Batch_scan(args.many))
        Many_Batch=Batch_scan(args.many)
        for url in Many_Batch:
            count = 1  # 记录请求多少次
            fix(url,args.thread,args.document,args.save)