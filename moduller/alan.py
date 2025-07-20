def alanmenu():
    print ("alanmenu")
    print("Alan Hesaplama")
print("1 - Dikdörtgen")
print("2 - Üçgen")

secim = input("Şekil seçin (1/2): ")

if secim == "1":
    uzunluk = int(input("Uzunluğu gir (tam sayı): "))
    genislik = int(input("Genişliği gir (tam sayı): "))
    alan = uzunluk * genislik
    print("Dikdörtgenin alanı:", alan)
elif secim == "2":
    taban = int(input("Tabanı gir (tam sayı): "))
    yukseklik = int(input("Yüksekliği gir (tam sayı): "))
    alan = (taban * yukseklik) // 2
    print("Üçgenin alanı:", alan)
else:
    print("Geçersiz seçim!")
