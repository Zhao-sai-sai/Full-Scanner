import os
from lib.choose import choose_color_2
from thirdparty.extracted import webcrack
from lib.cmdline import picture
from lib.choose_model import Auxiliary
from lib.choose_model import Big_Category

# 爆破判断
def blasting_Options_Judge(Judge):
    Auxiliary.Sundries().total_tips() # 提示

    if Judge=='Q':
        os.system('cls' if os.name == 'nt' else 'clear')# 终端清空
        print("退出了")
        return
    if Judge=='q':
        Big_Category.Category()
    elif Judge=='1':
        url=input('请输入目标地址：')
        webcrack.Interface(url)

# 爆破
def blasting_Choose():
    Auxiliary.Sundries().total_tips() # 提示

    print("\t%s\n\t%s\n\t%s\n\t%s"%(choose_color_2('登录界面自动化破解:\t\t\t1'),
                                            choose_color_2('ftp爆破:\t\t\t\t2'),
                                            choose_color_2('返回上一层:\t\t\t\tq'),
                                            choose_color_2('退出:\t\t\t\t\tQ')))
    print(" %s" % (f'\033[0;33;40m{"—" * 60}\033[0m'))
    blasting_Options_Judge(input(" 请输入："))
