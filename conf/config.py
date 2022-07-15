import time
import random
from pathlib import Path
import os

def folder_creation(folder): # 查文件夹是否存在，不存在创建
    my_file = Path(folder)
    if not my_file.is_dir():
        os.makedirs(folder)

folder_creation('./result/back') # 查文件夹是否存在，不存在创建
folder_creation('./result/cms')# 查文件夹是否存在，不存在创建
folder_creation('./result/fofa')# 查文件夹是否存在，不存在创建
folder_creation('./result/ftp')# 查文件夹是否存在，不存在创建
folder_creation('./result/ProbeBackup')# 查文件夹是否存在，不存在创建
folder_creation('./result/searchengine')# 查文件夹是否存在，不存在创建
folder_creation('./result/shodan')# 查文件夹是否存在，不存在创建
folder_creation('./result/ssh')# 查文件夹是否存在，不存在创建
folder_creation('./result/webcrack')# 查文件夹是否存在，不存在创建
folder_creation('./result/whois')# 查文件夹是否存在，不存在创建
folder_creation('./result/Contentextraction')# 查文件夹是否存在，不存在创建



current_time=time.strftime("%Y-%m-%d%H:%M:%S", time.localtime())



SeriousConfig={
    'fofa':'',  # fofa的cookie
    'shodan':'' # shodan的api
}





ua_list = [
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
]

userAgent = random.choice(ua_list) # 随机 User-Agent
HeadersConfig={
    'User-Agent':userAgent
}

# 需要的字典的位置设置
Specifyablastdictionary={
    'ftp':{'admin':'dictionary/ftp/admin.txt','passwd':'dictionary/ftp/passwd.txt'},
    'backgroundscan':'dictionary/BackgroundDetection/ask.txt',
    'extracted':{'admin':'dictionary/extracted/admin.txt','passwd':'dictionary/extracted/passwd.txt'},

    # ssh字典
    'ssh':{'admin':'dictionary/ssh/admin.txt','passwd':'dictionary/ssh/passwd.txt'},
    # 后台扫描的字典
    'back':'dictionary/BackgroundDetection/ask.txt',

}


# 输出的结果保存到位置
Savelocation={

    # fofa保存
    'fofa':f'result/fofa/{current_time}fofa.txt',

    # shodan保存
    'shodan':f'result/shodan/{current_time}shodan.txt',

    'back':f'result/back/{current_time}backgroundscan.txt',

    # cms识别保存
    'cms':f'result/cms/{current_time}cms.txt',

    # whois保存
    'whois': f'result/whois/whoislog.txt',

    # bing
    'bing': f'result/searchengine/{current_time}bing.txt',

    # google
    'google': f'result/searchengine/{current_time}google.txt',

    # 备份文件扫描保存
    'ProbeBackup':f'result/ProbeBackup/{current_time}ProbeBackup.txt',

    # 网页破解保存
    'webcrack': f'result/webcrack/{current_time}webcrack.txt',

    # ftp破解保存
    'ftp': f'result/ftp/{current_time}ftp.txt',

    # ssh破解保存
    'ssh': f'result/ssh/{current_time}ssh.txt',

    # 文件的中的域名提取保存
    'Contentextraction_dns': f'./result/Contentextraction/{current_time}dns.txt',
    'Contentextraction_http': f'./result/Contentextraction/{current_time}http.txt',

}
