#from collect.search_engine import main


#from lib.choose_model import Big_Category

# from Activelibrary.backgroundscan import mian




class whether():
    # # 选择使用选择模式
    # def G_(G):
    #     if G==True:
    #         Big_Category.Category()


    # 被动信息收集
    # fofa_
    def fofa_judge(self,Fofa_Parameter, Cookie):
        from collect import fofa
        try:
            if Fofa_Parameter != None:
                fofa.Interface(Fofa_Parameter, Cookie)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    # shodan搜索
    def shodan_judge(self,Shodan_Parameter, api):
        from collect import shodan
        try:
            if Shodan_Parameter != None:
                shodan.shod(Shodan_Parameter, api)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    # whois查询
    def whois_judge(self,whois_Parameter,args):
        from collect import req_whois
        try:
            if whois_Parameter != None:
                req_whois.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    # bing提取
    def google_judge(self,google_Parameter,args):
        from collect import bing
        if google_Parameter !=None:
            bing.Interface(args)

    def SubDNS_judge(self,SubDNS_Parameter,args):
        from collect.SubDnsDetect import SubDns
        if SubDNS_Parameter!=None:
            #print(SubDNS_Parameter)
            SubDns.DNS_Interface(args)

    # # 主动信息收集

    # cms识别
    def CmsVulScan_judge(self,Cms_Parameter):
        from thirdparty.CmsVulScan import CmsVulScan

        try:
            if Cms_Parameter!=None:
                CmsVulScan.Interface(Cms_Parameter)
        except Exception as bc:
                print("有错误！错误提示" + str(bc))

    # 备份文件扫描
    def BP_judge(self,BP,args):
        from Initiative.Backupfilescan import ProbeBackup
        try:
            if BP != None:
                ProbeBackup.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    # 后台扫描
    def BK_judge(self,BK,args):
        from Initiative.backgroundscan import back
        try:
            if BK != None:
                back.Interfacemian(args)
        except Exception as bc:
                print("有错误！错误提示" + str(bc))

    # 端口扫描
    def PS_judge(self,PS,args):
        from Initiative.portscan import port
        try:
            if PS != None:
                port.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))



    # 暴力破解
    # 登录界面爆破
    def webcrack_judge(self,Crack_Parameter):
        from thirdparty.extracted import webcrack

        try:
            if Crack_Parameter!=None:
                webcrack.Interface(Crack_Parameter)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))
    #
    #  Ftp爆破
    def ftp_judge(self,Ftpcrack_Parameter,args):
        from blasting.ftp_blasting import ftp
        try:
            if Ftpcrack_Parameter !=None:
                ftp.fill_in(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    #  ssh爆破
    def ssh_judge(self,ssh_crack,args):
        from blasting.ssh_blasting import ssh
        try:

            if ssh_crack !=None:
                #print(ssh_crack)
                ssh.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))