from lib.choose import choose_color_2
from lib.choose_model import Auxiliary
from lib.choose_model.sub_options import blasting_Options
from lib.choose_model.sub_options import Passive_Options
from lib.choose_model.Auxiliary import Sundries

# 判断大类输入的什么
def Category_Judge(Judge='No'):
    if Judge=='Q':
        Auxiliary.Terminal_clear() # 终端清空
        print("退出了")
        return
    elif Judge=='1':
        Passive_Options.Passive_Information_Gathering()
    elif Judge=='4':
        blasting_Options.blasting_Choose() # 进入爆破选项，blasting_Options在sub_options文件夹下

# 大类
def Category():
    Auxiliary.Sundries().total_tips() # 提示

    print("%s\n%s\n%s\n%s\n%s\n%s"%(choose_color_2('被动信息收集:\t\t\t|1|'.center(35, '*')),
                                                            choose_color_2('主动信息收集:\t\t\t|2|'.center(35, '*')),
                                                            choose_color_2('CDN识别:\t\t\t\t|3|'.center(35, '*')),
                                                            choose_color_2('爆破:\t\t\t\t|4|'.center(33, '*')),
                                                            choose_color_2('POC和EXP:\t\t\t\t|5|'.center(36, '*')),
                                                            choose_color_2('退出:\t\t\t\t|Q|'.center(33, '*'))))
    print(Sundries().Wire_)
    Category_Judge(input(" 请输入："))