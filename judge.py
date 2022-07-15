#from collect.search_engine import main


#from lib.choose_model import Big_Category

# from Activelibrary.backgroundscan import mian




class whether():
    # 选择使用选择模式
    def G_(self,G):
        if G==True:
            from lib.choose_model import Big_Category
            Big_Category.Category()

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
    # dns
    def SubDNS_judge(self,SubDNS_Parameter,args):
        from collect.SubDnsDetect import SubDns
        if SubDNS_Parameter!=None:
            #print(SubDNS_Parameter)
            SubDns.DNS_Interface(args)
    # Google
    def Google_judge(self,SubDNS_Parameter,args):

        if SubDNS_Parameter!=None:
            from collect import google
            #print(SubDNS_Parameter)
            google.Interface(args)
    # # 主动信息收集

    # cms识别
    def CmsVulScan_judge(self,Cms_Parameter):


        try:
            if Cms_Parameter!=None:
                from thirdparty.CmsVulScan import CmsVulScan
                CmsVulScan.Interface(Cms_Parameter)
        except Exception as bc:
                print("有错误！错误提示" + str(bc))

    # 备份文件扫描
    def BP_judge(self,BP,BPm,args):

        try:
            if BP != None: # 单个扫描
                from Initiative.Backupfilescan import ProbeBackup
                ProbeBackup.Interface(args)

            elif BPm!=None: # 批量扫描
                from Initiative.Backupfilescan import ProbeBackup
                ProbeBackup.Interface(args)

        except Exception as bc:
            print("有错误！错误提示" + str(bc))

    # 后台扫描
    def BK_judge(self,BK,BKm,args):

        # try:
        if BK != None:
            from Initiative.backgroundscan import back
            back.Interfacemian(args)
        elif BKm != None:  # 批量扫描
            from Initiative.backgroundscan import back
            back.Interfacemian(args)
        # except Exception as bc:
        #         print("有错误！错误提示" + str(bc))

    # 端口扫描
    def PS_judge(self,PS,args):

        try:
            if PS != None:
                from Initiative.portscan import port
                port.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))



    # 暴力破解
    # 登录界面爆破
    def webcrack_judge(self,Crack_Parameter):


        try:
            if Crack_Parameter!=None:
                from thirdparty.extracted import webcrack
                webcrack.Interface(Crack_Parameter)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))
    #
    #  Ftp爆破
    def ftp_judge(self,Ftpcrack_Parameter,args):

        #try:
        if Ftpcrack_Parameter !=None:
            from blasting.ftp_blasting import ftp
            ftp.fill_in(args)
        # except Exception as bc:
        #     print("有错误！错误提示" + str(bc))

    #  ssh爆破
    def ssh_judge(self,ssh_crack,args):

        try:

            if ssh_crack !=None:
                from blasting.ssh_blasting import ssh
                #print(ssh_crack)
                ssh.Interface(args)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))
    # # 其他
    # 端口对应服务查询
    def portquery_judge(self,Portquery_Parameter,args):
        if Portquery_Parameter!=None:
            from other.portquery import potrquery
            potrquery.Interfacemian(args)



    # def Acting_judge(self,PSC_Parameter):
    #     from other.acting import Agentmian
    #     if PSC_Parameter != False:
    #         print("dsads")


    # POC/EXP
    def PE_judge(self,PEP_Parameter,refresh_Paramete,reset_Paramete,args):


        if PEP_Parameter!=False: #使用POC/EXP
            from PocAndExpScript import storage # 调用
            storage.whether(args)

        elif refresh_Paramete!=False: # 更新POC/EXP
            from PocAndExpScript import main
            main.Interface()

        elif reset_Paramete!=False: # 重置
            from PocAndExpScript import main
            main.default()