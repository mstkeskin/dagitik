import sys

import threading

def main(argv):
    if(len(sys.argv)!=2):
        sys.exit("Lutfen 2den buyuk bir sayi giriniz ")

    plaintext = list(raw_input("Lutfen bir mesaj giriniz"))
    alfabe=list('abcdefghijklmnopqrstuvwxyz')
    s = int(sys.argv[1])
    sifreleme = ''

    for c in plaintext:
        if c in alfabe:
            sifreleme += alfabe[(alfabe.index(c)-s)%(len(alfabe))]
        else:
            sifreleme +=c

    sifreleme=sifreleme.upper()

    print 'Sifreli mesajiniz: ' + sifreleme

if __name__ == "__main__":
    main(sys.argv[1:])
