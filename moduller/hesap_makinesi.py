def hesap_makinesimenu():
    print ("hesap_makinesimenu")

    print("HESAP MAKİNESİ MENÜSÜ")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Ana Menüye Dön")

    islem = input("İşlem seçiniz: ")


    if islem == "1":
        sayi1 = input("1. sayıyı giriniz: ")
        sayi2 = input("2. sayıyı giriniz: ")
        print("Sonuç =", int(sayi1) + int(sayi2))
    elif islem == "2":
        sayi1 = input("1. sayıyı giriniz: ")
        sayi2 = input("2. sayıyı giriniz: ")
        print("Sonuç =", int(sayi1) - int(sayi2))
    elif islem == "3":
        sayi1 = input("1. sayıyı giriniz: ")
        sayi2 = input("2. sayıyı giriniz: ")
        print("Sonuç =", int(sayi1) * int(sayi2))
    elif islem == "4":
        sayi1 = input("1. sayıyı giriniz: ")
        sayi2 = input("2. sayıyı giriniz: ")
        print("Sonuç =", int(sayi1) / int(sayi2))
    else:
        print("Ana menüye dönülüyor...")    
    