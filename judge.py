from blasting.ftp_blasting import ftp
from collect import shodan,fofa
from thirdparty.extracted import webcrack
from thirdparty.CmsVulScan import CmsVulScan
from lib.choose_model import Big_Category
from Activelibrary.backgroundscan import mian


class whether():

# 选择使用选择模式
    def G_(self,G):
        if G==True:
            Big_Category.Category()

#  Ftp爆破
    def ftp(self,Ftpcrack_Parameter,u,p=21,quantity=1):
        try:
            if Ftpcrack_Parameter==True:
                ftp.fill_in(ip=u,port=p,quantity=quantity)
        except Exception as bc:
            print("出差了看看是不是参数输入错误")
# shodan搜索
    def shodan(self,Shodan_Parameter,u,API):
        try:
            if Shodan_Parameter==True:
                shodan.shod(u,API)
        except Exception as bc:
            print("有错误！错误提示"+str(bc))
# 登录界面爆破
    def webcrack_(self,Crack_Parameter,u):
        try:
            if Crack_Parameter==True:
                webcrack.Interface(u)
        except Exception:
            print("出差了看看是不是参数输入错误")
# cms识别
    def CmsVulScan_(self,Cms_Parameter,u):
        try:
            if Cms_Parameter==True:
                CmsVulScan.Interface(u)
        except Exception:
            print("出差了看看是不是参数输入错误")
# fofa_
    def fofa_(self,Fofa_Parameter,u,Cookie):
        try:
            if Fofa_Parameter==True:
                fofa.Interface(u,Cookie)
        except Exception:
            print("出差了看看是不是参数输入错误")
# 后台扫描
    def c_(self,c,u):
        try:
            if c == True:
                mian.Interface(u)
        except Exception:
            print("出差了看看是不是参数输入错误")

