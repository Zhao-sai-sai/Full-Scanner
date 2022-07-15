# -- coding:UTF-8 --
import requests
from lxml import etree
import urllib3
from urllib.parse import quote
import time
#from conf import config # 配置文件
urllib3.disable_warnings()  # 忽略https证书告警

from lib.choose import UseStyle  # 设置颜色
from conf import config  # 配置文件


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['google'], 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件


def Climb_Google(proxies, url):
    HeadersConfig = {
        'Host': 'www.google.com.hk',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.google.com.hk',
        'sec-ch-ua-platform': "Linux",
        'sec-ch-ua-arch': "x86",
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'empty',
    }
    try:
        html = requests.get(url=url, headers=HeadersConfig, verify=False, proxies=proxies, timeout=5)
        # //div[@id="search"]//div//div//div//div//div//div/a[@data-ved]/@href
        #print(html.text)
        html = etree.HTML(html.text)
        divs = html.xpath('//div[@id="search"]//div//div//div//div//div//div/a[@data-ved]/@href')  # 语法
        divs2 = html.xpath('//a/h3/text()')  # 提取标题
        i1=0
        for i in divs:
            print(UseStyle("标题：《"+str(divs2[i1])+"》",fore='red')+"\n地址："+i) # 输出爬的结果
            i1+=1
            Searchresults(i)
    except IndexError:
        print("标题不匹配")

def combination(keywords, amount,proxies):
    keywords = keywords.replace(' ', '+') # 空格用+来代替
    keywords=quote(keywords, 'utf-8') # 进行url编码



    for i in range(0, int(amount)):
        print(f'\033[0;33m {"*" * 60}\033[0m\n正在爬取第：{i + 1}页')

        url = f"https://www.google.com.hk/search?q={keywords}&hl=zh-CN&start={str(i)}0"

        Climb_Google(proxies, url)


def Interface(args):
    keywords = args.google # 搜索关键字


    # 代理
    proxies = {
            'http': f'http://{args.googlep}',
            'https': f'http://{args.googlep}'}

    if args.googlem == None:  # 页数
        amount=100000
    else:
        amount = args.googlem

    print(UseStyle(f"\n扫描结果保存在{config.Savelocation['google']}文件夹下\n搜索的关键字是：{keywords}\n页数：{amount}",fore='red') + f'\n\033[0;33m ')
    time.sleep(3)  # 暂停 3 秒
    combination(keywords, amount,proxies)

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
    proxies = {
            'http': f'http://127.0.0.1：8889',
            'https': f'http://127.0.0.1：8889'}
    combination(keywords, amount,proxies)