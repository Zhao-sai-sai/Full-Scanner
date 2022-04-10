from blasting.ftp_blasting import ftp
from collect import shodan,fofa
from thirdparty.extracted import webcrack
from thirdparty.CmsVulScan import CmsVulScan


class whether():

    def ftp(self,Ftpcrack_Parameter,u,p=21,quantity=1):
        try:
            if Ftpcrack_Parameter==True:
                ftp.fill_in(ip=u,port=p,quantity=quantity)
        except Exception as bc:
            print("出差了看看是不是参数输入错误")
    def shodan(self,Shodan_Parameter,u,API):
        try:
            if Shodan_Parameter==True:
                shodan.shod(u, API)
        except Exception:
            print("出差了看看是不是参数输入错误")
    def webcrack_(self,Crack_Parameter,u):
        try:
            if Crack_Parameter==True:
                webcrack.Interface(u)
        except Exception:
            print("出差了看看是不是参数输入错误")
    def CmsVulScan_(self,Cms_Parameter,u):
        try:
            if Cms_Parameter==True:
                CmsVulScan.Interface(u)
        except Exception:
            print("出差了看看是不是参数输入错误")
    def fofa_(self,Fofa_Parameter,u,Cookie):
        try:
            if Fofa_Parameter==True:
                fofa.Interface(u,Cookie)
        except Exception:
            print("出差了看看是不是参数输入错误")
