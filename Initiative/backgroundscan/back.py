# -*- coding:utf-8 -*-
import urllib.request
import threading
from urllib import error
import time
from conf import config # 配置文件
import queue
from lib.Auxiliary import current_time,Wire
from urllib.parse import quote # urllib请求url里面带中文就会报错用这个抱住就可以了
import sys
# choose_color_2  随机颜色 UseStyle指定颜色
from lib.choose import UseStyle,choose_color_2


schedule = 0 # 记录请求多少次
pl=0 # 记录批量扫描的数量
count=0 # 记录文件内容一个多少行

# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['back'], 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

# 批量扫描
def Batch_scan(path):
    Batch=[]
    i = 1
    # 叫文件内容变成
    search_url=queue.Queue()
    thefile=open(path,mode='br', encoding="UTF-8")

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
def Read_dictionary(document):
    global count # 记录文件内容一个多少行

    # 叫文件内容变成
    search_url=queue.Queue()
    thefile=open(document)

    # 统计有多少行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')

    print(UseStyle("文件一共有"+str(count)+"条",fore='yellow'))
    print(Wire())
    # 叫每一行内容都保存到search_url中
    for i in open(document, encoding="UTF-8"):
        search_url.put(i.rstrip())

    return search_url



def ask(search_url,url,proxies):

    while not search_url.empty():

        searchurl=search_url.get()
        #time.sleep(1)  # 暂停 1 秒
        #print(searchurl)
        try:
            #print(config.HeadersConfig)
            global schedule

            print(f"\r{current_time()} 进度: [{schedule}/{count}]",end='')
            #back=requests.get(url+i,headers=config.HeadersConfig)
            back = urllib.request.Request(url=(url+quote(searchurl)), headers=config.HeadersConfig, method='GET')

            if proxies != None:

                # 使用选择的代理构建代理处理器对象
                httpproxy_handler = urllib.request.ProxyHandler(proxies)

                # 通过 urllib.request.build_opener(),创建自定义opener对象
                opener = urllib.request.build_opener(httpproxy_handler)

                #发送代理请求
                response = opener.open(back, timeout=7) # 代理请求

            else:
                response = urllib.request.urlopen(back, timeout=7)

            if response.status==200:
                schedule+=1

                print(UseStyle(
                    f"\t\t\t\t\t\n\n{'*' * 20}\n请求这个地址存在：" + url + searchurl + f"\n{'*' * 20}\n\n",
                    fore='green'))


                #print(+)
                # print("\r", end="")
                # Searchresults(url + searchurl)
                # print('\r'+current_time()+f"进度: {schedule}/{count}",end='')


            elif response.status==301:
                schedule += 1

                print(UseStyle(
                    f"\t\t\t\t\t\n\n{'*' * 20}\n请求这个地址存在：" + url + searchurl + f"\n{'*' * 20}\n\n",
                    fore='green'))

                #print(current_time() + UseStyle(f"请求第[{str(schedule)}]这个地址存在：" + url + searchurl, fore='green'))
                # print("\r", end="")
                # Searchresults(url + searchurl)
                # print('\r'+current_time()+f"进度: {schedule}/{count}",end='')

        except error.HTTPError as cw:
            if str(cw) in "HTTP Error 404: Not Found":  # 报错404的
                schedule += 1
            if str(cw) in "<urlopen error [Errno 113] No route to host>": # 报错超时的
                print('\n目标未7响应时间超时了！')
                break
        except Exception as bc:
            print("未知错误！" + str(bc))

            #print(UseStyle(f'请求第[{str(schedule)}][*]这个地址不存在：',fore='yellow')+UseStyle(url+searchurl+'\t\t\t\t\t[*]'+"状态码："+str(e.code),fore='red'))

def Thread(url,T,document,proxies):
    threadpool = []
    search_url=Read_dictionary(document)
    for _ in range(int(T)):
        Threads = threading.Thread(target=ask, args=(search_url, url,proxies))
        threadpool.append(Threads)
    for th in threadpool:
        th.start()
    for th in threadpool:
        threading.Thread.join(th)



def Interface(args):
    print(args.url)
    args.url=(args.url.strip())

    if args.url[-1]!='/': # 查看最后一个是否有/没有添加/
        args.url+='/'
    args.thread=int(args.thread)

    Thread(args.url,args.thread,args.document,args.proxies)

def Interfacemian(args):
    global pl
    args.url=args.BK
    print(args.BK)
    args.many=args.BKm
    args.document=args.BKd
    args.thread=args.BKt
    args.proxies=args.BKp #代理

    if args.url != None or args.many != None:
        # 默认字典
        if args.document == None:
            args.document = config.Specifyablastdictionary['back']

        # 设置代理
        if args.proxies != None:
             args.acting=args.proxies
             args.proxies= {
                "http": "http://" +args.acting ,
                "https": "http://" + args.acting
            }

        # 默认线程
        if args.thread == None:
            args.thread = 10



        if args.many == None:
            print(UseStyle(f'扫描结果保存在{config.Savelocation["back"]}文件夹下\n' +
                           '目标地址是：' +
                           args.url +
                           "\n线程数是：" +
                           str(args.thread) +
                           '\n字典：' +
                           args.document,
                           fore='yellow'))
            Interface(args)

        else:
            # 批量扫描
            Many_Batch=Batch_scan(args.many)
            for url in Many_Batch:
                count = 1  # 记录请求多少次
                schedule = 1  # 重置字典的数量
                args.url=url
                pl += 1  # 记录批量扫描的数量
                print(choose_color_2(f'\n\n\n扫描结果保存在{config.Savelocation["back"]}文件夹下' +
                                     '\n字典：' +
                                     args.document+
                                     f"\n正在扫描：{url} 第{str(pl)}个目标"+
                                     f"\n线程数是：{str(args.thread)}"))
                Interface(args)