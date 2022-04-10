import argparse
from lib.picture  import picture_choice
from lib.choose import choose_color_2






def picture():

    Author='\033[0;37;43m===作者=·=w啥都学===\033[0m'
    Blog='\033[0;37;43m===作者博客=.=www.zssnp.top===\033[0m'
    github='\033[0;37;43m===项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\033[0m'
    Frame=f'\033[0;33;40m {"—"*60}\033[0m'
    picture_=picture_choice()
    h='注意：输入-h/--help查看工具的使用'
    print(Frame)
    print(picture_)
    print(Author)
    print(Blog)
    print(f"""{Frame}
      {picture_}                    
      
                                        {Author}
                            {Blog}
    {github}
{Frame}    
                            {h}
""")

def help_h():
    parser = argparse.ArgumentParser(usage=choose_color_2('本程序是一个多功能工具，支持信息收集，漏洞扫描，常见的POC和EXP'))
    # 选择模式
    Choose_cmdline=parser.add_argument_group(choose_color_2("选择模式"),
          "如果不喜欢输入命令那样，可以用下面的参数") # 子选项

    Choose_cmdline.add_argument("-G", metavar='',
                        help="选择使用选择模式")


    # 目标指定
    Choose=parser.add_argument_group(choose_color_2("指定目标"),
          "指定目标的参数") # 子选项
    Choose.add_argument("-u", metavar='目标地址',
                        help="指定目标地址 比如 -u www.xxxx.com")
    Choose.add_argument("-p",metavar='端口',
    help="端口扫描，指定端口，指定参数不添加参数默认扫描全端口", default=0)
    Choose.add_argument("-quantity", help="设置速度默认是1",
                        metavar='速度', default=0)


    #被动信息收集
    Passive_collect_message=parser.add_argument_group(choose_color_2("被动信息收集"),
                                                      "下面是常见的被动信息收集方法会利用各大搜索引擎") # 子选项
    Passive_collect_message.add_argument("-passive",
                        help="被动信息收集，会利用fofa,shodan进行信息收集",
                        action="store_true", default=0)

    Passive_collect_message.add_argument("-fofa", help="fofa子域名探测，会利用fofa搜索",
                        action="store_true", default=0)

    Passive_collect_message.add_argument("-shodan", help="shodan信息收集，会利用shodan信息收集",
                        action="store_true")

    Passive_collect_message.add_argument("-son", help="被动子域名探测，会结合搜索引擎进行探测",
                        action="store_true", default=0)
    Passive_collect_message.add_argument("-PCT",
                        help="认证密钥或者Cookie，shodan和fofa都是需要的")

    # 主动信息收集
    Active_collect_message=parser.add_argument_group(choose_color_2("主动信息收集"),
                                                      "下面是常见的主动信息收集方法")
    Active_collect_message.add_argument("-cms",action="store_true",
                                        help="目标cms识别")

    Active_collect_message.add_argument("-pC",metavar='目标地址范围',
                                        help="C段扫描 演示 -pC 1.1.1.1-255:80:8888或1.1.1.1/24-255:80:8888", default="0")

    Active_collect_message.add_argument("-WAF", help="WAF识别",
                                        action="store_true", default=0)

    Active_collect_message.add_argument("-c", help="目录爬取 比如 -c /admin/",
                                        action="store_true",default=0)



    # CDN识别
    CDN_Identify=parser.add_argument_group(choose_color_2("CDN识别"),
                                           "下面是常见的CDN识别的方法")
    CDN_Identify.add_argument("-PING", help="超级PING",
                            action="store_true", default=0)

    # 爆破
    Blasting=parser.add_argument_group(choose_color_2("爆破"),
                                        "下面是常见，web爆破，和服务的爆破")

    Blasting.add_argument("-crack", help="登录界面自动化破解",
                         action="store_true")

    Blasting.add_argument("-ftpcrack", help="ftp爆破",
                        action="store_true")

    # 漏洞验证和利用
    Vulnerability_Scan=parser.add_argument_group(choose_color_2("POC和EXP"))

    Vulnerability_Scan.add_argument("-SPOC", metavar='POC名字',
                                    help="搜索现有点POC", default="1")
    Vulnerability_Scan.add_argument("-SEXP", metavar='POC名字',
                                    help="搜索现有点EXP", default="1")
    Vulnerability_Scan.add_argument("-POC", help="指定POC",
                                    action="store_true", default="1")
    Vulnerability_Scan.add_argument("-EXP", help="指定EXP",
                                    action="store_true", default="1")
    Vulnerability_Scan.add_argument("-CPE", help="自动扫描CMS识别后利用CMS的POC和EXP",
                                    action="store_true", default="1")
    return parser.parse_args()