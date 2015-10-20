import sys
import thread


def main(argv):
    if(len(sys.argv)!=2):
        sys.exit("Lutfen 2den buyuk bir sayi giriniz ")

    file=open('metin.txt','r')


    #plaintext = list(raw_input("Lutfen bir mesaj giriniz").lower())
    plaintext=file.read()
    plaintext=plaintext.lower()
    alfabe=list('abcdefghijklmnopqrstuvwxyz')
    s = int(sys.argv[1])
    sifreleme = ''



    for c in plaintext:
        if c in alfabe:
            sifreleme += alfabe[(alfabe.index(c)-s)%(len(alfabe))]
        else:
            sifreleme +=c

    sifreleme=sifreleme.upper()

    filename="crypted_<%d>.txt" %s
    file = open(filename,'w')
    file.write(sifreleme)
    file.close()


    #print 'Sifreli mesajiniz: ' + sifreleme

if __name__ == "__main__":
    main(sys.argv[1:])
