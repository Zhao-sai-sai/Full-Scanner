from collect import shodan,fofa
from lib.choose_model import Auxiliary
from lib.choose_model import Big_Category
from lib.choose import choose_color_2



# 被动信息判断
def Passive_Options_Judge(Judge):
    Auxiliary.Sundries().total_tips() # 提示

    if Judge=='Q':
        Auxiliary.Terminal_clear()  # 终端清空
        print("退出了")
        return
    if Judge=='q':
        Big_Category.Category()
    elif Judge=='1':
        url=input(choose_color_2('请输入目标地址：'))
        Cookie = input(choose_color_2('请输Cookie值：'))
        fofa.Interface(url,Cookie)
    elif Judge=='2':
        host=input(choose_color_2('请输入目标地址：'))
        API = input(choose_color_2('请输API(如果不输入直接回车默认使用配置config文件的)：'))
        shodan.shod(host,API)

# 被动信息收集选择
def Passive_Information_Gathering():

    Auxiliary.Sundries().total_tips() # 提示

    print("%s\n%s\n%s\n%s"%(choose_color_2('fofa子域名探测:\t\t\t|1|'.center(36, '*')),
                            choose_color_2('shodan信息收集:\t\t\t|2|'.center(36, '*')),
                            choose_color_2('返回上一层:\t\t\t\t|q|'.center(32, '*')),
                            choose_color_2('退出:\t\t\t\t|Q|'.center(31, '*'))))
    print(" %s" % (f'\033[0;33;40m{"—" * 60}\033[0m'))
    Passive_Options_Judge(input(choose_color_2(" 请输入：")))