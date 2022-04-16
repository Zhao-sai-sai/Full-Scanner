from lib.choose import choose_color_2
from thirdparty.extracted import webcrack
from lib import Auxiliary
from lib.choose_model import Big_Category
from blasting.ftp_blasting import ftp
from rich.console import Console
from rich.table import Table
from rich import box

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
        print(choose_color_2("当前使用的是登录界面的爆破"))
        url=input(choose_color_2('请输入目标地址：'))
        webcrack.Interface(url)
    elif Judge=='2':
        print(choose_color_2("当前使用的是ftp爆破"))
        host=input(choose_color_2('请输入目标地址：'))
        p=input(choose_color_2('请输入目标端口(直接回车默认21)：'))
        quantity=input(choose_color_2('请输入线程数(直接回车默认1)：'))
        ftp.fill_in(ip=host,port=p,quantity=quantity)

# 爆破
def blasting_Choose():
    Auxiliary.Sundries().total_tips() # 提示

    table = Table(title="暴力破解", box=box.HORIZONTALS, style="yellow")

    table.add_column("序列", justify="right", style="green", min_width=3, no_wrap=True)
    table.add_column("名字", style="blue", min_width=51, justify="right")


    table.add_row("|1|", "登录界面自动化破解")
    table.add_row("|2|", "ftp爆破")
    table.add_row("|q|", "返回上一层")
    table.add_row("|Q|", "退出")

    console = Console()
    console.print(table)
    blasting_Options_Judge(input(" 选择 > "))
