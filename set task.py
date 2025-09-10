# # №1
# from distutils.command.install import value
#
# lugat = {
#     'Boolean': 'Mantiqiy qiymat',
#     'Float':"O'nlok son",
#     "For": "Biror amalni qayta-qayta bajarish tsikli",
#     "If": "Shartlarni tekshirish operatori",
#     "Integer": "Butun son",
#     "String": "Matn tipi",
#     "List": "Ro'yxat",
#     "Dict": "Kalit-qiymat juftliklari to'plami",
#     "Tuple": "O'zgarmas ro'yxat",
#     "Set": "Unikal elementlar to'plami"
# }
#
# for key,value in sorted(lugat.items()):
#     print(f"{key} - {value}")
#
#
#
# # №2
# davlatlar = {
#     "AQSH": "Washington D.C.",
#     "ITALIYA": "Rim",
#     "MALAYZIYA": "Kuala-Lumpur",
#     "O'ZBEKISTON": "Toshkent",
#     "QIRG'IZISTON": "Bishkek",
#     "QOZOG'ISTON": "Nursulton",
#     "ROSSIYA": "Moskva",
#     "SINGAPUR": "Sungapur",
#     "TOJIKISTON": "Dushanbe"
# }
# print("\nDavlatlar:")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat)
#
# print('\nPoytaxtlari:')
# for potaxt in sorted(davlatlar.values()):
#     print(potaxt)
#
#
#
#
# # №3
# davlatlar = {
#     "AQSH": "Washington D.C.",
#     "ITALIYA": "Rim",
#     "MALAYZIYA": "Kuala-Lumpur",
#     "O'ZBEKISTON": "Toshkent",
#     "QIRG'IZISTON": "Bishkek",
#     "QOZOG'ISTON": "Nursulton",
#     "ROSSIYA": "Moskva",
#     "SINGAPUR": "Sungapur",
#     "TOJIKISTON": "Dushanbe"
# }
# print(davlatlar)
# davlat = input('Qaysi davlatning,poytaxtini bilishni istaysiz?:').upper()
# if davlat in davlatlar:
#     print(f'{davlat}ning poytaxti {davlatlar[davlat]} shahri')
# else:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
#
#
#
# # №4
# sevimli_filmlar = {
#     "Alining": ["Terminator", "Rambo", "Titanic"],
#     "Valining": ["Tenet", "Inception", "Interstellar"],
#     "Hasanning": ["Abdullajon", "Bomba", "Shaytanat"],
#     "Husanning": ["Mahallada duv-duv gap", "John Wick"]
# }
#
# for ism, filmlar in sevimli_filmlar.items():
#     print(f"\n{ism} sevimli kinolari:")
#     for film in filmlar:
#         print(film)
#
#
#
#
# # №5
davlatlar = {
    "O'zbekiston": {
        "poytaxt": "Toshkent",
        "hududi": 448978,
        "aholisi": 33000000,
        "pul_birligi": "so'm"
    },
    "Rossiya": {
        "poytaxt": "Moskva",
        "hududi": 17098246,
        "aholisi": 144000000,
        "pul_birligi": "rubl"
    },
    "AQSH": {
        "poytaxt": "Vashington",
        "hududi": 9631418,
        "aholisi": 327000000,
        "pul_birligi": "dollar"
    },
    "Malayziya": {
        "poytaxt": "Kuala-Lumpur",
        "hududi": 329750,
        "aholisi": 25000000,
        "pul_birligi": "rinngit"
    }
}

for davlat, info in davlatlar.items():
    print(f"\n{davlat}ning poytaxti {info['poytaxt']}")
    print(f"Hududi: {info['hududi']} kv.km")
    print(f"Aholisi: {info['aholisi']}")
    print(f"Pul birligi: {info['pul_birligi']}")

