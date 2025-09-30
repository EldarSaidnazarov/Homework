class Shaxs:
    def __init__(self,ism,familiya,yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yoshda"
class Talaba(Shaxs):
    __talaba_son = 0
    def __init__(self,ism,familiya,yosh, id):
        super().__init__(ism,familiya,yosh)
        self.id = id
        self.fanlar = []
        Talaba.__talaba_son +=1

    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        print(f"{self.ism} {fan.nomi} fanga yozildi")

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f"{fan.nomi} fani ro'yxatdan o'chirildi")
        else:
            print("Siz bu fanga yozilmagansiz")
    @classmethod
    def get_num_talaba(cls):
        return cls.__talaba_son

    def get_info(self):
        fanlar_nomi = ", ".join([fan.nomi for fan in self.fanlar]) if self.fanlar else "Hali fan yo'q"
        return f"Talaba: {self.ism} {self.familiya}, {self.yosh} yoshda, ID: {self.id}, Fanlar: {fanlar_nomi}"

class Fan:
    __fan_soni = 0

    def __init__(self, nomi):
        self.nomi = nomi
        Fan.__fan_soni +=1
    @classmethod
    def get_fan_soni(cls):
        return cls.__fan_soni

    def __repr__(self):
            return self.nomi

class Professor(Shaxs):
    def __init__(self, ism, familiya, yosh, kafedra):
        super().__init__(ism, familiya, yosh)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {self.ism} {self.familiya}, {self.yosh} yoshda, kafedra: {self.kafedra}"

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, login):
        super().__init__(ism, familiya, yosh)
        self.login = login

    def get_info(self):
        return f"Foydalanuvchi: {self.ism} {self.familiya}, login: {self.login}"


class Admin(Foydalanuvchi):
    def ban_user(self, foydalanuvchi):
                print(f"Foydalanuvchi {foydalanuvchi.ism} bloklandi")

    def get_info(self):
        return f"Admin: {self.ism} {self.familiya}, login: {self.login}"

matematika = Fan("Matematika")
fizika = Fan("Fizika")
ingliz_tili = Fan("Ingliz tili")


talaba1 = Talaba("Eldar", "Saidnazarov", 20, "F010")
talaba2 = Talaba("Ali","Sherov",20,"F020")
print(talaba1.get_info())

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)
print(talaba1.get_info())


talaba1.remove_fan(ingliz_tili)
talaba1.remove_fan(fizika)
print(talaba1.get_info())


prof1 = Professor("Olim", "Karimov", 50, "Fizika")
print(prof1.get_info())

user1 = Foydalanuvchi("Aziz", "Sodiqov", 25, "aziz25")
print(user1.get_info())

admin1 = Admin("Rustam", "Aliyev", 30, "admin_rustam")
print(admin1.get_info())
admin1.ban_user(user1)
print(Talaba.get_num_talaba())
print(Fan.get_fan_soni())