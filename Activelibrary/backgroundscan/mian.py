# -*- coding:utf-8 -*-
import urllib.request
import threading
from urllib import error
import time
from datetime import datetime
from lib.choose_model import Auxiliary
from conf import config
import queue
from lib.choose import UseStyle
from lib.choose_model.Auxiliary import current_time,Wire
from urllib.parse import quote # urllib请求url里面带中文就会报错用这个抱住就可以了

schedule = 0 # 记录请求多少次

count=0 # 记录文件内容一个多少行

# 读取字典文件内容
def Read_dictionary():
    global count

    # 叫文件内容变成
    search_url=queue.Queue()
    thefile=open('dictionary/BackgroundDetection/php.txt')

    # 统计有多少行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')

    print(UseStyle("文件一共有"+str(count)+"条",fore='yellow'))
    print(Wire())
    # 叫每一行内容都保存到search_url中
    for i in open('dictionary/BackgroundDetection/php.txt'):
        search_url.put(i.rstrip())

    return search_url



def ask(search_url,url):
    while not search_url.empty():
        searchurl=search_url.get()
        time.sleep(1)  # 暂停 1 秒
        #print(searchurl)
        try:
            global schedule
            #back=requests.get(url+i,headers=config.HeadersConfig)
            back = urllib.request.Request(url=(url+quote(searchurl)), headers=config.HeadersConfig, method='GET')
            response = urllib.request.urlopen(back,)
            print()
            if response.status==200:
                schedule+=1
                print(current_time()+UseStyle(f"请求第[{str(schedule)}]这个地址存在："+url+searchurl,fore='green'))
                print("\r", end="")
                print(current_time()+f"进度: {schedule}/{count}","\r", end='')
            elif response.status==301:
                schedule += 1
                print(current_time()+UseStyle(f"请求第[{str(schedule)}]这个地址存在："+url+searchurl,fore='green'))
                print("\r", end="")
                print(current_time()+f"进度: {schedule}/{count}","%\r", end='')
        except error.HTTPError as e:
            schedule += 1
            #print(UseStyle(f'请求第[{str(schedule)}][*]这个地址不存在：',fore='yellow')+UseStyle(url+searchurl+'\t\t\t\t\t[*]'+"状态码："+str(e.code),fore='red'))
            print(current_time()+f"进度: {schedule}/{count}","\r", end='')

def Thread(url,T):
    search_url=Read_dictionary()
    for i in range(int(T)):
        Threads = threading.Thread(target=ask, args=(search_url, url))
        Threads.start()

def Interface(url):
    T = int(input(UseStyle('请输入请求线程(默认线程3)：',fore='green')))
    if T=='':
        T=3
    if url[-1]!='/': # 查看最后一个是否有/没有添加/
        url+='/'
    print(UseStyle('目标地址是：'+url+"\n线程数是："+str(T),fore='yellow'))
    Thread(url,T)

