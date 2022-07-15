from collect.SubDnsDetect import bing,fofa,crt,censys
#from lib.choose import UseStyle # 设置颜色


def DNS_Interface(args):

    keywords="site:"+args.SubDNS

    Dns_List=[] # 统计
    # -----------------------------------------------------------------------------
    DNS_Bing=bing.DNS_Climb_bing(keywords) # bing搜索

    Dns_List+=DNS_Bing # 统计

    print('\n'.join(str(i.rstrip()) for i in DNS_Bing)) #一行循环输出搜索出来的结果

    # -----------------------------------------------------------------------------
    DNS_censys = censys.DNS_Climb_censys(args.SubDNS)  # censys证书探测

    diff_list = list(set(DNS_censys) - set(Dns_List))  # 用于检查没有出来的域名进行输出

    Dns_List += DNS_censys  # 统计

    print('\n'.join(str(i.rstrip()) for i in diff_list))  # 一行循环输出搜索出来的结果

    #-----------------------------------------------------------------------------
    DNS_crt=crt.DNS_Climb_Crt(args.SubDNS)  # crt证书探测

    diff_list = list(set(DNS_crt) - set(Dns_List))  # 用于检查没有出来的域名进行输出

    Dns_List += DNS_crt # 统计

    print('\n'.join(str(i.rstrip()) for i in diff_list))  # 一行循环输出搜索出来的结果

    # -----------------------------------------------------------------------------
    DNS_Fofa=fofa.Dns_Request(args.SubDNS) # fofa探测

    diff_list = list(set(DNS_Fofa) - set(Dns_List)) # 用于检查没有出来的域名进行输出

    Dns_List += diff_list  # 统计

    print('\n'.join(str(i.rstrip()) for i in diff_list))  # 一行循环输出搜索出来的结果
