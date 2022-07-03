#import urllib.request
import whois
from conf import config
import requests
from lxml import etree
import  re

# choose_color_2  随机颜色
from lib.choose import UseStyle

# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['whois'], 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

def Whois_centralops(dns):
    data = {
        "__VIEWSTATE": "",
        "addr": dns,
        "dom_whois": "true",
        "net_whois": "true",
        # "net_whois":"true",
    }
    headers = {
        'Host': 'centralops.net',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://centralops.net/co/DomainDossier.aspx',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://centralops.net',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    html = requests.post(url="http://centralops.net/co/DomainDossier.aspx", headers=headers, data=data)
    html = etree.HTML(html.text)
    divs = html.xpath(r'//body/pre/text()')  # 语法
    divs[1] = re.sub('\n\n', '\n', divs[1])  # 俩个回车变成一个
    divs[0] = re.sub('\n\n', '\n', divs[0])  # 俩个回车变成一个
    import time
    data = f"""
    {"*"*14}centralops引起查询：网络 Whois 记录{"*"*14}
    {divs[1]}\n
    {"*"*14}centralops引起查询：域 Whois 记录{"*"*14}
    {divs[0]}
    """
    return data
    # print("--------------centralops引起查询：网络 Whois 记录-------------")
    # time.sleep(2)
    # print(divs[1])
    #
    #
    # print("--------------centralops引起查询：域 Whois 记录--------------")
    # time.sleep(2)
    # print(divs[0])


def Whois_check(DNS):
    centr_alops=Whois_centralops(DNS)
    print(UseStyle(centr_alops,fore="yellow"))
    try:
        req_whois = whois.whois(DNS)
        # print(req_whois)
        data=f"""
        "自带的'
        "注册商：{str(req_whois["registrar"])}
        "域名服务器：{str(req_whois["whois_server"])}
        "推荐网址：{str(req_whois["referral_url"])}
        "更新时间：{str(req_whois["updated_date"])}
        "创建时间：{str(req_whois["creation_date"])}
        "过期时间：{str(req_whois["expiration_date"])}
        "名称服务器：{str(req_whois["name_servers"])}
        "电子邮件：{str(req_whois["emails"])}
        "邮政编码：{str(req_whois["zipcode"])}
        "status：{str(req_whois["status"])}
        "dnssec：{str(req_whois["dnssec"])}
        "名称：{str(req_whois["name"])}
        "组织：{str(req_whois["org"])}
        "城市：{str(req_whois["city"])}
        "国家：{str(req_whois["country"])}\n"""
        print(UseStyle(data,fore="yellow"))
        Searchresults((("#"*100)+"\n查询的目标是："+DNS+centr_alops+data+("#"*100)))
    except:
        print("请求出错：可能是你请求太多了，或者换一个域名，或者重新请求")

def Interface(args):
    DNS=args.whois
    DNS=DNS.strip()

    # 检查dns前面是不是有http或者有https://，有替换空
    DNS=DNS.replace("http://",'')
    DNS = DNS.replace("https://", '')
    DNS = DNS.replace("/", '')

    print("结果会保存到："+config.Savelocation['whois']+"\n当前查询的目标是："+DNS+f'\n\033[0;33m {"*"*60}\033[0m')

    # 利用万网提供了域名查询接口，查看域名的情况
    # <returncode>200</returncode> 返回码，200表示返回成功
    # <key>doucube.com</key>  表示当前查询的域名
    # <original>211 : Domain name is not available</original> 返回结果的原始信息，主要有以下几种
    #
    # original=210 : Domain name is available     表示域名可以注册
    # original=211 : Domain name is not available 表示域名已经注册
    # original=212 : Domain name is invalid       表示查询的域名无效
    # original=213 : Time out 查询超时

    # Inquire_DNS=('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain='+DNS.strip())
    #
    # # 发送请求
    # req = urllib.request.urlopen(Inquire_DNS)
    #
    # # 获得响应数据
    # Inquire_DNS=req.read().decode()
    # print("响应：\n"+Inquire_DNS)
    #
    # if "210" in str(Inquire_DNS):
    #     print(DNS+"：域名可以注册")
    # elif "211" in str(Inquire_DNS):
    #     print(DNS+"：域名已经注册\n")

    Whois_check(DNS)
    # elif "212" in str(Inquire_DNS):
    #     print(DNS+"：表示查询的域名无效")
    # elif "213" in str(Inquire_DNS):
    #     print(DNS+"：查询超时")


