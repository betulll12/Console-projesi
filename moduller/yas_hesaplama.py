def yas_hesaplamamenu():
    print ("yas_hesaplamamenu")
    print("Yaş Hesaplama Programı")
dogum = int(input("Doğum yılını gir: "))
yas = 2025 - dogum

print("Yaşın:", yas)

if yas >= 18:
    print("Reşitsin.")
else:
    print("Reşit değilsin.")
