def hacimmenu():
    print ("hacimmenu")
    print("Hacim Hesaplama")
print("1 - Küp")
print("2 - Dikdörtgen prizma")

secim = input("Şekil seçin (1/2): ")

if secim == "1":
    kenar = int(input("Kenar uzunluğunu gir (tam sayı): "))
    hacim = kenar * kenar * kenar
    print("Küpün hacmi:", hacim)
elif secim == "2":
    uzunluk = int(input("Uzunluk (tam sayı): "))
    genislik = int(input("Genişlik (tam sayı): "))
    yukseklik = int(input("Yükseklik (tam sayı): "))
    hacim = uzunluk * genislik * yukseklik
    print("Dikdörtgen prizmanın hacmi:", hacim)
else:
    print("Geçersiz seçim!")
