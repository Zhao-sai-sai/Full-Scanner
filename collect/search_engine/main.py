from collect.search_engine import bing



def Interface(args):
    print(args.SEbing)
    # SEbing有这个参数说明就光bing扫描
    if args.SEbing != False:
        bing.Interface(args)
