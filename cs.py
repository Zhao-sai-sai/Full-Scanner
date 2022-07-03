import requests
from urllib import error
import urllib.request


# proxy="127.0.0.1:8889"
#
# proxies = {
#   "http": "http://"+proxy,
#   "https": "http://"+proxy
# }
# HeadersConfig = {
#   'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
# }
# back = urllib.request.Request(url="http://www.baidu.com", headers=HeadersConfig , method='GET')
#
#
# # 构建代理Handler
# httpproxy_handler = urllib.request.ProxyHandler(proxies)
#
# # 通过 urllib.request.build_opener(),创建自定义opener对象
# opener = urllib.request.build_opener(httpproxy_handler)
#
# # 发送代理请求
# response = opener.open(back)
#
# print(response.read().decode('utf-8'))

# p="127.0.0.1:8889"
#
# proxies = {
#   "http": "http://"+p,
#   "https": "http://"+p
# }
# proxies=None
# html = requests.get(url="https://www.google.com.hk/webhp?hl=zh-CN&sourceid=cnhp", proxies=proxies)
#
# print(html.text)
















# from colorama import init
# import time
# init(autoreset=True)
# for i in range(10):
#     time.sleep(1)
#     print("now is :", i, end='\r')
# coding=utf8
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)

for i in range(100):
    time.sleep(1)
    print(Fore.RED + str(i), end='\r')

