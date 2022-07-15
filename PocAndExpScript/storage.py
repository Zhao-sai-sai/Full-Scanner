
from lib.cmdline import cmdline  # 图标
#args= cmdline.help_h()
def whether(args):
    print()

    

#************************************************************
    if args.CVE202226134u!=None: # 判断是否存在
        from PocAndExpScript.generate import CVE_2022_26134
        CVE_2022_26134.main(args.CVE202226134u,)#CVE-2022-26134Confluence远程命令执行漏洞
