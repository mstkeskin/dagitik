__author__ = 'mesutkeskin'

import Queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q



    def run(self):
        print "Starting " + self.name
        #threadLock.acquire()
        oku_ve_sifrele(self.name,self.q)
        #threadLock.release()
        print "Exiting " + self.name


#def main(argv):
 #   if(len(sys.argv)!=2):
        #sys.exit("Lutfen 2den buyuk bir sayi giriniz ")

s=input("Lutfen kayma sayisi giriniz:")
num_thread=input("Lutfen thread sayisini belirtiniz:")
num_character=input("Lutfen calisilacak karakter sayisini belirtiniz:")
global_file=open('metin.txt','r')


def oku_ve_sifrele(threadName,q):
   while not exitFlag:
       queueLock.acquire()
       if not workQueue.empty():
            data = q.get()
            plaintext=global_file.read(num_character)
            plaintext=plaintext.lower()
            alfabe=list('abcdefghijklmnopqrstuvwxyz')

            sifreleme = ''
            for c in plaintext:
                if c in alfabe:
                    sifreleme += alfabe[(alfabe.index(c)-s)%(len(alfabe))]
                else:
                    sifreleme +=c

                sifreleme=sifreleme.upper()
            filename="crypted_%d_%d_%dtxt" %(s,num_thread,num_character)
            file=open(filename,'a')
            file.write(sifreleme)
            file.close()

            queueLock.release()

       else:
           queueLock.release()




queueLock = threading.Lock()
workQueue = Queue.Queue()


threadID=0


threads = []
for n in range(num_thread):
    thread =myThread(threadID,'thread_'+str(threadID),workQueue)
    thread.start()
    threads.append(thread)
    threadID +=1

queueLock.acquire()
for l in range(num_thread):
             workQueue.put(l)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
     t.join()
print "Exiting Main Thread"
