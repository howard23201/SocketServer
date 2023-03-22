import socket
from threading import Thread

class Server:
    server_socket = None
    server_address = ''
    client_socket = None
    client_address = ''
    step = 0

    Acceptthread = None
    def __init__(self,IP,port):
        # bind the socket to a specific address and port
        self.server_address = (IP, port)
        # print("\nServer: {0}\n".format(self.server_address))
        
    def Start(self):
        while True:
            try:
                # print("\nstep: {0}\n".format(self.step))
                if(self.step == 0):
                    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.server_socket.bind(self.server_address)
                    self.server_socket.listen(1)
                    self.server_socket.setblocking(False)
                    self.step = 1
                elif(self.step == 1):
                    if(self.server_socket != None):
                        self.BeginAcceptClient()
                        if(self.client_socket != None):
                            # self.server_socket.setblocking(True)
                            self.step = 2
                elif(self.step == 2):
                    while(self.step != -1):
                        try:
                            data = self.client_socket.recv(1024)
                            if(self.client_socket != None) and (len(data) != 0):
                                data = data.decode()
                                if data.endswith("\r\n"):
                                    data = data.replace("\r\n","")
                                print('==> RECV: {0}'.format(data))
                            elif(len(data) == 0):
                                self.step = 1
                                break
                        except socket.error:
                            pass
                        
                elif(self.step == -1):
                    break
            except Exception as ex:
                print("\nServer Exception: {0}\n".format(ex))
                self.step = -1
        if(self.client_socket != None):
            self.client_socket.close()
            while True:
                try:
                    self.client_socket.getpeername()
                except OSError:
                    break
        self.server_socket.close()
        while True:
            try:
                self.server_socket.getsockname()
            except OSError:
                break
    def SendCommand(self,Msg):
        try:
            if(self.client_socket != None):
                Msg = str(Msg).encode()
                self.client_socket.send(Msg)
                print('<== SEND: {0}'.format(Msg.decode()))    

            else:
                print("server is down")
        except:
            print("error")
    def BeginAcceptClient(self):
        while self.step != -1:
            try:
                ClientTuple = self.server_socket.accept()
                if ClientTuple != ():
                    response = 'Hello, client!'
                    self.client_socket = ClientTuple[0]
                    self.client_address = ClientTuple[1]
                    self.client_socket.send(response.encode())
                    print('\nConnected: ', self.client_address)   
                    break
            except socket.error:
                pass

                       
    def Restart(self):
        self.server_socket.close()
        self.step = 0
    def Stop(self):
        self.step = -1
        

    
# s = Server("10.228.33.116",10000)   
# s.Start()