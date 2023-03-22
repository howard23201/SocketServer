import netifaces as ni

class Networks:
    interfaces = None
    addresses = []
    cnt = 0
    # 获取本机所有网络接口的信息
    def __init__(self):
        self.interfaces = ni.interfaces()
        for interface in self.interfaces:
            self.cnt += 1
            self.addresses.append(ni.ifaddresses(interface))
    def GetIP(self):
        resultArray = []
        for address in self.addresses:
            # 获取每个网络接口的 IPv4 地址信息
            if ni.AF_INET in address:
                ip_info = address[ni.AF_INET][0]
                # print(f'IP Address: {ip_info["addr"]}')
                resultArray.append(ip_info["addr"])
        return resultArray
    def GetMAC(self):
        resultArray = []
        # 获取每个网络接口的 MAC 地址信息
        for address in self.addresses:
            if ni.AF_LINK in address:
                mac_info = address[ni.AF_LINK][0]
                resultArray.append(mac_info["addr"])
        return resultArray
    def GetName(self):
        resultArray = []
        for iface in self.interfaces:
            addrs = ni.ifaddresses(iface)
            if ni.AF_INET in addrs.keys():
                
                resultArray.append(iface)
        return resultArray
# n = Networks()
# # s = n.GetIP()
# # for ss in s:
# #     print(ss)
# s = n.GetName()

# print(s)
