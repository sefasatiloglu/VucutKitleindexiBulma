#Kullanicidan almamız gereken bazı değerler var.
#Kullanicidan boy ve kilosunu aliyoruz.

boy=int(input("Boyunuzu giriniz(cm cinsinden): "))
kilo=float(input("Kilonuzu giriniz: "))
#Vucut kitle endeksi hesaplama: kilo/((boy/100)**2)
vucutkitleHesapla=kilo/((boy/100)**2)
print("Vucut kitle endex'iniz {}".format(round(vucutkitleHesapla,2)))
print("Sonucunuz: ")
#Daha sonra hesapladigimiz vucut kitle endeksini if ile kontrol sagliyoruz
#Eger vucut kitle endeksi 18 ve 18'den dusuk ise cok zayif oldugunu belirtiyoruz.
#Burada tum kontroller yapilarak kullanicinin eger kilosu fazla ise ne kadar kilo vermesini de hesapliyoruz.
if vucutkitleHesapla <=18.0:
    print("Cok Zayıf")
    print("{} kg almanız gerekiyor".format(round(18.5*((boy/100)**2)-kilo,2)))
elif vucutkitleHesapla <=23.9:
    print("Normal")
elif vucutkitleHesapla<=29.0:
    print("Fazla kilolusunuz")
    print("{} kg vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
elif vucutkitleHesapla<=38.9:
    print("Obez (Sagliginiza dikkat etmeniz gerekiyor)")
    print("{} kg vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
else:
    print("Aşırı obez")
    print("{} kg vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))