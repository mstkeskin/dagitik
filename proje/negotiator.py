import Queue
import socket
import time
import threading
import datetime

import timestring

connect_point_list = {}
connect_point={}

class TestThread(threading.Thread):
        def  __init__(self, name,port,ip,connect_point_list):

            threading.Thread.__init__(self)
            self.name = name
            self.ip = ip
            self.port=port
            self.connect_point_list=connect_point_list

        def run(self):

            self.socket=socket.socket()
            self.socket=socket.connect((self.ip,self.port))
            self.socket.sendall("HELLO")
            mesaj_1=""
            while True:
                gecici_list=connect_point_list.copy()
                mesaj_1=self.socket.recv(1024)

                time.sleep(10)
                try:
                    print("Gelen cevap:")+mesaj_1
                    if mesaj_1=="SALUT":
                        self.socket.sendall("REGWA")
                        self.gecici_list[str(self.port)]='W'
                        self.gecici_list[str(self.port)]=str(datetime.strptime("%H:%M:%S.%f", timestring).time)
                    elif mesaj_1  !=  "SALUT":
                        self.socket.sendall("REGER")

                except socket.timeout:
                    self.socket.close()

class ServerThread(threading.Thread):
        def  __init__(self, name,ClientSocket,port,ip,Queue,connect_point_list):

            threading.Thread.__init__(self)
            self.name = name
            self.ClientSocket=ClientSocket
            self.ip = ip
            self.port=port
            self.Queue=Queue
            self.connect_point_list=connect_point_list

        def parser(self,data):

            data=data.strip()


            if data[0:5] == "HELLO":
                response="SALUT"
                self.ClientSocket.send(response)

            elif data[0:5] =="CLOSE":
                response="BUBYE"
                self.ClientSocket.send(response)
                self.ClientSocket.close()

            elif data[0:5]=="REGME":
                data= data[6:].split(":")
                ip=data[0]
                port=data[1]
                connect_point={'ip':'port'}

                if connect_point_list.has_key(ip,port):
                    response='REGOK'+str(datetime.strptime("%H:%M:%S.%f", timestring).time)
                    self.cSocket.send(response)

                else:
                    response='REGWA'
                    connect_point_list[(connect_point)]=('W',str(datetime.strptime("%H:%M:%S.%f", timestring).time))
                    self.ClientSocketSocket.send(response)

            elif data[0:5] == "GETNL":
                            data = data[6:]
                            j=data
                            return j
            else:
                   response = "CMDER"
                   return response


        def run(self):



            self.socket=socket.socket()
            self.socket=socket.bind((self.ip,self.port))
            self.socket.listen(4)

            while True:
                gelen_data=self.socket.recv(1024)
                mesaj=self.parser(gelen_data)
                if gelen_data != "":
                    print "gelen_data:"+gelen_data

            self.socket.close()

class ClientReaderThread(threading.Thread):
        def  __init__(self, name,ClientSocket,port,ip,Queue,connect_point_list):

            threading.Thread.__init__(self)
            self.name = name
            self.ClientSocket=ClientSocket
            self.ip = ip
            self.port=port
            self.Queue=Queue
            self.connect_point_list=connect_point_list

        def parser(self,data):

            if data[0:5] == "BUBYE":

                self.socket.close()
            else:
                response="REGER"
                print("REGER")

        def run(self):


            while True:
                gelen_data=self.ClientSocket.recv(1024)
                mesaj=self.parser(gelen_data)
                if gelen_data != "":
                    print "gelen_data:"+gelen_data

                else:
                    break



class ClientThread(threading.Thread):

        def  __init__(self, name,ClientSocket,port,ip,Queue,connect_point_list):

                threading.Thread.__init__(self)
                self.name = name
                self.ClientSocket=ClientSocket
                self.ip = ip
                self.port=port
                self.Queue=Queue
                self.connect_point_list=connect_point_list

        def run(self):
            self.Queue.put("HELLO")


            while True:
                if self.Queue.size()>0:

                    gelen_data=self.ClientSocket.recv(1024)
                mesaj=self.parser(gelen_data)
                if gelen_data != "":
                    print "gelen_data:"+gelen_data

                else:
                    break
