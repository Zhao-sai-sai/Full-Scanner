import os
from lib.cmdline import banner

# 终端清空
def Terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Sundries():


    def __init__(self):
        self.hint=' \033[0;31m选择你想要的操作：\n\t使用说明按照下面的输入就可以了\n\n \033[0m'+f'\033[0;33m{"—" * 60}\033[0m'
        self.Wire_=f'\033[0;33m {"—"*60}\033[0m'

    def Wire(self):
        return self.Wire_

    def total_tips(self):
        Terminal_clear() # 终端清空
        print(banner())  # 图标
        print(self.hint)
