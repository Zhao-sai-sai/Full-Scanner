from thirdparty.CmsVulScan.modules.function import col as color
import random

banner_1 = color(r""" 
""","yellow")
banner_2 = color(r'''
''',"green")


banner_3 = color(r'''
''',"red")



banner_4 = color(r'''
''',"cyan")


banner_5 = color(r'''
''',"cyan")



def banner():
    o_o = random.choice(range(5))
    if o_o == 0:
        return banner_1
    elif o_o == 1:
        return banner_2
    elif o_o == 2:
        return banner_3
    elif o_o == 3:
        return banner_4
    elif o_o == 4:
        return banner_5
