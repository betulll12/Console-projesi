def bmimenu():
    print ("bmimenu")
    print("BMI (Vücut Kitle İndeksi) Hesaplama")
kilo = float(input("Kilonuzu girin (kg): "))
boy = float(input("Boyunuzu girin (metre): "))
bmi = kilo / (boy * boy)

print("BMI değeriniz:", bmi)

if bmi < 18.5:
    print("Zayıf")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Fazla kilolu")
else:
    print("Obez")
