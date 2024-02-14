#### PHYTHON HESAP MAKİNESNE HOŞ GELDİNİZ #### 
import math

print("*************** PHYTHON HESAP MAKİNESİNE HOS GELDİNİZ **************\n")
print("işlmeler : \n 1.Toplama\n 2.Cikarma\n 3.Bolme\n 4.Carpma\n 5.Us alma\n 6.Karekok alma\n 7.EXİT ") 

while True:
    x = int(input("lutfen sadece islemin numarasini basinda nokta olmadan giriniz"))
    if x == 7:
        print("gorusmek uzere")
        break
    elif x == 1:
        sayi1 = float(input("lutfen  ilk sayiyi giriniz"))
        sayi2 = float(input("lutfen 2. sayiyi giriniz"))
        sonuc = sayi1 + sayi2
        print(sonuc)

    elif x == 2:
        sayi1 = float(input("lutfen  ilk sayiyi giriniz"))
        sayi2 = float(input("lutfen 2. sayiyi giriniz"))
        sonuc = sayi1 - sayi2
        print(sonuc)

    elif x == 3:
        try:
            sayi1 = float(input("lutfen  ilk sayiyi giriniz"))
            sayi2 = float(input("lutfen 2. sayiyi giriniz"))
            sonuc = (sayi1/sayi2)
            print(sonuc)

        except ZeroDivisionError:
            print("bir sayiyi 0 sayisina bolemezsin")
        except ValueError:
            print("lutfen sadece sayi gir")

    elif x == 4:
        try: 
            sayi1 = float(input("lutfen  ilk sayiyi giriniz"))
            sayi2 = float(input("lutfen 2. sayiyi giriniz"))
            sonuc = sayi1 * sayi2
            print(sonuc)

        except ValueError:
            print("lutfen sadece sayi giriniz.")

    elif x == 5:
        taban = int(input("lutfen tabani giriniz ama en fazla 5 basamakli ve tam sayi olsun"))
        us = int(input("lutfen tabanin ussunu giriniz ama en fazla 5 basamki ve tam sayi olsun "))
        if taban or us >= 100000:
            break
        elif taban or us != int:
            break
        else:
            sonuc = taban ** us
            print(sonuc)
    elif x == 6:
        try:
           a = int(input("lutfen karekoku alinacak sayiyi giriniz."))
           print(math.sqrt(a))

        except ValueError:
            print("lutfen sadece tam sayi giriniz")

    else:
        print("boyle bir islev yok tekrar tuslayiniz lutfen")
        
        


    

        
        




        

      