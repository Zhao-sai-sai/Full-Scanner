import argparse
from lib.choose import choose_color_2 # 随机颜色
from lib.choose import UseStyle # 指定颜色
import random





banner_1 = r"""    
         ___     _ _     ___                            
        | __|  _| | |___/ __| __ __ _ _ _  _ _  ___ _ _ 
        | _| || | | |___\__ \/ _/ _` | ' \| ' \/ -_) '_|
        |_| \_,_|_|_|   |___/\__\__,_|_||_|_||_\___|_| 
"""
banner_2 = r'''
                    _/_/_/_/              _/_/_/   
               _/                  _/          
              _/_/_/  _/_/_/_/_/    _/_/       
             _/                        _/      
            _/                  _/_/_/         
'''

banner_3 = r'''

             _____                                               
        () |_       |\ |\    ()  _   _,               _  ,_  
          /| ||  |  |/ |/----/\ /   / |  /|/|  /|/|  |/ /  | 
         (/    \/|_/|_/|_/  /(_)\__/\/|_/ | |_/ | |_/|_/   |/
'''
banner_4 = """


         __|    | |       __|                              
         _||  | | |____|\__ \  _|  _` |   \    \   -_)  _| 
        _|\_,_|_|_|     ____/\__|\__,_|_| _|_| _|\___|_|  
"""

banner_5 = """


                 _       __                 
                |_  ||__(_  _ _.._ ._  _ ._ 
                ||_|||  __)(_(_|| || |(/_|
"""
banner_6="""

      _   _   _   _   _   _   _   _   _   _   _   _  
     / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
    ( F | u | l | l | - | S | c | a | n | n | e | r )
     \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
"""
banner_7="""
    _____     _ _        _____                                 
    |  ____|   | | |      / ____|                                
    | |__ _   _| | |_____| (___   ___ __ _ _ __  _ __   ___ _ __ 
    |  __| | | | | |______\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    | |  | |_| | | |      ____) | (_| (_| | | | | | | |  __/ |   
    |_|   \__,_|_|_|     |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                               
"""

banner_8="""

        +-+-+-+-+-+-+-+-+-+-+-+-+
         F|u|l|l|-|S|c|a|n|n|e|r
        +-+-+-+-+-+-+-+-+-+-+-+-+

"""

banner_11 = r'''
                                ####                                   #:
                              .+.::.+==                             : : *+
                             #=::#:::-# :                         .+.+#:-#+#
                             #=:::::::#   +...:#--::::..:::..    -*:-:::::==
                             .+-::::::.+##-::::::::::-:-::::::-#+* #:::::::=#
                               .*=::::-::::::-::-:::-::-:-:::::::::::::-:-:=#
                               #=:::::#  =.-:::::::::-::::::::::###-:::::+ #
                              #=.:::+* +.:::#:#----:::::::-:::#:=  *#:::.*=
                             #=#:::-#+::::::#::::::--::#:::-:::-::#= +:::**
                            +:::::::-:::::::::-:::::::::::::::-::--::-:::::=
                          =*+::::-#:::.:::::::::::.:::::--::-#::#::::-::::==#
                         #*+#:::#:::#=    *#::#-#+    +:::::-#####-:--:::::=#
                         #*+#::::#::+ +###**::::#      ::--#*     *-:::::::.=#
                         +*+#:::::::::::::::-:::-+    +:::::+#####+:::-::::#.#:
                          ++#::::######:-:::-::--::..-::::::--:::-:-:::#::::+ *
                          ++#::-#+++#.#+#:::::::::-:#--::--:-:::#+++++#:::#:= *
                          +##::##+++++++#--:-::::#+ *+:::::::--#++++.++#::::= *
                          ++#:::#+++++++#::-:--::#+**#::::::::##+++++++###::= *
                          +++#:::#######-:::-:::::#:::::-:::::##++++++##::::= *
                           ++##::::##::#:::-:::::::::::::::##::::###-#:::::#=
                            ++++#-::::::::::::#:-::--::::::#--:::::::-::-#= #
                             .+++###::::::-:::::-:::##:#:::::-:::-::::-##=+
                              #=+++++#+###:#-:::::::::-:#--#:::::::::-#+*.
                          .+##::+*  +++++++++++++++++#-#-####.#+#+++**=
                         #*+#-::::.+     **=+++++++++++++++++=*** +
                         .*+++++#---+ ******==+++++++++=     =++++. :
                             ******** **********=++=******  +::::::+*#
                                    ********************** =#::::::+*#
                                    ********************** *+###:-+=.
                                    ************************ =+++=
                                   *************************     *
                                   **********==============********* #
                                   ***=+######:::::-:::::::##+#++*** #
                                  #::::::::::::::-::::-####+#-::-=
                                    #::-:::::::::::::###++##:::::-:+*#
                                    ::::-#++#########++++++#::::-:.+*#
                                   -*:::::::###+++++++=*=+++###::##=*#
                                   .=##:::#:::#+++* **= ***++++#+++==
                                      +::::::::#+ *         #.***=
                                     :#+:::::::#+ *
                                       .+::::##= #
                                        #++++++ =
                                          ####
'''

