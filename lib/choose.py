import random
STYLE = {
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },

        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },

        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },

        'default' :
        {
            'end' : 0,
        },
}
# 里面有4个参数第一个是字，mode是显示模式，fore是前景色，back背景
def UseStyle(string, mode = '', fore = '', back = ''):

    mode  = '%s' % STYLE['mode'][mode] if STYLE['mode'].__contains__(mode) else ''

    fore  = '%s' % STYLE['fore'][fore] if STYLE['fore'].__contains__(fore) else ''

    back  = '%s' % STYLE['back'][back] if STYLE['back'].__contains__(back) else ''

    style = ';'.join([s for s in [mode, fore, back] if s])

    style = '\033[%sm' % style if style else ''

    end   = '\033[%sm' % STYLE['default']['end'] if style else ''

    return '%s%s%s' % (style, string, end)


# def choose_color(banner,cb):
#     if cb == "green":
#         return "\033[0;31;40m{}\033[0m".format(banner)
#     elif cb == "red":
#         return "\033[0;31;40m{}\033[0m".format(banner)
#     elif cb == "yellow":
#         return "\033[0;33;40m{}\033[0m".format(banner)
#     elif cb == "cyan":
#         return "\033[0;36;40m{}\033[0m".format(banner)


def choose_color_2(cb):
    i = random.choice(range(4))
    if i == 0:
        return "\033[1;32m{}\033[0m".format(cb)
    elif i == 1:
        return "\033[1;31m{}\033[0m".format(cb)
    elif i == 2:
        return "\033[1;33m{}\033[0m".format(cb)
    elif i == 3:
        return "\033[1;36m{}\033[0m".format(cb)

