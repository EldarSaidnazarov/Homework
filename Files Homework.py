with open('data/pi_million_digits.txt') as file:
    pi = file.read().replace('\n','').strip()
    birthday = '09437027'
    find = pi.find(birthday)
    if find != -1:
        print(f"Дата {birthday} найдена в числе pi на позиции {find}")
    else:
        print(f"Дата {birthday} не найдена в числе pi")

import pickle
pi_float = float(pi[:100])
with open('pi_float', 'wb') as f:
    pickle.dump(pi_float, f)
    print("Число pi сохранено в формате float с помощью pickle.")

# Проверка: загрузи число из pickle и выведи
with open('pi_float', 'rb') as f:
    loaded_pi = pickle.load(f)
    print("Загруженное число pi из файла:", loaded_pi)