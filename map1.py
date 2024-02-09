## map fonk. kullanarak once kup, sonra kare alip yazdirmak 
## map fonk. kullanarak sayilari pozitif hale getirip yazdirmak
## map fonk. kullanarak sayilari int den float'a dönüştürmek
## map fonk kullanarak isimler yazip ilk harflerini buyuk yazmak
## map fonk kullanarak isimler yazip tum harflerini buyuk yazmak


def kupAl(sayi):
    return sayi ** 3

sayilar = [1,2,3,4,5]
negatif_sayilar = [-8,-32]
isimler = ["hans","george","adam"]


sonuc1 = list(map(kupAl,sayilar))
print(sonuc1)

sonuc2 = list(map(lambda sayi : sayi **2 , sayilar))
print(sonuc2)

sonuc3 = list(map(abs,negatif_sayilar))
print(sonuc3)

sonuc4 = list(map(float,sayilar))
print(sonuc4)

sonuc5 = list(map(str.capitalize,isimler))
print(sonuc5)

sonuc6= list(map(str.upper,isimler))
print(sonuc6)