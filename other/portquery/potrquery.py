from other.portquery import tcpudp


def tcp_query(tcp):

    if tcp in tcpudp.tcp.keys():
        print(f"此{tcp}端口={tcpudp.tcp[tcp]}\n\n")
    else:
        print("对不起作者还没有添加，你可以去自己添加")
def udp_query(udp):

    if udp in tcpudp.udp.keys():
        print(f"此{udp}端口={tcpudp.udp[udp]}")
    else:
        print("对不起作者还没有添加，你可以去自己添加")

def Interfacemian(args):
    tcp=args.tcp
    udp=args.udp

    if tcp != None:
        tcp_query(tcp)
    if udp != None:
        udp_query(udp)

if __name__=="__main":
    udp_query("53")