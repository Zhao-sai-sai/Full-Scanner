from lib.choose import choose_color_2
from thirdparty.extracted import webcrack
from lib.choose_model import Auxiliary
from lib.choose_model import Big_Category
from blasting.ftp_blasting import ftp

# 爆破判断
def blasting_Options_Judge(Judge):
    Auxiliary.Sundries().total_tips() # 提示

    if Judge=='Q':
        Auxiliary.Terminal_clear()# 终端清空
        print("退出了")
        return
    if Judge=='q':
        Big_Category.Category()
    elif Judge=='1':
        print("当前使用的是登录界面的爆破")
        url=input('请输入目标地址：')
        webcrack.Interface(url)
    elif Judge=='2':
        print("当前使用的是ftp爆破")
        host=input('请输入目标地址：')
        p=input('请输入目标端口(直接回车默认21)：')
        quantity=input('请输入线程数(直接回车默认1)：')
        ftp.fill_in(ip=host,port=p,quantity=quantity)

# 爆破
def blasting_Choose():
    Auxiliary.Sundries().total_tips() # 提示

    print("%s\n%s\n%s\n%s"%(choose_color_2('登录界面自动化破解:\t\t\t|1|'.center(39, '*')),
                                            choose_color_2('ftp爆破:\t\t\t\t|2|'.center(35, '*')),
                                            choose_color_2('返回上一层:\t\t\t\t|q|'.center(35, '*')),
                                            choose_color_2('退出:\t\t\t\t|Q|'.center(33, '*'))))
    print(" %s" % (f'\033[0;33;40m{"—" * 60}\033[0m'))
    blasting_Options_Judge(input(" 请输入："))
