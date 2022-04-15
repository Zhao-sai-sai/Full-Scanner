from lib.choose_model import Auxiliary
from lib.choose_model import Big_Category
from lib.choose import choose_color_2
from Activelibrary.backgroundscan import mian


# 被动信息判断
def Active_Options_Judge(Judge):
    Auxiliary.Sundries().total_tips() # 提示

    if Judge=='Q':
        Auxiliary.Terminal_clear()  # 终端清空
        print("退出了")
        return
    if Judge=='q':
        Big_Category.Category()
    elif Judge=='1':
        url=input(choose_color_2('请输入目标地址：'))
        Cookie = input(choose_color_2('请输入请求线程：'))
        mian.Interface(url,Cookie)
    elif Judge=='4':
        url=input(choose_color_2('请输入目标地址：'))
        mian.Interface(url)


# 被动信息收集选择
def Active_Information_Gathering():

    Auxiliary.Sundries().total_tips() # 提示

    print("%s\n%s\n%s\n%s\n%s\n%s"%(choose_color_2('目标cms识别:\t\t\t\t|1|'.center(36, '*')),
                            choose_color_2('C段扫描:\t\t\t\t|2|'.center(35, '*')),
                            choose_color_2('WAF识别:\t\t\t\t|3|'.center(34, '*')),
                            choose_color_2('后台扫描:\t\t\t\t|4|'.center(34, '*')),
                            choose_color_2('返回上一层:\t\t\t\t|q|'.center(34, '*')),
                            choose_color_2('退出:\t\t\t\t|Q|'.center(32, '*'))))
    print(" %s" % (f'\033[0;33;40m{"—" * 60}\033[0m'))
    Active_Options_Judge(input(choose_color_2(" 请输入：")))