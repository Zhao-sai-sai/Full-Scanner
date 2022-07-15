import re
import time
import urllib.parse
from conf import config # 配置文件

# 提取出来的结果保存起来
def Searchresults(results_IP,current_time):
    Searchresults_document = open(current_time, 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件




# 光提取文件中的域名/IP、比如文件有一个http://1.1.1.1/x/x/x/x、提取出来的就是1.1.1.1
def Interface_dns(url):

    current_time = config.Savelocation['Contentextraction_dns']
    print("正在提取！")
    for dns in open(url):
        domian = urllib.parse.urlparse(dns).netloc
        if not domian=='':
            Searchresults(domian,current_time)
    print(f"提取完成文件保存在：{current_time}")


# 取文件中的和[http/https://]+域名、比如文件有一个http://1.1.1.1/x/x/x/x、提取出来的就是http://1.1.1.1
def Interface_http(url):
    current_time = config.Savelocation['Contentextraction_http']
    print("正在提取！")
    for dns in open(url):
        a = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{6}))+', dns)
        for i in a:
            Searchresults(i, current_time)
    print("提取完成文件保存在："+current_time)



if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d%H:%M:%S", time.localtime()) + 'http.txt'
    print("正在提取！")
    for dns in open('dns.txt'):
        a = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{6}))+', dns)
        for i in a:
            Searchresults(i, current_time)
    print("提取完成文件保存在："+current_time)