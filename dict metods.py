# clear()
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
}
dasturchilar.clear()
print(dasturchilar)



car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'narh':13000,
    'km':50000,
    'korobka':'avtomat'
}
car.clear()
print(car)


telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro',
        'orif':'nokia 3310',
         'hamida': 'galaxy s9',
    'maryam': 'huawei p30',
    'tohir': 'iphone x',
    'umar': 'iphone x'
}
telefonlar.clear()
print(telefonlar)



# copy()
telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro',
        'orif':'nokia 3310',
         'hamida': 'galaxy s9',
    'maryam': 'huawei p30',
    'tohir': 'iphone x',
    'umar': 'iphone x'
}
x = telefonlar.copy()
print(x)



car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'narh':13000,
    'km':50000,
    'korobka':'avtomat'
}
x = car.copy()
print(x)



dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
}
x = dasturchilar.copy()
print(x)



#fromkeys()
a = ("a", "b", "c")
b = 25
c = dict.fromkeys(a,b)
print(c)


a = ("a", "b", "c")

c = dict.fromkeys(a)
print(c)


a = ("a", "b", "c")
b = ('how','are','you')
c = dict.fromkeys(a,b)
print(c)



# get()
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
}
x = dasturchilar.get('vali',)
print(x)


car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'narh':13000,
    'km':50000,
    'korobka':'avtomat'
}

x = car.get('price')
print(x)    #none


car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}

x = car.get('narh',13000)
print(x)



# items()
car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}

x = car.items()
print(x)


car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}

x = car.items()
car['yil'] = 2020
print(x)



dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],

}
x = dasturchilar.items()
dasturchilar['ali'] = 'java','c#'
print(x)



# keys()
car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}

print(car.keys())



car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}
x = car.keys()
car['price'] = 12000
print(x)



telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro',
        'orif':'nokia 3310'
}
print(telefonlar.keys())



# pop()
telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
telefonlar.pop('olim')
print(telefonlar)



car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}

car.pop('rang')
print(car)



car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}
print(car.pop('model'))



# popitem()
telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
telefonlar.popitem()
print(telefonlar)



telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
print(telefonlar.popitem())



car = {
    'model':'lacetti' ,
    'rang':'oq',
    'yil':2018,
    'km':50000,
    'korobka':'avtomat'
}

car.popitem()
print(car)



# setdefault()
telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
telefonlar.setdefault('umar','samsung s21')
print(telefonlar)




telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
telefonlar.setdefault('vali','samsung s21')
print(telefonlar)



telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
print(telefonlar.setdefault('ali','samsung s21'))



# update()
telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
telefonlar.update({'ali':'iphone 11'})
print(telefonlar)



telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
telefonlar.update({'umar':'mi 12pro'})
print(telefonlar)



telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
telefonlar.update({'ali':'iphone x'})
print(telefonlar)



# values()
telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}

print(telefonlar.values())



telefonlar = {
        'ali':'iphone x',
        'vali' : 'galaxy s9',
        'olim':'mi 10 pro'
}
x = telefonlar.values()
telefonlar['ali'] = 'iphone 11pro'
print(x)



dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],

}

print(dasturchilar.values())