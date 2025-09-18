# import random
# seed()  Устанавливает начальное значение генератора случайных чисел.
# random.seed(100)
# print(random.random())
#
#
# random.seed(20)
# print(random.random())
# random.seed(20)
# print(random.random())


# getstate()  Возвращает внутреннее состояние генератора.
# import random
# state = random.getstate()
# print(state)
#
# x = random.getstate()
# print(x)


# setstate() Восстанавливает генератор случайных чисел в предыдущее состояние.
# random.seed(10)
# print(random.random())
# state = random.getstate()
# print(random.random())
# random.setstate(state)
# print(random.random())
#
#
# random.seed(20)
# print(random.random())
# x = random.getstate()
# print(random.random())
# random.setstate(x)
# print(random.random())


# getrandbits(k)  Возвращает целое число с (k) случайными битами.
# print(random.getrandbits(10))
#
# print(random.getrandbits(8))


# randrange()  Возвращает случайное число в диапазоне.
# print(random.randrange(0,10))
#
# print(random.randrange(0,100,5))


# randint()  Возвращает случайное целое число от a до b включительно.
# print(random.randint(0,5))

# print(random.randint(0,100))


# choice() Выбирает один случайный элемент.
# colors = ['red', 'green', 'blue']
# print(random.choice(colors))
#
# cars = ['matiz', 'spark', 'gentra']
# print(random.choice(cars))


# choices() Выбирает k элементов с возможностью повторений.
# colors = ['red', 'green', 'blue']
# print(random.choices(colors, k=3))
#
# colors = ['red', 'green', 'blue']
# print(random.choices(colors, weights=[100,10,50],  k=3))


# shuffle()  Перемешивает элементы на месте.
# num = [1, 2, 3, 4, 5]
# random.shuffle(num)
# print(num)
#
#
# colors = ['red', 'green', 'blue']
# random.shuffle(colors)
# print(colors)


# sample()  Выбирает k уникальных элементов без повторений.
# colors = ['red', 'green', 'blue']
# print(random.sample(colors, k=1))
#
#
# num = [1, 2, 3, 4, 5]
# print(random.sample(num, k=3))


# random()  Возвращает число от 0.0 до 1.0.
# print(random.random())


# uniform()  Случайное число с плавающей точкой от a до b.
# print(random.uniform(0,10))
#
# print(random.uniform(0.5,10.5))


# triangular()  Возвращает число от low до high, максимум вероятности в mode.
# print(random.triangular(10,20,15))

# print(random.triangular(20,40,60))


# betavariate()  Бета-распределение (0.0 до 1.0). Применяется в байесовской статистике.
# print(random.betavariate(2, 5))

# print(random.betavariate(5,2))


# expovariate()  Экспоненциальное распределение. lambd — обратная величина среднего.
# print(random.expovariate(1.5))

# print(random.expovariate(2.5))


# gammavariate()  Гамма-распределение.
# print(random.gammavariate(2, 3))

# print(random.gammavariate(5,7))


# gauss()  Гауссовское (нормальное) распределение.
# print(random.gauss(0, 1))

# print(random.gauss(5,6))


# lognormvariate()  Логнормальное распределение (логарифм нормально распределён).
# print(random.lognormvariate(0, 1))

# print(random.lognormvariate(2,3))


# normalvariate()  Аналог gauss(), нормальное распределение.
# print(random.normalvariate(0, 1))

# print(random.normalvariate(0, 2))


# vonmisesvariate()Распределение фон Мизеса,используется в угловой статистике (например, направления ветра).
# print(random.vonmisesvariate(0, 2))

# print(random.vonmisesvariate(0, 4))


# paretovariate()  Распределение Парето — применяется в моделировании богатства, городов и т. д.
# print(random.paretovariate(2))

# print(random.paretovariate(3))


# weibullvariate()  Распределение Вейбулла. Применяется в анализе надёжности.
# print(random.weibullvariate(1,2))

# print(random.weibullvariate(3, 4))

