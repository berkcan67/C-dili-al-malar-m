## hesap makinasina hoş geldiniz
import math
print(
  "1. Bölme\n"
  "2. Çarpma\n"
  "3. Cikarma\n"
  "4. Toplama\n"
  "5. Us alma\n"
  "6. Karekok bulma\n"
)
x = int(input("hangi islemi secmek istiyosaniz lutfen o islemin sadece numarasini yaziniz"))
if x == 1:
    try:
        a = int(input(" a: "))
        b = int(input(" b:"))
        print(a/b)

    except ZeroDivisionError:
        print(" b sayisi 0 olamaz")
    
    except ValueError:
        print( " sadece sayisal deger giriniz!!!")

    else:
        print("işlem tamamlandı")

elif x == 2:
    try:
        a = int(input(" a: "))
        b = int(input(" b: "))
        print(a*b)

    except ValueError:
        print(" a ve b yerine sadece int sayi giriniz")

elif x == 3:
    try:
        a = int(input(" a: "))
        b = int(input(" b:"))
        print(a-b)
   
    except ValueError:
        print("sadece int deger giriniz")


elif x == 4:
    try:
        a = int(input(" a: "))
        b = int(input(" b:"))
        print(a+b)

    except ValueError:
        print("sadece int deger giriniz")


elif x == 5:
    try:
        a = int(input("lutfen max 4 basamakli bir a tabani giriniz."))
        b = int(input("lutfen max 4 basamkli bir b ussu giriniz "))
        if (a or b) >= 10000:
            print("sayi kurala uygun degil tekrar derle ve uygun sayi gir")
        else: 
            print(a**b)
    except ValueError:
        print("sadece integer sayi giriniz")

elif x ==6:
    try:
        a = int(input(" max 4 bas.lı bir pozitif integer a sayisi girin yoksa islem biter"))
        if a>=1000 or a<0:
            print(" lütfen daha önceki adimdaki kurala uygun sayi gir simdi derleyip baslayabilirsin")
        else:
            print(math.sqrt(a))

    
    except ValueError:
        print("sadece int sayi giriniz")
    
else:
    print("sadece belirtilen tuslarara basabilirsin baska tuslara basamazsin simdi senin islemini bitirecegim")