banner_12 = r'''
######*****************=================--==-----------=================*****************###########
####***************==============-----------------------------=============***************##########
##***************=========------------::::::::::::::::::::----------=============************#######
*************=========--------::::::::::::::::##*:::::::::::::::::-------==========*************####
**********==========------:::::::::::::.::::#*##****........:::::::::-------==========***********###
*********========------:::::::::..........######****=*...........:::::::::-----=========************
*******========------:::::::............#####*#***=====*  ............:::::::-----=========*********
*****=======--------:::::..............#######*##========       .........:::::::----=========*******
***========------:::::::..............#%%#####***=========         .........::::::-----======*******
**========-----:::::::..........  ....##########===========            .......::::::----=======*****
=========-----:::::::.........      .%#####**##**==========             ........:::::-----=======***
========----:::::::..........        ####*#***###======--===              ........:::::----=======**
======------::::::..........         %##**********=-------==                .......:::::-----======*
======-----::::::...........        #####%##%%%%##%%%%%###*==                 .......:::::----======
====------:::::::..........        .#%%%%%%%%%%%%%%%%%%#%%%%-*                 ......::::::----=====
====------:::::::.........         %%%%%-%%%%%%%%%%%%%%%%%%%%#                  .......:::::----====
====-----::::::::.......... .     #%%%%%##%%%%%%%%%%%%%%%%%%%%*                   ......:::::----===
===-----:::::::............        %#%%%%%%%%%%%%%%%%%%%%%%%%-%                    ......:::::----==
===------::::::.............. ..   ##%-%%%%%%%%%%%%%%%%%%%%%%-#                    ......::::::----=
===------::::::................. #-%##%%%%%%%%%%%%%%%%%%%%%%%%#*                   .......::::::---=
===------::::::..:...........#%%%%%-###%%%%%%%%%%%%%%%%%%%%%%#**#**                 ......::::::----
===-----:::::::...........#%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%#**#******              .......:::::----
===------:::::::........:%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%##************            ........:::-----
===------::::::::.......%%%%%%%%%%%%%%%-#%%%%%%%%%%%%%%-%##***#**********            ......::::::---
===------::::::::::.:::-%%%%%%%%%%%%%%%%%##%%%%%%%%%%%###****##******#***            ......::::::---
====------:::::::::::##-%%%%%%%%%%%---%-%%------%-%%%%%%%%--%%%%%%%%####%#*          .......:::::---
====------:::::::::::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#         .......:::::---
=====-------:::::::::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*       .........:::::---
=====-------::::::::%%-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=*      ........::::::---
======---------:::*###-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%****  .........::::::----
=======--------::-%-##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*****  ........:::::-----
'''



# banner_1 = choose_color(banner_1, "yellow")
# banner_2 = choose_color(banner_2, "green")
# banner_3 = choose_color(banner_3, "red")
# banner_4 = choose_color(banner_4, "cyan")
# banner_5 = choose_color(banner_5, "cyan")


# 随机图标
def picture_choice():
    i = random.choice(range(7))
    if i == 0:
        return banner_1
    elif i == 1:
        return banner_2
    elif i == 2:
        return banner_3
    elif i == 3:
        return banner_4
    elif i == 4:
        return banner_5
    elif i == 5:
        return banner_6
    elif i == 6:
        return banner_7
    elif i == 7:
        return banner_8

