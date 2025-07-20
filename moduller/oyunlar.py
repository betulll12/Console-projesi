def oyunlarmenu():
    print ("oyunlarmenu")

print("Oyunlar Menüsü")
print("1 - Sayı Tahmin Etme")
print("2 - Kelime Tahmin Etme")
print("3 - Taş Kağıt Makas")

secim = input("Bir oyun seçin (1/2/3): ")

# 1️⃣ Sayı Tahmin Etme
if secim == "1":
    print("Sayı Tahmin Oyununa Hoş Geldin!")
    print("1 ile 10 arasında bir sayı tuttum, tahmin et.")
    sayi = "3"
    tahmin = input("Tahminin nedir? ")

    if tahmin == sayi:
        print("Tebrikler! Bildin")
    else:
        print("Üzgünüm, bilemedin. Doğru cevap:", sayi)

# 2️⃣ Kelime Tahmin Etme
elif secim == "2":
    print("Kelime Tahmin Oyununa Hoş Geldin!")
    print("İpucu: K_____ (K harfiyle başlıyor,obje)")

    tahmin = input("Kelime tahminin nedir?: ")

    if tahmin == "kitap":
        print("Doğru bildin!")
    else:
        print("Yanlış tahmin. Doğru cevap: kitap")

# 3️⃣ Taş Kağıt Makas
elif secim == "3":
    print("Taş - Kağıt - Makas oyununa hoş geldin!")
    print("Seçenekler: taş, kağıt, makas")
    oyuncu = input("Senin seçimin: ")
    bilgisayar = "taş"  # sabit rakip

    print("Bilgisayar:", bilgisayar)

    if oyuncu == bilgisayar:
        print("Berabere!")
    elif oyuncu == "kağıt":
        print("Sen kazandın!")
    elif oyuncu == "makas":
        print("Kaybettin")
    elif oyuncu == "taş":
        print("Berabere!")
    else:
        print("Geçersiz seçim!")

# Geçersiz seçim
else:
    print("Geçersiz seçim! Lütfen 1, 2 veya 3 gir.")

