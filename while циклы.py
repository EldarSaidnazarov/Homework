# №1
while True :
    a = input('svetavor qaysi rangda: ').lower()
    if a=="qizil" or a=="sariq" or a=="yashil":
        print("rahmat, to’g’ri keladi")
        break
    else:
        print("bu xato rang")



# №2
import random
rand = random.randint(1,10)
while True:
    son = int(input("1 dan 10 gacha bo'lgan sonni toping: "))
    if son == rand :
        print("Tabriklaymiz, siz topdingiz!")
        break
    elif son > rand:
        print("Biz o'ylagan son siz o'ylagan sondan kichik")
    elif son < rand:
        print("Biz o'ylagan son siz o'ylagan sondan katta")
    else:
        print("Noto'g'ri, qayta urinib ko'ring")



# №3
ismlar = []
while True:
    ism = input("Do'stingiz ismini kiriting (stop-tugatish): ").strip()
    if ism.lower() == 'stop' :
        break
    ismlar.append(ism)

print(f"\nDo'stlaringiz ro'yxati:")
for ism in ismlar:
    print(f'{ism}')



# №4
USD_kurs = 12600

while True:
    summa = input("So'm miqdorini kiriting (yoki 'exit' tugatish uchun): ").strip()
    if summa.lower() == 'exit':
        print("Dastur to'xtatildi.")
        break
    elif summa.isdigit():
        som = int(summa)
        dollar = som/USD_kurs
        print(f"{som}so'm = {dollar:.2f} USD")
    else:
        print("Iltimos, to'g'ri son kiriting.")
