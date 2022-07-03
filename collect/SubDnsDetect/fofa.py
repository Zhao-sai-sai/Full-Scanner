import  requests
from lxml import etree
import base64
from urllib.parse import urlparse # urlparse提取url的dns
import time
# from conf import config # 配置文件
#
# # choose_color_2  随机颜色 UseStyle指定颜色
# from lib.choose import choose_color_2,UseStyle



# 第一次请求
def Dns_Request(DNS):
    try:
        DNS = f'domain="{DNS}"'
        DNS = base64.b64encode(DNS.encode('utf-8')).decode("utf-8")


        Dns_List = []
        headers = {
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }
        # 请求
        html=requests.get("https://fofa.info/result?qbase64="+str(DNS),headers=headers)
        html = etree.HTML(html.text)
        divs = html.xpath(r'//span[@class="aSpan"]//@href')  # 探测IP


        for DNS in divs:
            DNS_Res = urlparse(DNS).netloc  # 获得url里面的域名
            if not (DNS_Res in Dns_List):  # 取反如果Dns_List列表里面有就不添加
                Dns_List.append(DNS_Res)
        return Dns_List

    except Exception as bc:
        print("有错误！错误提示" + str(bc))