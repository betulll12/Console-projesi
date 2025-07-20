def anamenu():
    print ("anamenu")

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║   Vektorel App      ║")
    print("║                     ║")
    print("║  1-Hesap makinesi   ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Şekil çizdirme   ║")
    print("║  4-Not Hesaplama    ║")
    print("║  5-Yaş hesaplama    ║")
    print("║  6-BMI hesaplama    ║")
    print("║  7-Zam hesaplama    ║")
    print("║  8-Alan hesaplama   ║")
    print("║  9-Hacim hesaplama  ║")
    print("║  10-Çıkış           ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")


    secim = input("Seçiminizi yapınız (1-10):")
    if secim=="1":
        import moduller.hesap_makinesi
        moduller.hesap_makinesi.hesap_makinesimenu()  
    if secim=="2":
        import moduller.oyunlar
        moduller.oyunlar.oyunlarmenu()  
    if secim == "3":
        import moduller.sekil_ciz
        moduller.sekil_ciz.sekil_cizmenu()
    if secim == "4":
        import moduller.not_hesapla
        moduller.not_hesapla.not_hesaplamenu()
    if secim == "5":
        import moduller.yas_hesaplama
        moduller.yas_hesaplama.yas_hesaplamamenu()
    if secim == "6":
        import moduller.bmi
        moduller.bmi.bmimenu()
    if secim == "7":
        import moduller.zam
        moduller.zam.zammenu()
    if secim == "8":
       import moduller.alan
       moduller.alan.alanmenu()
    if secim == "9":
       import moduller.hacim
       moduller.hacim.hacimmenu()

    if secim == "10":
        print("Çıkış")
        exit()

    else:
     print("Geçersiz seçim! Lütfen tekrar deneyin.")    

anamenu()
    
    