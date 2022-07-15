# -- coding:UTF-8 --
import requests
from lxml import etree
import urllib3
from urllib.parse import urlparse # urlparse提取url的dns
from conf import config # 配置文件

urllib3.disable_warnings()  # 忽略https证书告警

def DNS_Climb_bing(keywords):
    amount = 10 # 默认页数
    Dns_List=[]
    for i in range(0, int(amount)):
        url = f"https://cn.bing.com/search?q={keywords}&go=%E6%90%9C%E7%B4%A2&qs=ds&first={i}1&FORM=PERE1"
        try:
            html = requests.get(url=url, headers=config.HeadersConfig, verify=False, timeout=5)
            # //div[@id="search"]//div//div//div//div//div//div/a[@data-ved]/@href
            html = etree.HTML(html.text)
            divs = html.xpath(r'//div/h2/a/@href')  # 语法


            #print(divs2)
            for DNS in divs:
                DNS_Res = urlparse(DNS).netloc #　获得url里面的域名

                if not(DNS_Res in Dns_List): # 取反如果Dns_List列表里面有就不添加

                    Dns_List.append(DNS_Res)


        except Exception as bc:
            print("有错误！错误提示" + str(bc))


        return Dns_List
