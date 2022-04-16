#!/usr/bin/env python
'''
主程序

'''

h='\t\t\t  注意：输入-h/--help查看工具的使用\n'


from lib import cmdline
from lib.cmdline import banner
import judge


if __name__ == '__main__':
# 图标
    print(banner())
    args= cmdline.help_h()
    judge=judge.whether()
# 选择使用选择模式
    judge.G_(args.G)

# 被动信息收集
    # fofa
    judge.fofa_(args.fofa,args.Cookie)

    # shodan
    judge.shodan(args.shodan,args.API)

# 主动信息收集
    #cms探测
    judge.CmsVulScan_(args.cms)


    #后台扫描
    judge.c_(args.c,args.T)

# 爆破

    # 登录界面自动化破解
    judge.webcrack_(args.crack)

    # ftp
    judge.ftp(args.ftp,args.p,args.T)





