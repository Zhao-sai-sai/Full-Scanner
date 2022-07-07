import requests

from lxml import etree


# def verify(proxies, ip, PORT):
#     print(proxies)
#     try:
#         response = requests.get(url="http://www.baidu.com/", proxies=proxies, timeout=1)
#         if response.status_code == 200:
#             print("这个IP可以用:" + ip + ':' + PORT)
#             Searchresults((ip + ':' + PORT))
#     except:
#         print('这个代理不可用')
# def judge(ip, PORT, protocol):
#     print("正在验证")
#     if protocol == 'HTTP':
#         proxies = {"http": ('http://' + ip + ':' + PORT)}
#         verify(proxies, ip, PORT)
#     elif protocol == 'SOCKS5':
#         proxies = {"http": ('socks5://' + ip + ':' + protocol)}
#         verify(proxies, ip, PORT)



html = requests.get(url="http://ip.yqie.com/ipproxy.htm")

html.encoding = "utf-8"
print(html.text)
html = etree.HTML(html.text)

IP = html.xpath(r"//table//tbody/tr/td[1]")  # 提取ip
# PORT = html.xpath(r"//tbody/tr/td[2]/text()")  # 提取端口
# Location = html.xpath(r"//tbody/tr/td[3]/text()")  # 提取地区
# anonymous = html.xpath(r"//tbody/tr/td[4]/text()")  # 提取匿名程度
# protocol = html.xpath(r"//tbody/tr/td[5]/text()")  # 提取协议

print(IP)
# for i in range(17):
#     print("===================================")
#     print("ip地址是：" + IP[i] + "端口是" + str(PORT[i]) + "\n匿名程度：" + anonymous[i] + "\n用的协议" + str(
#         protocol[i]) + "\n位置在:" + Location[i])
#     judge(IP[i], str(PORT[i]), protocol[i])