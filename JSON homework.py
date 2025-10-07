import json

data = {
    "Model": "Malibu",
    "Rang": "Qora",
    "Yil": 2020,
    "Narh": 40000
}

data_json = json.dumps(data)
print(data_json)

with open("data.json", "w") as file1:
    json.dump(data, file1)

# Читаем данные из файла data.json обратно в словарь
with open("data.json", "r") as file1:
    salom = json.load(file1)
print(salom)


talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

# Преобразуем JSON-строку в словарь
talaba_dict = json.loads(talaba_json)
ism = talaba_dict["ism"]
familiya = talaba_dict["familiya"]
print(ism, familiya)

# Записываем словарь talaba_dict в файл talaba.json
with open("talaba.json", "w") as file2:
    json.dump(talaba_dict, file2)

# Читаем данные из файла talaba.json обратно в словарь
with open("talaba.json", "r") as file2:
    salom2 = json.load(file2)
print(salom2)
