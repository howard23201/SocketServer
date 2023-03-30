from lib.NetworkInterfaces import Networks
from lib.SocketServer import Server

import math
from threading import Thread

def Main():
    Net = Networks()
    ips = Net.GetIP()
    server = None
    ServerIP = ""
    while(True):
        try:
            print("\n-------------------\n"+
                "1: start server\n"+
                "2: send msg\n"+
                "3: stop server\n"+
                "4: Check ip address\n"+
                "-------------------\n")
            Cmd = input('please enter a number:\n')
            if(Cmd == '1'):
                strIP = ""
                i = 0
                for i in range(len(ips)):
                    cnt = str(i + 1)
                    strIP += "{0} => {1}\n".format(cnt,ips[i])
                num = int(input("Please choose an IP address to start.\n{0}\n=>".format(strIP)))
                
                print('local ip: {0}:{1},waiting for a client connection...'.format(ips[num - 1],10000))
                server = Server(ips[num - 1],10000)
                ServerIP = "{0}:{1}".format(ips[num - 1],10000)
                Sthread = Thread(target = server.Start)
                Sthread.start()
            elif(Cmd == '2'):
                msg = input('please enter cmd:')
                server.SendCommand(msg)
                print("server sent: {0}\n".format(msg))
            elif(Cmd == '3'):
                server.Stop()  
                print("server closed\n")
            elif(Cmd == '4'):       
                print('Server IP address: {0}\n'.format(ServerIP))
            else:
                print("undefine code\n")
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    Main() 