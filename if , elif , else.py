# # №1
harorat = int(input("Bugun necha gradus?>>>"))
if harorat < 0:
    print("Bugun sovuq")
elif 0 <= harorat <= 20:
    print("Bugun salqin kun")
elif 21 <= harorat <= 30 :
    print("Bugugn iliq")
else :
    print("Bugun issiq kun")




# №2
sum = int(input("Summa kiriting>>>"))
if sum < 50000 :
    print("Chegirma yo'q")
elif 50000 <= sum <= 100000 :
    skidka = sum * 0.05
    summ = sum - skidka
    print(f"5% chegirma bilan : {summ} sum" )
else:
    skidka = sum * 0.1
    summ = sum - skidka
    print(f"10% chegirma bilan :{summ} sum")




# №3
login = input("Login kiriting>>>")
parol = int(input("Parol kiriting>>>"))
if login == "admin" and parol == 12345:
    print("Xush kelibsiz admin")
else:
    print("Login yoki parol xato")




# №4
yosh = int(input("Yoshingizni kiriting>>>"))
if yosh < 13 :
    print( "Sizga ushbu film tavsiya etilmaydi")
elif 13 <= yosh <=17 :
    print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
else:
    print("Siz filmni tomosha qilishingiz mumkin")




# №5
print("""1-Osh
2-Mastava
3-Shashlik""")
taom = input("Salam aleykum nima yemokchi siz?:").title()
if taom == "Osh" :
    print("Narxi:60.000\n5 minutga olib kelamiz")
elif taom == "Mastava" :
    print("Narxi:30.000\n15 minutga tayor boladi")
elif taom == "Shashlik" :
    print("Narxi:13.000\n10minutga tayor boladi")
else:
    print("Bunday taom yoq!")




# №6
pochta = input("Email kiriting>>>")
if pochta.find("@") != -1 and pochta.find(".") != -1 :
    print( "Email qabul qilindi" )
else:
   print("Noto'g'ri email manzili")




# №7
baho = int(input("Nechta bal olding?:"))
if 86 <= baho <= 100:
        print("5 baho")
elif 70 <= baho <= 85:
        print("4 baho")
elif 55 <= baho <= 69:
        print("3 baho")
elif 0 <= baho < 55:
        print("2 baho")
else:
    print("Xato! Bal 0 va 100 orasida bo'lishi kerak")




# №8
karta = int(input("Karta summa>>>"))
summa = int(input("Nechi summ yechmoqchisiz?>>>"))
if karta < summa:
    print("Hisobda yetarli mablag' mavjud emas")
elif summa < 5000:
    print("Minimal yechish summasi 5 000 so'm")
else:
    print("Pul muvaffaqiyatli yechildi")
    print(f"Kartada {karta - summa} so'm qoldi")


# №9
kun = input("Bugun qaysi kun?:").title()
if kun == "Shanba" or kun == "Yakshanba" :
    print("Bugun dam olish!")
elif kun == "Dushanba" or kun == "Seshanba" or kun == "Chorshanba" or kun == "Payshanba" or kun == "Juma":
    print("Ish kuni bugun")
else:
    print("Hafta kunini kiriting!")




# №10
trafik = float(input("Oyiga qancha internet trafikidan foydalanasiz! (GB da): "))
if trafik < 1 :
    print("Sizga 'Mini' tarifi mos keladi")
elif trafik <= 5 :
    print("Sizga 'Standard' tarifi mos keladi")
else:
    print("Sizga 'Unlimited' tarifi mos keladi")

