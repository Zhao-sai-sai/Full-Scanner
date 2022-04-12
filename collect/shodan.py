import shodan
from conf import config
from lib.choose import choose_color_2,UseStyle
from lib.choose_model.Auxiliary import Sundries

# API
def shodan_API():
    i = str(input("请输入"))
    # 输入API
    Shodan_api = 0
    if i == '1':
        API_document = open("API.txt", 'r')  # 读文件
        Shodan_api = API_document.readline()  # 读取文件的API

        API_document.close()  # 关闭文件
    else:
        Shodan_api = input("请输入自己的shodan的API：")
        API_document = open("API.txt", 'w')
        API_document.write(Shodan_api)
        API_document.close()
        api = shodan.Shodan(Shodan_api)

    print('''
             _               _
         ___| |__   ___   __| | __ _ _ __
        / __| '_ \ / _ \ / _` |/ _` | '_ \
        \__ \ | | | (_) | (_| | (_| | | | |
        |___/_| |_|\___/ \__,_|\__,_|_| |_|
    
        * 信息收集
        * 1. 输入用第一次的API
         ''')

    # api = shodan_API()
    host = str(input("请输入目标地址："))
    return api


def shod(host,Shodan_api):
    print(Shodan_api)
    try:
        if Shodan_api==None or Shodan_api=='': # 查看你的PCT是否输入参数,没有输入执行
            print(choose_color_2("当前你使用的是默认config配置文件的API[*]内容：")+str(config.SeriousConfig['shodan']))

            Shodan_api=config.SeriousConfig['shodan']
        else:
            print(choose_color_2("你手动指定的API[*]内容：")+str(Shodan_api))

        print("IP地址是："+UseStyle(host,mode='underline'))# 输出显示样式
        print(Sundries().Wire_)
        api = shodan.Shodan(Shodan_api)

        resultip = api.host(host)


        for result in resultip['data']:
            print(choose_color_2("放的端口：" + str(result['port']) + "\n使用的服务器软件：" + result['product'] + '\n响应信息：' + str(
                result['data']) + '\n爬曲时间：' + result['timestamp'] + "\n国家是：" + resultip['country_name']))
        print()
    except Exception as bc:
        print("有错误！\n错误提示"+str(bc))