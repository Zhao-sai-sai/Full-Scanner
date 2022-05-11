import argparse
from lib.picture  import picture_choice
from lib.choose import choose_color_2


def banner():
    Author='\033[0;33m作者=·=w啥都学===\033[0m'
    Blog='\033[0;33m===Blog地址=.=www.zssnp.top\033[0m'
    github='\033[0;33mgithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\033[0m'
    gitee='\033[0;33mgitee项目地址：https://gitee.com/wZass/Full-Scanner\033[0m'
    Frame=f'\033[0;33m {"—"*60}\033[0m'
    picture_=choose_color_2(picture_choice())
    icon=f"""\n{Frame}\n{picture_}\n\n\n{Author}\n{Blog}\n{gitee}\n{github}\n{Frame}                              """
    return  icon

def help_h():
    parser = argparse.ArgumentParser(description='本程序是一个多功能工具，支持信息收集，漏洞扫描，常见的POC和EXP',usage=choose_color_2('python3 Full-Scanner.py [参数] [目标] [其他参数]'))
    # 选择模式
    Choose_cmdline=parser.add_argument_group(choose_color_2("选择模式"),
                                            "如果不喜欢输入命令那样，可以用下面的参数") # 子选项

    Choose_cmdline.add_argument("-G",action="store_true",
                                help="选择使用选择模式")



    #被动信息收集
    Passive_collect_message=parser.add_argument_group(choose_color_2("被动信息收集"),
                                                      "下面是常见的被动信息收集方法会利用各大搜索引擎") # 子选项
    # Passive_collect_message.add_argument("-passive",
    #                                     help="被动信息收集，会利用fofa,shodan进行信息收集",
    #                                     action="store_true")

    Passive_collect_message.add_argument("-fofa",
                                         metavar='[IP/域名]',
                                         help="fofa子域名探测     注意：用-Cookie参数指定Cookie或者去config文件添加",
                                         default=False)

    Passive_collect_message.add_argument("-shodan",
                                         metavar='[IP]',
                                         help="shodan信息收集     注意：用-API参数指定自己的API或者去config文件添加",
                                         default=False)

    # Passive_collect_message.add_argument("-son",
    #                                      help="被动子域名探测，会结合搜索引擎进行探测",
    #                                      default=False)


    # 主动信息收集
    Active_collect_message=parser.add_argument_group(choose_color_2("主动信息收集"),
                                                      "下面是常见的主动信息收集方法")
    Active_collect_message.add_argument("-cms",
                                        metavar='[URL]',
                                        default=False,
                                        help="目标cms识别")

    Active_collect_message.add_argument("-pC",
                                        help="C段扫描 演示 -pC 1.1.1.1-255:80:8888或1.1.1.1/24-255:80:8888",
                                        default=False)

    # Active_collect_message.add_argument("-WAF", help="WAF识别",
    #                                     action="store_true")


    # 备份文件扫描
    Active_collect_message.add_argument("-c",
                                        metavar='[URL]',
                                        default=False,
                                        help="后台扫描 注意：-T 可以指定线程默认是30")
    ProbeBackup=parser.add_argument_group(choose_color_2(" 备份文件扫描"),
                                            "备份文扫描详细参数")
    ProbeBackup.add_argument("-b",
                            metavar='[URL]',
                            default=False,
                            help="""备份文件扫描 指定扫描的目标，比如https://baidu.com/""")
    ProbeBackup.add_argument('-many',
                            dest='many',
                            type=str,
                            nargs='?',
                            help="多个目标保存到一个文件里面进行批量扫描")
    ProbeBackup.add_argument('-thread',
                            dest='thread',
                            type=int,
                            nargs='?',
                            help="指定线程默认是1")
    ProbeBackup.add_argument('-document',
                              dest='document',
                              type=str,
                              nargs='?',
                              help="指定字典默认是自己生成")
    ProbeBackup.add_argument('-save',
                            dest='save',
                            type=str,
                            nargs='?',
                            help="扫描出来的结果保存到位置")

    # CDN识别
    CDN_Identify=parser.add_argument_group(choose_color_2("CDN识别"),
                                           "下面是常见的CDN识别的方法")
    CDN_Identify.add_argument("-PING",
                              help="超级PING",
                              action="store_true",
                              default=0)

    # 爆破
    Blasting=parser.add_argument_group(choose_color_2("爆破"),
                                        "下面是常见，web爆破，和服务的爆破")

    Blasting.add_argument("-crack",
                          help="登录界面自动化破解",
                          default=False)

    Blasting.add_argument("-ftp",
                          help="ftp爆破,可以用-p指定端口,-T指定线程",
                          default=False)

    # 漏洞验证和利用
    Vulnerability_Scan=parser.add_argument_group(choose_color_2("POC和EXP"))

    Vulnerability_Scan.add_argument("-SPOC",
                                    metavar='POC名字',
                                    help="搜索现有点POC", default="1")
    Vulnerability_Scan.add_argument("-SEXP",
                                    metavar='POC名字',
                                    help="搜索现有点EXP", default="1")
    Vulnerability_Scan.add_argument("-POC",
                                    help="指定POC",
                                    action="store_true")
    Vulnerability_Scan.add_argument("-EXP", help="指定EXP",
                                    action="store_true", default="1")
    Vulnerability_Scan.add_argument("-CPE", help="自动扫描CMS识别后利用CMS的POC和EXP",
                                    action="store_true", default="1")

    # # 其他参数
    Choose=parser.add_argument_group(choose_color_2("其他参数"),
          "上面的参数有的可能会用到的") # 子选项
    Choose.add_argument("-p",
                        help="指定端口，指定参数不添加参数默认扫描全端口",
                        default = False)
    Choose.add_argument("-T",
                        help="设置速度/线程",
                        default = False)
    Choose.add_argument("-Cookie",
                        help="Cookie需要验证,比如Fofa，如果不想每次都指定可以去config.py文件里面添加",
                        default = False)
    Choose.add_argument("-API",
                        help="指定API，比如shodan就需要自己的API，如果不想每次都指定可以去config.py文件里面添加",
                        default = False)



    return parser.parse_args()