def banner():
    Author='\033[0;33m作者：w啥都学\033[0m'
    Blog='\033[0;33mBlog地址：www.zssnp.top\033[0m'
    github='\033[0;33mgithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\033[0m'
    gitee='\033[0;33mgitee项目地址：https://gitee.com/wZass/Full-Scanner\033[0m'
    Frame=f'\033[0;33m {"*"*60}\033[0m'
    picture_=choose_color_2(picture_choice())
    icon=f"""{Frame}\n{picture_}\n\n\n{Author}\n{Blog}\n{gitee}\n{github}\n{Frame}                              """
    return  icon

# 换行
class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
            # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

def help_h():
    parser = argparse.ArgumentParser(description='本程序是一个多功能工具、支持信息收集、爆破、漏洞扫描、常见的POC和EXP',
                                     usage=choose_color_2('python3 Full-Scanner.py [参数] [目标] [其他参数]'),
                                     formatter_class=SmartFormatter)
    # 选择模式
    Choose_cmdline=parser.add_argument_group(choose_color_2("选择模式"),
                                            "如果不喜欢输入命令那样、可以用下面的参数") # 子选项

    Choose_cmdline.add_argument("-G",action="store_true",
                                help="选择使用选择模式")



#被动信息收集
    parser.add_argument_group(UseStyle("[1][*]被动信息收集",fore='green'),
                                            "下面是常见的被动信息收集方法会利用各大搜索引擎") # 子选项
    # Passive_collect_message.add_argument("-passive",
    #                                     help="被动信息收集、会利用fofa,shodan进行信息收集",
    #                                     action="store_true")

    # fofa子域名探测
    Fofa_Passive_collect_message=parser.add_argument_group(UseStyle("[1]被动信息收集：[1]fofa搜索结果提取",fore='green'))
    Fofa_Passive_collect_message.add_argument("-fofa",
                                              metavar='IP/域名',
                                              dest='fofa',
                                              type=str,
                                              nargs='?',
                                              help="fofa搜索结果提取")

    Fofa_Passive_collect_message.add_argument("-Cookie",
                                              metavar='Cookie值',
                                              dest='cookie',
                                              type=str,
                                              nargs='?',
                                              help="Cookie需要验证、如果不想每次都指定可以去config.py文件里面添加",)

    # shodan信息收集
    Shodan_Passive_collect_message = parser.add_argument_group(UseStyle("[1]被动信息收集：[2]shodan信息收集", fore='green'))
    Shodan_Passive_collect_message.add_argument("-shodan",
                                                 metavar='[IP]',
                                                 dest='shodan',
                                                 type=str,
                                                 nargs='?',
                                                 help="shodan信息收集")
    Shodan_Passive_collect_message.add_argument("-api",
                                                 metavar='api值',
                                                 dest='api',
                                                 type=str,
                                                 nargs='?',
                                                 help="用-API参数指定、如果不想每次都指定可以去config.py文件里面添加")


    # whois查询
    whois_Passive_collect_message = parser.add_argument_group(UseStyle("[1]被动信息收集：[3]whois查询", fore='green'))
    whois_Passive_collect_message.add_argument("-whois",
                                            metavar='域名',
                                            dest='whois',
                                            type=str,
                                            nargs='?',
                                            help="whois查询、咧-whois https://www.baidu.com/")
    # bing爬取
    SE_collect_message = parser.add_argument_group(UseStyle("[1]被动信息收集：[4]搜索引擎爬虫", fore='green'),
                                                                   "下面这个会用一下搜索引擎进行搜索提取搜索的URL")
    SE_collect_message.add_argument("-bing",
                                   metavar='查询语句',
                                   dest='bing',
                                   type=str,
                                   nargs='?',
                                   help="""搜索引擎爬虫、咧 -bing 'intitle:后台登陆 "学院"' """)

    SE_collect_message.add_argument("-bingm",
                                   metavar='提取的页数',
                                   dest='bingm',
                                   type=int,
                                   nargs='?',
                                   help="""提取的页数如果不指定默认就是100000、咧 -bingm 5 """)
    # bing爬取
    google_collect_message = parser.add_argument_group(UseStyle("[1]被动信息收集：[5]搜索引擎爬虫", fore='green'),
                                                                   "下面这个会用一下搜索引擎进行搜索提取搜索的URL")
    google_collect_message.add_argument("-google",
                                   metavar='查询语句',
                                   dest='google',
                                   type=str,
                                   nargs='?',
                                   help="""搜索引擎爬虫、咧 -google 'intitle:后台登陆 "学院"' """)

    google_collect_message.add_argument("-googlem",
                                   metavar='提取的页数',
                                   dest='googlem',
                                   type=int,
                                   nargs='?',
                                   help="""提取的页数如果不指定默认就是100000、咧 -google 5 """)
    google_collect_message.add_argument("-googlep",
                                   metavar='代理地址',
                                   dest='googlep',
                                   type=str,
                                   nargs='?',
                                   help="""设置代理、咧 -googlep 127.0.0.1:8080 """)

    # bing爬取
    SubDNS_collect_message = parser.add_argument_group(UseStyle("[1]被动信息收集：[6]子域名查询", fore='green'),
                                                                   "这个采用的一些搜索引擎进行域名探测有bing、crtsh、fofa、censys等、不需要输入API这个是采集的查询结果的页面进行提取的")
    SubDNS_collect_message.add_argument("-SubDNS",
                                   metavar='域名',
                                   dest='SubDNS',
                                   type=str,
                                   nargs='?',
                                   help="""子域名查询""")

    # 主动信息收集
    parser.add_argument_group(UseStyle("[2][*]主动信息收集",fore="yellow"),
                                            "下面是常见的主动信息收集方法")

    # 目标cms识别
    Cms_Active_collect_message=parser.add_argument_group(UseStyle("[2]主动信息收集：[1]目标cms识别",fore="yellow"))
    Cms_Active_collect_message.add_argument("-cms",
                                            metavar='URL',
                                            dest='cms',
                                            type=str,
                                            nargs='?',
                                            help="目标cms识别")
    # 备份文件扫描
    Backup_Active_collect_message=parser.add_argument_group(UseStyle("[2]主动信息收集：[2]备份文件扫描",fore="yellow"))

    Backup_Active_collect_message.add_argument("-PB",
                                                metavar='URL',
                                                type=str,
                                                nargs='?',
                                                help="""备份文件扫描 指定扫描的目标、比如 -PB https://baidu.com/""")
    Backup_Active_collect_message.add_argument('-PBm',
                                                dest='PBm',
                                                metavar='文件名',
                                                type=str,
                                                nargs='?',
                                                help="多个目标保存到一个文件里面进行批量扫描")
    Backup_Active_collect_message.add_argument('-PBt',
                                                dest='PBt',
                                                metavar='线程数',
                                                type=int,
                                                nargs='?',
                                                help="指定线程默认是1")
    Backup_Active_collect_message.add_argument('-PBd',
                                              dest='PBd',
                                              metavar='字典文件',
                                              type=str,
                                              nargs='?',
                                              help="指定字典默认是自己生成")
    Backup_Active_collect_message.add_argument('-PBp',
                                              dest='PBp',
                                              metavar='代理地址',
                                              type=str,
                                              nargs='?',
                                              help="可选代理地址")





    # 后台扫描
    Back_Active_collect_message = parser.add_argument_group(UseStyle("[2]主动信息收集：[3]后台扫描", fore="yellow"))
    Back_Active_collect_message.add_argument("-BK",
                                            metavar='URL',
                                            dest='BK',
                                            type=str,
                                            nargs='?',
                                            help="后台扫描、指定扫描的目标、比如 -BK https://baidu.com/")
    Back_Active_collect_message.add_argument('-BKm',
                                            metavar='文件名',
                                            dest='BKm',
                                            type=str,
                                            nargs='?',
                                            help="多个目标保存到一个文件里面进行批量扫描")


    Back_Active_collect_message.add_argument('-BKd',
                                        dest='BKd',
                                        metavar='字典文件',
                                        type=str,
                                        nargs='?',
                                        help="指定字典默认是用的php.txt")

    Back_Active_collect_message.add_argument('-BKt',
                                        dest='BKt',
                                        metavar='线程数',
                                        type=int,
                                        nargs='?',
                                        help="指定线程默认是30")
    Back_Active_collect_message.add_argument('-BKp',
                                        dest='BKp',
                                        metavar='代理地址',
                                        type=str,
                                        nargs='?',
                                        help="可选设置代理")

    # 端口扫描

    C_segment_query_Active_collect_message = parser.add_argument_group(UseStyle("[2]主动信息收集：[5]C段查询", fore="yellow"))
    C_segment_query_Active_collect_message.add_argument("-CPS",
                                            metavar='IP',
                                            dest='CPS',
                                            type=str,
                                            nargs='?',
                                            help="端口扫描、比如 -PS 1.1.1.1")
    C_segment_query_Active_collect_message.add_argument('-CPSp',
                                            metavar='指定端口',
                                            dest='CPSp',
                                            type=str,
                                            nargs='?',
                                            help="指定端口、不指定默认常见的端口、指定比如-PSp 1-65535或者22,80,3306")
    C_segment_query_Active_collect_message.add_argument('-CPSt',
                                            metavar='线程数',
                                            dest='CPSt',
                                            type=int,
                                            nargs='?',
                                            help="指定线程、线程太多会出问题")
    # 端口扫描

    Port_Active_collect_message = parser.add_argument_group(UseStyle("[2]主动信息收集：[4]端口扫描", fore="yellow"))
    Port_Active_collect_message.add_argument("-PS",
                                            metavar='IP',
                                            dest='PS',
                                            type=str,
                                            nargs='?',
                                            help="端口扫描、比如 -PS 1.1.1.1")
    Port_Active_collect_message.add_argument('-PSp',
                                            metavar='指定端口',
                                            dest='PSp',
                                            type=str,
                                            nargs='?',
                                            help="指定端口、不指定默认常见的端口、指定比如-PSp 1-65535或者22,80,3306")
    Port_Active_collect_message.add_argument('-PSt',
                                            metavar='线程数',
                                            dest='PSt',
                                            type=int,
                                            nargs='?',
                                            help="指定线程、线程太多会出问题")


    # Active_collect_message.add_argument("-pC",
    #                                     help="C段扫描 演示 -pC 1.1.1.1-255:80:8888或1.1.1.1/24-255:80:8888",
    #                                     default=False)
    #
    # # Active_collect_message.add_argument("-WAF", help="WAF识别",
    # #                                     action="store_true")
    #
    #

    #
    # # CDN识别
    # CDN_Identify=parser.add_argument_group(choose_color_2("CDN识别"),
    #                                        "下面是常见的CDN识别的方法")
    # CDN_Identify.add_argument("-PING",
    #                           help="超级PING",
    #                           action="store_true",
    #                           default=0)
