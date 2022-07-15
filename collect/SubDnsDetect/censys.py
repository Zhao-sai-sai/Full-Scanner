#import numpy #删除列表重复的
import requests
from bs4 import BeautifulSoup
import re
import urllib3
urllib3.disable_warnings()  # 忽略https证书告警

def DNS_Climb_censys(DNS):
    try:
        amount = 4  # 默认页数

        Dns_List = []
        headers={
            'Host': 'search.censys.io',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'close',
            'Referer': 'https://search.censys.io',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        for i in range(int(amount)):
            url=f"https://search.censys.io/certificates/_search?q={DNS}&page={i}"
            html=requests.get(url=url,headers=headers,verify=False)
            soup = BeautifulSoup(html.text, 'lxml')
            dns_ = soup.find_all(text=re.compile(rf"{DNS}"))
            for i in dns_: # 临时发挥写的现在我也懵看不太懂
                a=re.sub('\*=', '', i)
                a=a.split(',')[0]
                a = a.split('=')
                if len(a)==2:
                    if not (a in Dns_List):  # 取反如果Dns_List列表里面有就不添加
                        Dns_List.append(a[1])

        #Dns_List=numpy.unique(Dns_List)
        return Dns_List

    except Exception as bc:
        print("有错误！错误提示" + str(bc))

if __name__=="__main__":
    print(DNS_Climb_censys('zssnp.top'))
