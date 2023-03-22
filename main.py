from lib.NetworkInterfaces import Networks
from lib.SocketServer import Server

import math
from threading import Thread

def Main():
    Net = Networks()
    ips = Net.GetIP()
    server = None
    while(True):
        try:
            print("\n-------------------\n"+
                "1: start server\n"+
                "3: stop server\n"+
                "4: fsffslkgj;lgh\n"+
                "-------------------\n")
            str = input('please enter a number:\n')
            if(str == '1'):
                print('local ip: {0}:{1},waiting for a client connection...'.format(ips[0],10000))
                server = Server(ips[0],10000)
                Sthread = Thread(target = server.Start)
                Sthread.start()
            # elif(str == '2'):
            #     msg = input('please enter cmd:')
            #     server.SendCommand(msg)
            #     print("server sent: {0}\n".format(msg))
            elif(str == '3'):
                server.Stop()  
                print("server closed\n")
            elif(str == '4'):       
                print("fsffslkgj;lgh\n")
            else:
                print("undefine code\n")
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    Main() 