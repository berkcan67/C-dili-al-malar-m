### 200'e kadar olan cift sayilari toplayan python yazilimi. 200 dahil degil

i = 0
toplam = 0

while (i<200):
    i = i + 1
    if (i%2==0):
        toplam = toplam + i
    else:
        continue

print(f" 0' dan 200'e kadar olan cift sayilarin toplami:",toplam)
