def not_hesaplamenu():
    print ("not_hesaplamenu")
    
print("Not Hesaplama Programı")
vize = int(input("Vize notunu gir: "))
final = int(input("Final notunu gir: "))
ortalama = (vize * 0.4) + (final * 0.6)

print("Ortalaman:", ortalama)

if ortalama >= 50:
    print("Geçtin! ✅")
else:
    print("Kaldın! ❌")
