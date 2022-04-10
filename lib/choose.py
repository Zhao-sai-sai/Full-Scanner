import random

def choose_color(banner,cb):
    if cb == "green":
        return "\033[0;31;40m{}\033[0m".format(banner)
    elif cb == "red":
        return "\033[0;31;40m{}\033[0m".format(banner)
    elif cb == "yellow":
        return "\033[0;33;40m{}\033[0m".format(banner)
    elif cb == "cyan":
        return "\033[0;36;40m{}\033[0m".format(banner)


def choose_color_2(cb):
    i = random.choice(range(4))
    if i == 0:
        return "\033[1;32;40m{}\033[0m".format(cb)
    elif i == 1:
        return "\033[1;31;40m{}\033[0m".format(cb)
    elif i == 2:
        return "\033[1;33;40m{}\033[0m".format(cb)
    elif i == 3:
        return "\033[1;36;40m{}\033[0m".format(cb)

