

import threading
import socket
import time
import random


class Threads (threading.Thread):
     def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr


     def run(self):
        print "Starting Thread-" + str(self.threadID)
        Bayrak = 0
        while not Bayrak:
            try:
                self.clientSocket.settimeout(random.randint(0,9))
                Bayrak = self.clientSocket.recv(1024)
                if AlinanMesaj == "Bitti":
                   self.clientSocket.send("Bitti")
                   Bayrak=1

                else:
                    mesaj= "Mesaj alindi " + ''.join(str(self.clientAddr))
                    self.clientSocket.send(mesaj)


            except:
                saat = "Merhaba,saat şu an :" + time.asctime( time.localtime(time.time()) )
                self.clientSocket.send(saat)
        print "Ending Thread-" + str(self.threadID)
        return




s = socket.socket()
port = 12345
host = "0.0.0.0"
s.bind((host, port))
s.listen(5)
sayac = 0
while True:

    print "Bağlanmayı bekliyorum canım"
    c, addr = s.accept()
    print 'Bak burdan bir bağlantı elde ettim. ', addr
    sayac += 1
    thread = Threads(sayac , c, addr)
    thread.start()
