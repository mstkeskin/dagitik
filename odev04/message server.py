import threading

__author__ = 'mesutkeskin'

import socket
import threading
import time
class myThread (threading.Thread):

    def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
    def run(self):
        print "Starting Thread-" + str(self.threadID)



s = socket.socket()
host = "0.0.0.0"
port = 12345
s.bind((host, port))
s.listen(5)
while True:
        print "Bağlantı için beklneiyor"
        c, addr = s.accept()
        print 'Aman allafım bak burdan bir bağlantı edindim ', addr
        threadCounter += 1
        thread = myThread(threadCounter, c, addr)
        thread.start()
