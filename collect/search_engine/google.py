# -- coding:UTF-8 --
import requests
import time
import argparse
from lxml import etree
import urllib3
#from conf import config # 配置文件

urllib3.disable_warnings()  # 忽略https证书告警


# # 提取出来的结果保存起来
# def Searchresults(results_IP):
#     Searchresults_document = open(, 'a')  # 打开文件写的方式
#     Searchresults_document.write((results_IP + '\n'))  # 写入
#     Searchresults_document.close()  # 关闭文件


def Climb_Google(proxies, url):
    HeadersConfig = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }

    html = requests.get(url=url, headers=HeadersConfig, verify=False, proxies=proxies, timeout=5)
    # //div[@id="search"]//div//div//div//div//div//div/a[@data-ved]/@href
    #print(html.text)
    html = etree.HTML(html.text)
    divs = html.xpath('//div[@id="search"]//div//div//div//div//div//div/a[@data-ved]/@href')  # 语法

    for i in divs:
        #print("执行力")
        print(i)
        #Searchresults(i)


def combination(keywords, amount):
    proxies = {
        "http": f"http://127.0.0.1:8889",
        "https": f"http://127.0.0.1:8889",
    }

    for i in range(1, int(amount)):
        #print("执行力")
        url = f"https://www.google.com.hk/search?q={keywords}&hl=zh-CN&ei=ScOqYoPeA8fw4-EP5_en6A8&start={str(i)}0&sa=N&ved=2ahUKEwjDpsaSorH4AhVH-DgGHef7Cf0Q8tMDegQIARA-&biw=1536&bih=738&dpr=1.25"
        #print(url)
        #print()
        Climb_Google(proxies, url)


def Interface(args):
    keywords = "inurl:php?id= '图书馆'"
    #keywords=args.google
    agent=args.GA
    amount = 2
    combination(keywords, amount)
if __name__ == '__main__':
    print("""

      ____ _ _           _        ____                   _      
     / ___| (_)_ __ ___ | |__    / ___| ___   ___   __ _| | ___ 
    | |   | | | '_ ` _ \| '_ \  | |  _ / _ \ / _ \ / _` | |/ _ 
    | |___| | | | | | | | |_) | | |_| | (_) | (_) | (_| | |  __/
     \____|_|_|_| |_| |_|_.__/___\____|\___/ \___/ \__, |_|\___|
                            |_____|                |___/ 

                                                    *作者：赵赛赛""")
    keywords = "site:target.com"
    amount = 2
    combination(keywords, amount,)