# 爆破
    parser.add_argument_group(UseStyle("[3][*]爆破",fore="blue"),
                                        "下面是常见、web爆破、和服务的爆破")

    # 网页
    Crack_Blasting=parser.add_argument_group(UseStyle("[3]爆破：[1]网页登录界面自动化破解",fore="blue"))
    Crack_Blasting.add_argument("-crack",
                                metavar='URL',
                                dest='crack',
                                type=str,
                                nargs='?',
                                help="登录界面自动化破解、比如-crack https://xxx.com/admin.php")

    # ftp
    Ftp_Crack_Blasting = parser.add_argument_group(UseStyle("[3]爆破：[2]ftp爆破", fore="blue"))
    Ftp_Crack_Blasting.add_argument("-ftp",
                                    metavar='目标地址',
                                    dest='ftp',
                                    type=str,
                                    nargs='?',
                                    help="ftp爆破、比如-ftp 1.1.1.1")
    Ftp_Crack_Blasting.add_argument("-ftpp",
                                    metavar='指定端口号',
                                    dest='ftpp',
                                    type=str,
                                    nargs='?',
                                    help="指定端口")
    Ftp_Crack_Blasting.add_argument("-ftpt",
                                    metavar='线程数',
                                    dest='ftpt',
                                    type=int,
                                    nargs='?',
                                    help="指定线程")
    Ftp_Crack_Blasting.add_argument("-ftpadmin",
                                    metavar='文件名',
                                    dest='ftpadmin',
                                    type=str,
                                    nargs='?',
                                    help="指定用户字典、不指定使用默认")
    Ftp_Crack_Blasting.add_argument("-ftppasswd",
                                    metavar='文件名',
                                    dest='ftppasswd',
                                    type=str,
                                    nargs='?',
                                    help="指定密码字典、不指定使用默认")
    # ssh
    SSH_Crack_Blasting = parser.add_argument_group(UseStyle("[3]爆破：[3]SSH破解", fore="blue"))

    SSH_Crack_Blasting.add_argument('-ssh',
                                    metavar='目标地址',
                                    dest='ssh',
                                    type=str,
                                    nargs='?',
                                    help="ssh密码怕破解、比如 -ssh 1.1.1.1")
    SSH_Crack_Blasting.add_argument("-sshp",
                                    metavar='指定端口号',
                                    dest='sshp',
                                    type=str,
                                    nargs='?',
                                    help="指定端口、默认端口号22")
    SSH_Crack_Blasting.add_argument('-sshu',
                                    metavar='指定字典',
                                    dest='sshu',
                                    type=str,
                                    nargs='?',
                                    help="指定用户名字典、不指定使用默认字典")
    SSH_Crack_Blasting.add_argument('-sshd',
                                    metavar='指定字典',
                                    dest='sshd',
                                    type=str,
                                    nargs='?',
                                    help="指定密码字典、不指定使用默认字典")

    SSH_Crack_Blasting.add_argument('-ssht',
                                    dest='ssht',
                                    metavar='线程数',
                                    type=int,
                                    nargs='?',
                                    help="指定线程、线程太多会出问题、默认线程1")

