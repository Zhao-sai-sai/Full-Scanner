from lib import Auxiliary
from lib.choose_model.sub_options import blasting_Options
from lib.choose_model.sub_options import Passive_Options
from lib.choose_model.sub_options import Active_Options
from rich.console import Console
from rich.table import Table
from rich import box




# 判断大类输入的什么
def Category_Judge(Judge='No'):
    if Judge=='Q':
        Auxiliary.Terminal_clear() # 终端清空
        print("退出了")
        return
    elif Judge=='1':
        Passive_Options.Passive_Information_Gathering()
    elif Judge=='2':
        Active_Options.Active_Information_Gathering()
    elif Judge=='4':
        blasting_Options.blasting_Choose() # 进入爆破选项，blasting_Options在sub_options文件夹下

# 大类
def Category():
    Auxiliary.Sundries().total_tips() # 提示

    table = Table(title="渗透测试阶段", box=box.HORIZONTALS, style="yellow")

    table.add_column("序列", justify="right", style="blue", min_width=3, no_wrap=True)
    table.add_column("名字", style="green", min_width=51, justify="right")

    table.add_row("|1|", "被动信息收集")
    table.add_row("|2|", "主动信息收集")
    table.add_row("|4|", "暴力破解")
    table.add_row("|5|", "POC和EXP")
    table.add_row("|Q|", "退出")

    console = Console()
    console.print(table)

    Category_Judge(input(" 选择 > "))