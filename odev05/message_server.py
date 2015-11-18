_author__ = 'mesutkeskin'
import Queue
import socket
import time
import threading

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
fihrist = {}
lqueue = Queue.Queue()

threadLock = threading.Lock()


def main():
    tcounter = 0
    global fihrist
    log_thread = myThreads('LogThread', lqueue, 'log.txt')
    log_thread.start()


    while True:

        lqueue.put("Baglanti icin bekleniyor")

        client_socket, client_address = s.accept()

        lqueue.put("Ahanda buradan bir baglanti elde ettim %s" % str(client_address))
        tcounter += 1


        queue = Queue.Queue()
        WriteThread('WriteThread_' + str(tcounter), client_socket, client_address,queue,
                    lqueue).start()


        ReadThread('ReadThread_' + str(tcounter), client_socket, client_address, queue,
                   lqueue, fihrist).start()


    lqueue.put("Bitti")


    log_thread.join()


class ReadThread(threading.Thread):


    def __init__(self, thread_name, client_socket, client_address, queue, lqueue, fihrist):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.client_socket = client_socket
        self.client_address = client_address
        self.queue = queue
        self.lqueue = lqueue
        self.nick = ""
        self.fihrist = fihrist

    def run(self):
        self.lqueue.put("Basliyor %s" % self.thread_name)
        while True:
            received_message = self.client_socket.recv(1024)
            result = self.parser(received_message)
            if not result == 0:
                self.queue.put('Bitis')
                break
        self.lqueue.put("Bitiyor %s" % self.thread_name)

    def parser(self, data):
        global threadLock
        data = data.strip()


        if len(data) < 3 or " " in data[0:3] or (len(data) > 3 and data[3] != " "):
            self.sending("ERR\n")
            return 0


        code = data[0:3]

        argument = data[4:]
        # ERL Hatasi


        if not self.nick and code != "USR":
            response = "ERL"


        elif self.nick == "" and code == "USR":
            nick = argument


            #  nick fihristte yoksa ekleniyor
            if nick not in self.fihrist.keys():
                self.nick = nick


                # yenisi ekleniyor.
                self.fihrist.update({self.nick: self.queue})
                response = "HEL " + self.nick
                self.lqueue.put(self.nick + " katildi.")


            # nick varsa reddediliyor.
            else:
                response = "REJ " + nick


        # cikis istenirse

        elif code == "QUI":
            self.fihrist.pop(self.nick)
            response = "Gule Gule guzelim " + self.nick
            self.sending(response)
            self.client_socket.close()
            self.lqueue.put(self.nick + " ayrildi.")
            return 1




        # kullanicilar


        elif code == "LSQ":
            response = "LSA " + "".join('%s:' % k for k in self.fihrist.keys()).rstrip(':')

            # Baglanti testi(Tic-toc)

        elif code == "TIC":
            response = "TOC"

        # Mesaj genelse

        elif code == "SAY":      # thread kilitleniyor

            threadLock.acquire()
            for to_nick in self.fihrist.keys():
                fihrist[to_nick].put((self.nick, argument))

            threadLock.release()   # thread aciliyor
            response = "SOK"


        # ozel mesajsa


        elif code == "MSG" and ':' in argument:
            to_nick, message = argument.split(':', 1)
            to_nick = to_nick.strip()
            message = message.strip()
            if to_nick not in self.fihrist.keys():
                response = "MNO " + to_nick
            else:

                threadLock.acquire() # thread kitlenir
                fihrist[to_nick].put((to_nick, self.nick, message))

                threadLock.release()  # thread acilir
                response = "MOK"


        # sistem mesaji
        elif code == "SYS":
            threadLock.acquire()
            self.queue.put(argument)
            threadLock.release()
            response = "YOK"
        # ERR hatasi
        else:
            response = "ERR"


        self.sending(response + "\n")


        return 0

    def sending(self, data):


        self.client_socket.send(data)


class WriteThread(threading.Thread):
    def __init__(self, thread_name, client_socket, client_address, queue, lqueue):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

        self.client_address = client_address
        self.client_socket = client_socket
        self.lqueue = lqueue
        self.queue = queue


    def run(self):
        self.lqueue.put("Basliyor %s" % self.thread_name)
        while True:
            if not self.queue.empty():
               data_queue = self.queue.get()

               if data_queue == "Bitti":
                        break
               else:
                    # genel mesajsa
                    if len(data_queue) == 2:
                        from_nick, message = data_queu
                        message_to_send = "SAY %s:%s" % (from_nick, message)

                    # gonderilen ozel mesajsa
                    elif len(data_queue) > 2:
                        to_nick, from_nick, message = data_queue
                        message_to_send = "MSG %s:%s" % (from_nick, message)

                    # hicbiri degilse sistem mesajidir
                    else:
                        message_to_send = "SYS %s" % data_queue
                    try:
                        self.sending(message_to_send)
                    except socket.error:
                        self.client_socket.close()
                        break
        self.lqueue.put("Bitiyor %s" % self.thread_name)

    def sending(self, data):
        self.client_socket.send(data)


class myThreads(threading.Thread):
    def __init__(self, thread_name, lqueue, log_file_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.lqueue = lqueue
        self.log_file_name = log_file_name
        self.log_file = open(log_file_name, 'a+')

    def log(self, message):
        # kilitleniyor
        threadLock.acquire()
        t = time.ctime()
        self.log_file.write("%s: %s\n" % (t, message))
        self.log_file.flush()
        # kilit açılıyor
        threadLock.release()

    def run(self):
        self.log("Basliyor %s" % self.thread_name)
        while True:
            if not self.lqueue.empty():
                to_be_logged = self.lqueue.get()
                if to_be_logged == "Bitti":
                    break
                else:
                    self.log(to_be_logged)
        self.log("Bitiyor %s" % self.thread_name)
        self.log_file.close()


if __name__ == '__main__':
    main()
