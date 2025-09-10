# # №1
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for pochta  in pochtalar:
#     if "@" in pochta:
#         print(f"To'g'ri email: {pochta}")
#     else:
#         print(f"Noto'g'ri email: {pochta} ")
#
#
#
# # №2
# parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# for parol in parollar:
#     if len(parol) < 8:
#         print(f"Parol juda qisqa:{parol}")
#     elif parol.isalpha():
#         print(f"Kuchsiz parol: {parol}")
#     else:
#         print(f"Kuchli parol: {parol}")
#
#
#
# # №3
# haroratlar = [20, 22, 19, 24, 25, 23, 21]
# kunlar = ["Dushnba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# ortacha_harorat = sum(haroratlar)/len(haroratlar)
# print(ortacha_harorat)
# for kunlar,havo in zip(kunlar, haroratlar):
#      if havo >= 22:
#          print(f"Iliq kun: {kunlar} {havo}°")
#      else:
#          print(f"Salqin kun: {kunlar} {havo}° ")
#
#
#
# # №4
taomlar = ["Osh", "Shashlik", "Manti","Lag’mon" ]
ovqat = input("Nima ovqat yeysiz?>>>")
if ovqat.title() in taomlar:
        print(f"Buyurtmangiz qabul qilindi")
else:
        print(f"Kechirasiz, bunday taom yo'q")



# # №5
# yosh = [16, 21, 17, 30, 25]
# odamlar = ["Farrux", "Eldar", "Atabek", "Nurislom", "Suhrob" ]
# for odamlar,a in zip(odamlar,yosh):
#      if a < 18 :
#          print( f"Yosh chegarasiga yetmagan: {odamlar}")
#      else:
#          print(f"Xush kelibsiz: {odamlar}")
#
#
#
# # №6
# xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for xabar in xabarlar:
#     if xabar == "Batareya past":
#         print("Telefoningizni quvvatlang")
#
#



# №7
fayllar = [ "kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musicalar = [ ]
rasmlar = [ ]
for data in fayllar:
     if "jpg" in data:
         rasmlar.append(data)
     if "mp3" in data:
         musicalar.append(data)
print("Rasmlar:",rasmlar)
print("Musicalar:",musicalar)