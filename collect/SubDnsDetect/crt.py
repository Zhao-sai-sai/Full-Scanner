import requests
from bs4 import BeautifulSoup
import urllib3
#from conf import config # 配置文件
import re


urllib3.disable_warnings()  # 忽略https证书告警
headers = {
    'Host': 'crt.sh',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}


def DNS_Climb_Crt(DNS):
    try:
        Dns_List=[]
        html = requests.get(f"https://crt.sh/?q={DNS}",headers=headers,verify=False)
        soup = BeautifulSoup(html.text, 'lxml')
        dns_=soup.find_all(text=re.compile(fr".{DNS}"))

        for i in range(2,len(dns_)):
            if not (dns_[i] in Dns_List):  # 取反如果Dns_List列表里面有就不添加
                Dns_List.append(dns_[i])
        #print(Dns_List)
        return Dns_List
    except Exception as bc:
        print("有错误！错误提示" + str(bc))


if __name__=="__main__":

    DNS_Climb_Crt('zssnp.top')