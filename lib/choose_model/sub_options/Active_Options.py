from lib import Auxiliary
from lib.choose_model import Big_Category
from lib.choose import choose_color_2
from Activelibrary.backgroundscan import mian
from rich.console import Console
from rich.table import Table
from rich import box
from thirdparty.CmsVulScan import CmsVulScan
from lib.choose import UseStyle

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
        url=input(choose_color_2('请输入目标地址> '))
        CmsVulScan.Interface(url)
    elif Judge=='4':
        url=input(choose_color_2('请输入目标地址> '))
        T = input(UseStyle('请输入请求线程(默认线程30)：', fore='green'))
        mian.Interface(url,T)


# 被动信息收集选择
def Active_Information_Gathering():

    Auxiliary.Sundries().total_tips() # 提示

    table = Table(title="主动信息收集", box=box.HORIZONTALS, style="yellow")

    table.add_column("序列", justify="right", style="green", min_width=3, no_wrap=True)
    table.add_column("名字", style="blue", min_width=51, justify="right")


    table.add_row("|1|", "目标cms识别")
    table.add_row("|2|", "C段扫描")
    table.add_row("|3|", "WAF识别")
    table.add_row("|4|", "后台扫描")
    table.add_row("|q|", "返回上一层")
    table.add_row("|Q|", "退出")

    console = Console()
    console.print(table)

    Active_Options_Judge(input(" 选择 > "))