import argparse
from rich.console import Console
from rich.table import Table
from rich import box

def command(u):



    parser = argparse.ArgumentParser(description="CmsVulScan")
    parser.add_argument("-u", dest='url', help='指定url，如：http://www.baidu.com')
    parser.add_argument("-f", dest='file', help='批量扫描，指定文本文件，一行一个url', default=None)
    parser.add_argument("-p", dest='proxies', help='设置代理，格式：http://127.0.0.1:8080', default=None)
    parser.add_argument("-o", dest='save_path', help='指定保存路径', default=None)
    parser.add_argument("-t", dest='thread', help='指定线程，默认20',default=20)
    parser.add_argument("-out", dest='out', help='指定超时时间，默认20',default=20)
    parser.add_argument("-gen", dest='gen', help='重新生成payload文件',action="store_true")
    parser.add_argument("-URL", dest='URL', help='设定是否进行url模块扫描（误报率高，建议扫不出东西时开启）',action="store_true")


    table = Table(title="CMS识别项目地址：https://github.com/F6JO/CmsVulScan", box=box.HORIZONTALS, style="yellow")

    table.add_column("参数", justify="right", style="green", min_width=3, no_wrap=True)
    table.add_column("作用", style="blue", min_width=51, justify="right")


    table.add_row("-f","批量扫描，指定文本文件，一行一个url")
    table.add_row("-p", "设置代理，格式：http://127.0.0.1:8080")
    table.add_row("-o","指定保存路径")
    table.add_row("-t", "指定线程，默认20s")
    table.add_row("-out", "指定超时时间，默认20")
    table.add_row("-gen", "重新生成payload文件")
    table.add_row("-URL", "设定是否进行url模块扫描(误报率高，建议扫不出东西时开启)")

    console = Console()
    console.print(table)

    parameter=input("""  \033[0;31;40m比如：-o /a.txt         注意：不输入全部是默认\033[0m\n  \033[0;33;40m请输入：\033[0m""")

    if '-t' in parameter:
        return parser.parse_args(f'{parameter}'.split())
    else:
        return parser.parse_args(f'-u {u} {parameter}'.split())