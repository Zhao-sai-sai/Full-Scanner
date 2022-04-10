#!/usr/bin/env python

from lib import cmdline
import judge

if __name__ == '__main__':
    cmdline.picture()
    args= cmdline.help_h()
    judge=judge.whether()
# 爆破
    # ftp
    judge.ftp(args.ftpcrack,args.u,args.p,args.quantity)
    # 登录界面自动化破解
    judge.webcrack_(args.crack,args.u)

# 被动信息收集
    # shodan
    judge.shodan(args.shodan,args.u,args.PCT)

    # fofa

    judge.fofa_(args.fofa, args.u, args.PCT)

# 主动信息收集
    #cms探测
    judge.CmsVulScan_(args.cms,args.u)