# # 其他
    parser.add_argument_group(UseStyle("[*]其他：小工具", fore="blue"),"")
    portquery_Blasting = parser.add_argument_group(UseStyle("其他：端口查询对应的服务", fore="cyan"))
    portquery_Blasting.add_argument("-tcp",
                                    metavar='端口',
                                    dest='tcp',
                                    type=str,
                                    nargs='?',
                                    help="tcp查询")
    portquery_Blasting.add_argument("-udp",
                                    metavar='端口',
                                    dest='udp',
                                    type=str,
                                    nargs='?',
                                    help="udp查询")
    # # POC，EXP

    from PocAndExpScript.pecmdline import pecmdline
    parser=pecmdline.help_h(parser)

#     Other_Crack_Blasting = parser.add_argument_group(UseStyle("其他：[2]代理采集", fore="cyan"))
#     Other_Crack_Blasting.add_argument("-PSC",
#                                     metavar='指定采集域名',
#                                     dest='PSC',
#                                     type=str,
#                                     default=False,
#                                     nargs='?',
#                                     help="代理地址采集")
    # # 漏洞验证和利用
    # Vulnerability_Scan=parser.add_argument_group(choose_color_2("POC和EXP"))
    #
    # Vulnerability_Scan.add_argument("-SPOC",
    #                                 metavar='POC名字',
    #                                 help="搜索现有点POC", default="1")
    # Vulnerability_Scan.add_argument("-SEXP",
    #                                 metavar='POC名字',
    #                                 help="搜索现有点EXP", default="1")
    # Vulnerability_Scan.add_argument("-POC",
    #                                 help="指定POC",
    #                                 action="store_true")
    # Vulnerability_Scan.add_argument("-EXP", help="指定EXP",
    #                                 action="store_true", default="1")
    # Vulnerability_Scan.add_argument("-CPE", help="自动扫描CMS识别后利用CMS的POC和EXP",
    #                                 action="store_true", default="1")
    #
    # # # 其他参数
    # Choose=parser.add_argument_group(choose_color_2("其他参数"),
    #       "上面的参数有的可能会用到的") # 子选项
    # Choose.add_argument("-p",
    #                     help="指定端口、指定参数不添加参数默认扫描全端口",
    #                     default = False)
    # Choose.add_argument("-T",
    #                     help="设置速度/线程",
    #                     default = False)
    # Choose.add_argument("-Cookie",
    #                     help="Cookie需要验证,比如Fofa、如果不想每次都指定可以去config.py文件里面添加",
    #                     default = False)
    # Choose.add_argument("-API",
    #                     help="指定API、比如shodan就需要自己的API、如果不想每次都指定可以去config.py文件里面添加",
    #                     default = False)



    return parser.parse_args()


