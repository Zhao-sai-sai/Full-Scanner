import os
from lib.cmdline import picture
from lib.choose import choose_color_2

# 终端清空
def Terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Sundries():


    def __init__(self):
        self.hint=' \033[0;31;40m选择你想要的操作：\n\t使用说明想干什么输入对应的数字就可以了\n\n \033[0m'+f'\033[0;33;40m{"—" * 60}\033[0m'

    def total_tips(self):
        Terminal_clear() # 终端清空
        print(picture())  # 图标
        print(self.hint)
