__author__ = 'mesutkeskin'

import sys
import threading
import time

class myThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name


    def run(self):
        threadLock.acquire()
        oku_ve_sifrele()
        threadLock.release()


#def main(argv):
 #   if(len(sys.argv)!=2):
        #sys.exit("Lutfen 2den buyuk bir sayi giriniz ")

kayma_sayisi=input("Lutfen kayma sayisi giriniz:")
num_thread=input("Lutfen thread sayisini belirtiniz:")
num_character=input("Lutfen calisilacak karakter sayisini belirtiniz:")
global_file=open('metin.txt','r')


def oku_ve_sifrele():


    #plaintext = list(raw_input("Lutfen bir mesaj giriniz").lower())
    plaintext=global_file.read(num_character)
    plaintext=plaintext.lower()
    alfabe=list('abcdefghijklmnopqrstuvwxyz')
    #s = int(sys.argv[1])
    sifreleme = ''



    for c in plaintext:
        if c in alfabe:
            sifreleme += alfabe[(alfabe.index(c)-kayma_sayisi)%(len(alfabe))]
        else:
            sifreleme +=c

    sifreleme=sifreleme.upper()

    filename="crypted_<%d>_<%d>_<%d>.txt" %(kayma_sayisi,num_thread,num_character)
    file=open(filename,'a')
    file.write(sifreleme)
    file.close()

threadID=0
threadLock = threading.Lock()
threads = []
for n in range(num_thread):

    thread =myThread(threadID,'thread_'+str(threadID))
    thread.start()
    threads.append(thread)
    threadID=threadID+1





    #print 'Sifreli mesajiniz: ' + sifreleme

#if __name__ == "__main__":
 #   main(sys.argv[1:])

for t in threads:
    t.join()
