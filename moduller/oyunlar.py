def oyunlarmenu():
    print ("oyunlarmenu")

print("Sayı Tahmin Oyununa Hoş Geldin!")
print("1 ile 10 arasında bir sayı tuttum, tahmin et.")
sayi = "3"
tahmin = input("Tahminin nedir? ")

if tahmin == sayi:
    print("Tebrikler! Bildin!")
else:
    print("Üzgünüm, bilemedin. Doğru cevap:", sayi)



