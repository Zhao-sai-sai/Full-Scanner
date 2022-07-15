
import argparse
from lib.choose import UseStyle # 指定颜色

def help_h(parser):

    # 选择模式
    PE_Blasting = parser.add_argument_group(UseStyle("添加POCEXP或者自己的脚步",back='yellow'))
    PE_Blasting.add_argument("-PE",
                            dest='PE',
                            type=str,
                            default=False,
                            nargs='?',
                            help="使用POC/EXP")

    PE_Blasting.add_argument("-refresh",
                            dest='refresh',
                            type=str,
                            default=False,
                            nargs='?',
                            help="刷新添加POC/EXP")
    PE_Blasting.add_argument("-reset",
                            dest='reset',
                            type=str,
                            default=False,
                            nargs='?',
                            help="重置POC/EXP")
    return parser
    