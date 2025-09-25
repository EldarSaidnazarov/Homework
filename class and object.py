# # class
# class User:
#     def __init__(self,ism,foydalanuvchi_ismi,parol , email):
#         self.name = ism
#         self.username = foydalanuvchi_ismi
#         self.pochta = email
#         self.parol = parol
#         self.kurs = 3
#     def get_name(self):
#         print(self.name)
#     def get_username(self):
#         print(self.username)
#     def get_password(self):
#         print(self.parol)
#     def update_kurs(self):
#         self.kurs+=1
#     def get_info(self):
#         print(f"{self.name} {self.username} {self.parol} {self.pochta}, {self.kurs}-kurs")
#
# user1 = User("Eldar","GHOST","QWERTY","Eldar@mail.com")
# user2 = User("Asror","Overlord","QWERT","Asror@mail.com")
# user1.get_info()
# user2.get_info()




# object
class Avto:
    def __init__(self, model, rang, korobka, narh, yil, kilometer=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil
        self.kilometer = kilometer
    def get_info(self):
        return(f"Model: {self.model}, Rang: {self.rang}, "
        f"Korobka: {self.korobka}, Narh: {self.narh}$, "
        f"Yil: {self.yil}, Yurgan: {self.kilometer} km")


    def update_km(self,kilometer):
        self.kilometer = kilometer

avto1 = Avto("Toyota Camry", "oq", "avtomat", 25000, 2022)
avto2 = Avto("Chevrolet Malibu", "qora", "avtomat", 22000, 2021)
avto3 = Avto("Kia K5", "kulrang", "mexanik", 21000, 2023)


class Avtosalon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []

    def add_avto(self, avto):
        if isinstance(avto, Avto):
            self.avtolar.append(avto)
        else:
            print("Faqat Avto klassiga oid obyektlarni qo‘shish mumkin!")

    def get_avtolar(self):
        if self.avtolar:
            for avto in self.avtolar:
                print(avto.get_info())
        else:
            print("Sotuvda hozircha avtomobillar yo'q.")



salon = Avtosalon("Avto UZ", "Toshkent sh.")
salon.add_avto(avto1)
salon.add_avto(avto2)
salon.add_avto(avto3)
avto1.update_km(150)
avto2.update_km(200)
avto3.update_km(100)
salon.get_avtolar()

print(dir(avto1))
print(dir(avto2))
print(dir(str))
print(dir(int))

