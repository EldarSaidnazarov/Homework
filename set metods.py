# add()
fruits = {'banana', 'apple', 'orange'}
fruits.add('cherry')
print(fruits)



car = {'chevrolet','porsche','mercedes'}
car.add('bmw')
print(car)



car = {'chevrolet','porsche','mercedes'}
print(car.add('bmw'))  #None



# clear()
fruits = {'banana', 'apple', 'orange'}
fruits.clear()
print(fruits)



fruits = {'banana', 'apple', 'orange'}
print(fruits.clear()) #None



car = {'chevrolet','porsche','mercedes'}
car.clear()
print(car)



# copy()
fruits = {'banana', 'apple', 'orange'}
print(fruits.copy())


car = {'chevrolet','porsche','mercedes'}
print(car.copy())


country = {'Uzbekistan', 'USA', 'Rossiya'}
print(country.copy())



# difference()
a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'ban'}
print(a.difference(b))


a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'ban'}
print(a-b)


a = {'chevrolet','porsche','mercedes'}
b = {'bmw', 'mercedes', 'chevrolet'}
print(a.difference(b))



# difference update()
a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'ban'}
a.difference_update(b)
print(a)


a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'ban'}
a -= b
print(a)


a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'ban'}
c = {'bmw', 'apple', 'banana'}
a -= b | c
print(a)



# discard()
a = {1, 2 ,3}
a.discard(2)
a.discard(10)
print(a)


a = {'banana', 'apple', 'orange'}
a.discard('banana')
a.discard('cherry')
print(a)


b = {'bmw', 'mercedes', 'chevrolet'}
b.discard('lacetti')
print(b)



# intersection()
a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'banana'}
print(a.intersection(b))


a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
c = {'c', 'f', 'g'}
print(a & b & c)


a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
c = {'c', 'f', 'g'}
print(a.intersection(b,c))



# intersection update()
a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'banana'}
a.intersection_update(b)
print(a)


a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
c = {'c', 'f', 'g'}
a &= b & c
print(a)


a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
c = {'c', 'f', 'g'}
a.intersection_update(b,c)
print(a)



# isdisjoint()
a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'banana'}
print(a.isdisjoint(b))


a = {'banana', 'apple', 'orange'}
b = {'bmw', 'mercedes', 'chevrolet'}
print(a.isdisjoint(b))


a = {1, 2, 3}
b = {4, 5, 6}
c = a.isdisjoint(b)
print(c)



# issubset()
a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}
print(a.issubset(b))


a = {1, 2, 3}
b = {3, 4, 5}
print(a.issubset(b))


a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}
print(a <= b)



# issuperset()
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
print(a.issuperset(b))


a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
print(a >= b)


a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}
print(a.issuperset(b))



# pop()
fruits = {'banana', 'apple', 'orange'}
fruits.pop()
print(fruits)


fruits = {'banana', 'apple', 'orange'}
print(fruits.pop())


car = {'chevrolet','porsche','mercedes'}
print(car.pop())



# remove()
fruits = {'banana', 'apple', 'orange'}
fruits.remove('apple')
print(fruits)


a = {1, 2, 3}
a.remove(2)
print(a)


b = {'bmw', 'mercedes', 'chevrolet'}
b.remove('chevrolet')
print(b)



# symmetric difference()
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
print(a.symmetric_difference(b))


a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
print(a ^ b)


a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'banana'}
print(a.symmetric_difference(b))



# symmetric difference update()
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
a.symmetric_difference_update(b)
print(a)


a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
a ^= (b)
print(a)


a = {'banana', 'apple', 'orange'}
b = {'data', 'apple', 'banana'}
a.symmetric_difference_update(b)
print(a)



# union()
a = {'banana', 'apple', 'orange'}
b = {'bmw', 'mercedes', 'chevrolet'}
print(a.union(b))


a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
print(a | b)


a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
c = {'c', 'f', 'g'}
print(a | b | c)



# update()
a = {'banana', 'apple', 'orange'}
b = {'bmw', 'mercedes', 'chevrolet'}
a.update(b)
print(a)


a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
a |= b
print(a)


a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
c = {'c', 'f', 'g'}
a |= b | c
print(a)

