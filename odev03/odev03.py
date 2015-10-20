import sys

def main(argv):
    if(len(sys.argv)!=2):
        sys.exit("Lutfen 2den buyuk bir sayı giriniz ")

    plaintext = list(raw_input("Lütfen bir mesaj giriniz"))
    alfabe=list('abcdefghijklmnopqrstuvwxyz')
    s = int(sys.argv[1])
    sifreleme = ''

    for c in plaintext:
        if c in plaintext:
            sifreleme += alfabe[(alfabe.index(c)+k)%(len(alfabe))]

    print 'Şifrelenmiş mesajınız: ' + sifreleme

if __name__ == "__main__":
    main(sys.argv[1:])
