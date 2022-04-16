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


# 被动信息收集
    # fofa_
    def fofa_(self, Fofa_Parameter, Cookie):
        try:
            if Fofa_Parameter != False:
                fofa.Interface(Fofa_Parameter, Cookie)
        except Exception:
            print("出差了看看是不是参数输入错误")

    # shodan搜索
    def shodan(self, Shodan_Parameter, API):
        try:
            if Shodan_Parameter != False:
                shodan.shod(Shodan_Parameter, API)
        except Exception as bc:
            print("有错误！错误提示" + str(bc))
# 主动信息收集

    # cms识别
    def CmsVulScan_(self,Cms_Parameter):
        try:
            if Cms_Parameter!=False:
                CmsVulScan.Interface(Cms_Parameter)
        except Exception:
            print("出差了看看是不是参数输入错误")

    # 后台扫描
    def c_(self, c,T):
        try:
            if c != False:
                mian.Interface(c,T)
        except Exception:
            print("出差了看看是不是参数输入错误")
# 暴力破解

    # 登录界面爆破
    def webcrack_(self,Crack_Parameter):
        try:
            if Crack_Parameter!=False:
                webcrack.Interface(Crack_Parameter)
        except Exception:
            print("出差了看看是不是参数输入错误")

    #  Ftp爆破
    def ftp(self,Ftpcrack_Parameter,p,quantity):
        try:
            if Ftpcrack_Parameter !=False:
                ftp.fill_in(ip=Ftpcrack_Parameter,port=p,quantity=quantity)
        except Exception:
            print("出差了看看是不是参数输入错误")



