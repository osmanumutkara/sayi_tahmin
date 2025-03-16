import random
tahmin_adet=0
sayi=random.randint(1,100)
hak_adet=int(input("tahmin için kaç hak istiyorsunuz: "))
while True:
    tahmin=int(input("tahmin için bir sayı giriniz:"))
    tahmin_adet=tahmin_adet+1
    if tahmin==sayi:
        print("tebrikler doğru bildiniz puanınız:",100-((100/hak_adet)*(tahmin_adet)))
        break
    elif tahmin>sayi:
        print("çok söyledin aşağı in")
    elif hak_adet<=tahmin_adet:
        print("hakkınızı doldurdunuz lütfen daha sonra tekrar deneyiniz.")
        print("Sayı aslında buydu:",sayi)
        break
    elif tahmin<sayi:
        print("az söyledin yukarı")