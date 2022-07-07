import os
import math
import importlib
import re


# 导入到文件里面
class Retrofit():

    # storage.py修改
    def Searchresults(self,results_IP):
        Searchresults_document = open("PocAndExpScript/storage.py", 'a')  # 打开文件写的方式
        Searchresults_document.write((results_IP + '\n'))  # 写入
        Searchresults_document.close()  # 关闭文件

    # 添加pecmdline文件
    def generate_Construct(self,Construct):
        Searchresults_document = open(f"PocAndExpScript/pecmdline/pecmdline.py", 'a')  # 打开文件写的方式
        Searchresults_document.write((Construct + '\n'))  # 写入
        Searchresults_document.close()  # 关闭文件


    # 判断是否添加过POC/EXP
    def Has_it_been_added(self,results_IP):
        Record = []
        for i in open('PocAndExpScript/storage.txt'):
            Record.append(i.strip())
        if results_IP in Record:
            return False
        else:
            Searchresults_document = open("PocAndExpScript/storage.txt", 'a')  # 打开文件写的方式
            Searchresults_document.write((results_IP + '\n'))  # 写入
            Searchresults_document.close()  # 关闭文件
            return True

    # 删除文件里面的return parser
    def delete_return_parser(self):
        with open('PocAndExpScript/pecmdline/pecmdline.py', 'r') as fpr:
            content = fpr.read()
        content = content.replace('return parser', '')
        with open('PocAndExpScript/pecmdline/pecmdline.py', 'w') as fpw:
            fpw.write(content)

    # 检查generate文件夹有多少文件
    def listdir(self):
        listdir = os.listdir('PocAndExpScript/generate')
        listdir.remove('__init__.py')
        listdir.remove('__pycache__')
        return listdir

    # 添加if
    def Add_if(self,important):
        Add=0
        judge = (f'\n\n#{"*" * 60}\n'+f'    if ')
        for i in important:
            if Add==0:
                and_=f'args.{i}!=None'
                Add = 1
            else:
                and_=f' and args.{i}!=None'
            judge+=and_
        judge+=': # 判断是否存在'

        return judge

    # 构建函数的传的参数
    def build_parameters(self,Number_of_parameters):
        # 函数参数
        parameters = ''
        for i in Number_of_parameters:
            parameters += ('args.' + i + ',')
        return parameters

    # 构建# pecmdline添加基本比如：CVE201918370_Blasting = parser.add_argument_group(" POC/EXP：CVE-2019-18370","小米系列路由器远程任务执行（CVE-2019-18370，CVE-2019-18371）POC")
    def basic_addition(self,math):
        name = re.sub('-', '', math.he_lp['filename'])
        # 列
        # CVE201918370_Blasting = parser.add_argument_group(" POC/EXP：CVE-2019-18370","小米系列路由器远程任务执行（CVE-2019-18370，CVE-2019-18371）POC")
        library = f"""\n    {name}_Blasting = parser.add_argument_group(UseStyle(" {math.he_lp['filename']}",back='yellow'),"{math.he_lp['name']}")"""
        return library

    #
    def build_add_argument(self,filename,key,value):
        add = f"""\n    {filename}_Blasting.add_argument("-{filename + key}",
                    metavar='{value}',
                    dest='{filename + key}',
                    type=str,
                    nargs='?',
                    help="{value}")"""
        return add

    # 重置
    def reset(self,document,content):

        Searchresults_document = open(document, 'w')  # 打开文件写的方式
        Searchresults_document.write((content))  # 写入
        Searchresults_document.close()  # 关闭文件


# 初始化对象
Retrofit_save=Retrofit()



# pecmdline添加参数和函数
def Function_addition(math,research):

    # pecmdline添加基本比如：CVE201918370_Blasting = parser.add_argument_group(" POC/EXP：CVE-2019-18370","小米系列路由器远程任务执行（CVE-2019-18370，CVE-2019-18371）POC")
    library=Retrofit_save.basic_addition(math)

    Retrofit_save.generate_Construct(library)  # 添加pecmdline文件


    #--------添加参数-------------
    math_parameter = math
    # 添加参数
    filename = re.sub('-', '', math.he_lp['filename'])
    #name = re.sub('-', '', math.he_lp['name'])

    Number_of_parameters=[] # 函数的参数
    important=[]
    main=''
    for a,b in math_parameter.he_lp.items(): # 获取he_lp的键值对，a键b值

        # 过滤其他的没有用的参数比如poc的功能等
        if 'filename' == a or 'name'==a or 'filename'==a or 'main'==a or 'important'==a:
            pass
        else:
            add=Retrofit_save.build_add_argument(filename,a,b)
            Retrofit_save.generate_Construct(add) # 添加pecmdline文件
            Number_of_parameters.append(filename+a) # 函数的参数

        if 'important'==a:
            for i in b:
                important.append(filename+i)

        if 'main'==a:
            main=b# 函数名字

    #print(important)
# ++++++storage.py文件里面添加导入库和函数+++++++++++
    # 构建函数的传的参数
    parameters=Retrofit_save.build_parameters(Number_of_parameters)

    # 构建判断
    judge=Retrofit_save.Add_if(important)
    library=f'        from PocAndExpScript.generate import {research}'

    Retrofit_save.Searchresults(judge)

    Retrofit_save.Searchresults(library)  # 导入库
    # 调用其他文件的模块
    # research文件夹名字
    # main 函数
    # parameters 参数
    main=f"""        {research}.{main}({parameters})#{math_parameter.he_lp['name']}"""

    Retrofit_save.Searchresults(main)



# ++++++始终return parser保持在最后一行+++++++++++
    #删除文件里面的return parser
    Retrofit_save.delete_return_parser()

    # 添加文件里面的return parser
    parser="""
    return parser"""
    Retrofit_save.generate_Construct(parser)
# +++++++++++++++++++++++++++++++++++++++++++++


def Interface():
    listdir=Retrofit_save.listdir()# 检查generate文件夹有多少文件
    print(f"检查{str(len(listdir))}个POC/EXP")

    for i in listdir:
        print(f"{'*'*60}\n正在准备导入：[{i}]")
        remove_py = re.sub('.py', '', i) # 去掉.py
        math = importlib.import_module(f'PocAndExpScript.generate.{remove_py}') # 导入动态库

        # 判断是否添加过模块
        whether=Retrofit_save.Has_it_been_added(f'{remove_py}')

        if whether: # 没有添加过
            print(f"正在添加[{i}]")
            Function_addition(math,remove_py) # 添加
            print(f"导入成功[{i}]\n{'*'*60}")
        else:
            print(f"这个[{i}]漏洞验证脚本已经添加\n{'*'*60}")

        #print(math.he_lp)


# 重置
def default():
    default_pecmdline="""
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
    """

    default_storage="""
from lib.cmdline import cmdline  # 图标
#args= cmdline.help_h()
def whether(args):
    print()

    """

    # PocAndExpScript/
    # 修改文件内容
    pecmdline = f"PocAndExpScript/pecmdline/pecmdline.py"
    Retrofit_save.reset(pecmdline,default_pecmdline)
    print(f"{'*'*60}\n重置完成：{pecmdline}")

    storage_py=f"PocAndExpScript/storage.py"
    Retrofit_save.reset(storage_py,default_storage)
    print(f"重置完成：{storage_py}")

    storage_txt=f"PocAndExpScript/storage.txt"
    Retrofit_save.reset(storage_txt,'')

    print(f"重置完成：{storage_txt}\n{'*'*60}")
