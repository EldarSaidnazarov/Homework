# append()
cars = ["BMW", "Mercedes"]
cars.append("Porche")
print(cars)

fruits = ["apple", "grapefruit"]
fruits.append("banana")
print(fruits)

phones = ["Iphone", "Samsung"]
phones.append("Redmi")
print(phones)



# clear()
cars = ["BMW", "Mercedes", "Porche"]
cars.clear()
print(cars)

phones = ["Iphone", "Samsung", "Redmi"]
phones.clear()
print(phones)

fruits = ["apple", "grapefruit", "banana"]
fruits.clear()
print(fruits)



# copy()
fruits = ["apple", "banana"]
new_fruits = fruits.copy()
print(new_fruits)

cars = ["BMW", "Mercedes", "Porche"]
new_cars = cars.copy()
print(new_cars)

phones = ["Iphone", "Samsung", "Redmi"]
new_phones = phones.copy()
print(new_phones)



# count()
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))

cars = ["BMW", "Mercedes", "Porche"]
print(cars.count("BMW"))

fruits = ["banana", "cherry", "apple", "banana"]
print(fruits.count("banana"))



# extend()
num = [1, 2, 3]
num2 = [4, 5, 6]
num.extend(num2)
print(num)

fruits = ["banana", "apple", "mango"]
more_fruits = ["cherry", "strawberry", "blueberry"]
fruits.extend(more_fruits)
print(fruits)

cars = ["BMW", "Porche"]
more_cars = ["Mercedes", "Volvo"]
cars.extend(more_cars)
print(cars)



# index()
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))

num = [12, 24 ,36 ,48 ,60]
print(num.index(36))

fruits = ["apple", "banana", "cherry"]
print(fruits.index("cherry",1))



# insert()
cars = ["BMW", "Porche"]
cars.insert(1,"Mercedes")
print(cars)

num = [1, 2, 3]
num.insert(3,4)
print(num)

fruits = ["apple", "cherry"]
fruits.insert(2,"banana")
print(fruits)



# pop()
fruits = ["banana", "apple", "mango"]
fruits.pop(1)
print(fruits)

fruits = ["banana", "apple", "mango"]
x = fruits.pop(1)
print(x)

num = [1, 2 , 3, 3]
x = num.pop(2)
print(num)



# remove()
fruits = ["banana", "apple", "mango"]
fruits.remove("apple")
print(fruits)

fruits = ["banana", "apple", "mango", "banana"]
fruits.remove("banana")
print(fruits)

num = [12, 24, 36, 48]
num.remove(24)
print(num)



# reverse()
fruits = ["banana", "apple", "mango"]
fruits.reverse()
print(fruits)

fruits = ["banana", "apple", "mango", "banana"]
fruits.reverse()
print(fruits)

num = [1, 2, 3]
num.reverse()
print(num)



# sort()
phones = ["Iphone", "Samsung", "Redmi"]
phones.sort(reverse=True)
print(phones)

num = [3,4,5,7,9,1,2]
num.sort()
print(num)

cars = ["Mercedes", "Porche", "Bmw", "Volvo"]
cars.sort()
print(cars)

