def sekil_cizmenu():
    print ("sekil_cizmenu")
    
print("Şekil çizdirme uygulamasına hoş geldin!")
print("1 - Üçgen\n2 - Kare")
secim = input("Hangi şekli çizmek istersin? (1/2): ")

if secim == "1":
    print("  *  ")
    print(" *** ")
    print("*****")
elif secim == "2":
    print("******")
    print("******")
    print("******")
else:
    print("Geçersiz seçim!")

