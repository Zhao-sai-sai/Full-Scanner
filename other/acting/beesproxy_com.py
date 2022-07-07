import requests

from lxml import etree



def verify(proxies, ip, PORT):
    print(proxies)
    try:
        response = requests.get(url="http://www.baidu.com/", proxies=proxies, timeout=1)
        if response.status_code == 200:
            print("这个IP可以用:" + ip + ':' + PORT)

    except:
        print('这个代理不可用')


    # headers = headers_()
    #
    # try:
    #     html = requests.get('http://httpbin.org/get', proxies=proxies, timeout=2)
    #
    #     print(html)
    #     # html = etree.HTML(html.text)
    #     #
    #     # IP = html.xpath(r'//th/div[@id="tab0_ip"]/text()')  # 提取ip
    #     # address=html.xpath(r'//th/div[@id="tab0_address"]/text()')  # 地址
    #     # print("可以用的：IP"+IP+"地址:"+address)
    #     IP = re.findall(r'\d+\.\d+\.\d+\.\d+', html.text)[0]
    #     print("这个IP可以用:" + IP + ':::::' + ip + ':' + PORT)
    #
    #     Searchresults((ip + ':' + PORT))
    #     print("===================================")
    # except Exception:
    #     print("这个代理不可用")


# 判断代理方式
def judge(ip, PORT, protocol):
    print("正在验证")
    if protocol == 'HTTP':
        proxies = {"http": ('http://' + ip + ':' + PORT)}
        verify(proxies, ip, PORT)
    elif protocol == 'SOCKS5':
        proxies = {"http": ('socks5://' + ip + ':' + protocol)}
        verify(proxies, ip, PORT)



# 提取代理服务器地址和端口地方
def collection():
    headers = {  # 定义User-Agent请求头，用键值对的方式
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }
    html=requests.get("http://ip.yqie.com/ipproxy.htm",headers=headers)

    html = etree.HTML(html.text)
    #for i in range(4):

    IP=html.xpath(r"//tbody/tr/td[1]/text()") # 提取ip
    PORT=html.xpath(r"//tbody/tr/td[2]/text()") # 提取端口
    Location=html.xpath(r"//tbody/tr/td[3]/text()") # 提取地区
    anonymous=html.xpath(r"//tbody/tr/td[4]/text()") # 提取匿名程度
    protocol=html.xpath(r"//tbody/tr/td[5]/text()") # 提取协议
    print(IP)
    # for i in range(20):
    #     print("===================================")
    #     print("ip地址是：" + IP[i] + "端口是" + str(PORT[i]) + "\n匿名程度：" + anonymous[i] + "\n用的协议" + str(
    #         protocol[i]) + "\n位置在:" + Location[i])
    #     judge(IP[i], str(PORT[i]), protocol[i])
collection()