# №1
# def user_data(ism,familiya,yosh):
#     print(f"Ism: {ism.title()}\n"
#           f"Familiya : {familiya.title()}\n"
#           f"Yosh : {yosh}")
# user_data(input("ism: "),input("familiya: "),int(input("yosh: ")))



# №2
# def find_max(a , b , c):
#     max_son = max(a,b,c)
#     son = []
#     if a == max_son:
#         son.append("A")
#     if b == max_son:
#         son.append("B")
#     if c == max_son:
#         son.append("C")
#
#
#     print(f"Eng katta son - {' va '.join(son)} = {max_son}")
# a = int(input("A son: "))
# b = int(input("B son: "))
# c = int(input("C son: "))
#
#
# find_max(a,b,c)



# №3
# def find_letter_count(word,letter):
#     find = word.count(letter)
#     print(f"{word} so'zida {letter} dan {find} ta")
# word = input("So'z kiriting: ")
# letter = input("Qidirgan harfni kiriting: ")
# find_letter_count(word,letter)



# №4
# def list_sum(myList):
#     summa = sum(myList)
#     print(f"Listni yigindisi: {summa}")
#
#
# list_sum([5,7,10,6,4])



# №5
# def daraja(a,b):
#     print(f"{a} ning darajasi-{b} = {a**b}")
# daraja(4,2)



# №6
# def daraja(a,b,c,d):
#     print(f"{a}-ning darajasi-{b} = {a**b}\n"
#           f"{a}-ning darajasi-{c} = {a**c}\n"
#           f"{a}-ning darajasi-{d} = {a**d}")
#
# daraja(4,1,2,3)


# №7
# def digit_count_and_sum(word):
#     digit = [int(num) for num in word if num.isdigit()]
#     print(f"Raqamlar soni = {len(digit)}")
#     print(f"Raqamlar yigindisi = {sum(digit)}")
# digit_count_and_sum("23abc456")



# №8
# def add_right(a,b):
#     sum = int(b+a)
#     print(sum)
# add_right(12,8)



# №9
# def add_right(a,b):
#     sum = a+b
#     print(sum)
# add_right('sa','lom')



# №10
# def work_with_list(a):
#     minimum = min(a)
#     list = [x * minimum for x in a]
#     print(list)
#
# work_with_list([6,10,12])



# №11
# def big_sales(sales):
#     max_sales = max(sales, key=sales.get)
#     return max_sales
#
#
# sales = {
#     "yanvar": 12000,
#      "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
# print(big_sales(sales))



# №12
# def min_max(numbers, max_num, min_num):
#     minimum = max_num == max(numbers)
#     maximum = min_num == min(numbers)
#     return maximum , minimum
# numbers = [1,2,4,6,9]
# print(min_max(numbers,8,1))



# №13
# def expensiveProduct(products):
#     telefon = max(products, key=lambda p: p["price"])
#     return telefon["name"]
# products = [
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100}
# ]
# print(expensiveProduct(products))


