## arac bilgilendirme sihirbazi

def bilgi_al():
    telno = input("aracla bilgi almak icin numaranizi tuslayiniz")
    email = input("aracla bilgi almak ici emailini gir")
    print("telefon numaraniz:",telno)
    print(" e-mailiniz:",email)

print("merhaba arac olusturucuya hos geldiniz.\n")

print("lutfen istediginiz araci liste icinden numarasini yaziniz\n")

print("1.Mercedes-Maybach-s600","2.Bmw-760-Li","3.Audi-A8L")

y= int(input("lutfen istediginiz secenegin numarasini seciniz:"))
if  y == 1:
    print("aracin fiyati : 130.000 euro")

elif  y == 2:
    print("aracin fiyati : 200.000 euro ")

elif y == 3:
    print("aracin fiyati : 176.000 euro")

else:
    print("error 404")

print("aracla ilgili size ulaşmamizi ister misiniz?")


x = int(input("bilgi almak istiyorsaniz 1 istemiyosaniz 0 tusla"))


if x == 1:
    bilgi_al()
    print( "size ulasacagiz.")
    break
else :
    print("sistemden çıkınız lütfen ")
    break










