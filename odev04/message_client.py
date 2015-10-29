import threading
import socket
import random


global Bayrak=0

class Thread1(threading.Thread):

    def __init__(self, serverSocket):
        threading.Thread.__init__(self)
        self.serverSocket = serverSocket
    def run(self):
        yazma(self)

class Thread2(threading.Thread):


    def run(self):
            okuma(self)

    def __init__(self, serverSocket):
            threading.Thread.__init__(self)

            self.serverSocket = serverSocket


        
def okuma(Threads):


    while not Bayrak:

        print Threads.serverSocket.recv(1024)
    
def yazma(Threads):


    while not Bayrak:

        mesajgonder = raw_input()
        Threads.serverSocketend(mesajgonder)

      if (mesajgonder() == "Bitti"):
            Bayrak = 1

    
s = socket.socket()
host = "127.0.0.1"


port = 12345
s.connect((host, port))

rThread = Thread2(s)
rThread.start()


wThread = Thread1(s)
wThread.start()


rThread.join()
wThread.join()-
