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
        print("server bind at: {0}".format(self.server_address))
        self.server_address = (IP, port)
        
    def Start(self):
        while True:
            try:
                print("step: "+ str(self.step))
                if(self.step == 0):
                    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.server_socket.bind(self.server_address)
                    self.server_socket.listen(1)
                    self.server_socket.setblocking(False)
                    self.step = 1
                elif(self.step == 1):
                    if(self.server_socket != None):
                        self.BeginAcceptClient()
                        while(self.step != -1):
                            if(self.client_socket != None):
                                self.step = 2
                                break
                elif(self.step == 2):
                    while(True):
                        try:
                            data = self.client_socket.recv(1024)
                            if(self.client_socket != None) and (len(data) != 0):
                                data = data.decode()
                                print('received: {0}'.format(data))          
                            else:
                                self.Restart()
                                break
                        except Exception as ex:
                            print("socket closed,"+ str(ex)+"\n")
                            self.Restart()
                elif(self.step == -1):
                    break
            except Exception as ex:
                print(ex)
                self.step = -1
        # self.server_socket.shutdown(socket.SHUT_RD)
        
        self.Acceptthread = None
        while True:
            if self.Acceptthread == None:
                break
        self.server_socket.close()
        self.server_socket = None
    def SendCommand(self,Msg):
        try:
            if(self.client_socket != None):
                Msg = str(Msg)
                self.client_socket.send(Msg.encode())
            else:
                print("server is down")
        except:
            print("error")
    def BeginAcceptClient(self):
        while True:
            try:
                ClientTuple = self.server_socket.accept()
                if ClientTuple != ():
                    response = 'Hello, client!'
                    self.client_socket = ClientTuple[0]
                    self.client_address = ClientTuple[1]
                    self.client_socket.send(response.encode())
                    print('connection from', self.client_address)   
            except socket.error as e:
                
                print(e)
                raise

                       
    def Restart(self):
        if(self.step == 2):
            self.client_socket.shutdown(socket.SHUT_RDWR)
        self.server_socket.close()
        self.server_socket = None
        self.step = 0
    def Stop(self):
        if(self.step == 2):
            self.client_socket.shutdown(socket.SHUT_RDWR)
        
        self.step = -1
        

    
# s = Server("10.228.33.116",10000)   
# s.Start()