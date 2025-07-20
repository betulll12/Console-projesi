def zammenu():
    print ("zammenu")
    print("Zam Hesaplama")

maas = int(input("Mevcut maaşınızı gir (tam sayı): "))
zam_orani = int(input("Zam oranını yüzde olarak girin (örnek: %20 için 20): "))

zam_miktari = (maas * zam_orani) // 100
yeni_maas = maas + zam_miktari

print("Zamlı maaşınız:", yeni_maas)
