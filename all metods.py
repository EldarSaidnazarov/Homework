# capitalize()
from Tools.demo.spreadsheet import ljust, rjust, translate

text = "hello python!"
print(text.capitalize()) # Hello python!

text = "my name is Eldar"
print(text.capitalize())  # My name is eldar

text = "20 IS MY AGE"
print(text.capitalize())  # 20 is my age



# casefold()
num = "HELLO WORLD!"
print(num.casefold()) # hello word!

num = "MY NAME IS ELDAR"
print(num.casefold()) # my name is eldar

num = "I LOVE PYTHON"
print(num.casefold()) # i love python



# center()
lab = "Good"
x = lab.center(10, "-")
print(x) # ---Good---

lab = "Happy birthday"
print(lab.center(20,'!'))  # !!!Happy birthday!!!

lab = "№1"
print(lab.center(10, ">"))



# count()
gap = "I'm doing homework today"
print(gap.count("o",))  # 4

gap = "My grandfather is a kind and helpful gentleman"
print(gap.count("a", 10,50)) # 3

gap = "one of the most important thing to some people is wealth                                                                                                                                      "
print(gap.count("o",0,30)) # 4



# encode()
a = "Hello World!"
b = a.encode()
print(b)  # b'Hello World'

a = "My имя is Eldar"
print(a.encode())

c = "Моё name Eldar"
print(c.encode(encoding="ascii",errors="backslashreplace"))
print(c.encode(encoding="ascii",errors="ignore"))
print(c.encode(encoding="ascii",errors="namereplace"))
print(c.encode(encoding="ascii",errors="replace"))
print(c.encode(encoding="ascii",errors="xmlcharrefreplace"))



# endwith()
txt = "Hello Eldar!"
print(txt.endswith("!"))

txt = "Hello, welcome to my home."
print(txt.endswith("my home.",5,15))

txt = 'Hello, welcome to my home.'
b = txt.endswith(("welcome","my home."))
print(b)



# expandtabs()
txt = "H\ti"
print(txt.expandtabs(3))

txt = "S\ta\tl\to\tm"
print(txt.expandtabs())

txt = "E\tl\td\ta\tr"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(4))



# find()
txt = "Salom Eldar"
print(txt.find("Eldar"))

txt = "Salom Eldar"
print(txt.find("Hi"))

txt = "Hello have a good day"
print(txt.find("o",5,20))



# format()
txt = "This T-shirt {price:.2f} dolldars"
print(txt.format(price = 15))

txt = "My name is {name}, I'm {age}".format(name="Eldar",age=20)
print(txt)

txt = "My name is {}, I'm {}".format("Eldar",20)
print(txt)



# format_map()
txt = "Name: {name} ; Age: {age}"
print(txt.format_map({'name': 'Eldar', 'age': 20}))

txt = "T-shirt: {color} ; Price: {how much?}"
print(txt.format_map({'color':'White' , 'how much?': '10 dollars'}))

txt = "Country: {for} , City: {do}".format_map({'for':'Uzbekistan','do':'KHIVA'})
print(txt)



# index()
num = "Hello have a good day"
print(num.index("good"))

num2 = "Hello have a good day"
print(num2.index("o",5,20))

num3 = "Hello have a good day"
print(num3.find("q"))   # find = -1
# print(num3.index('q'))   # index = Hato beradi



# isalnum()
txt = "Xorazm90"
print(txt.isalnum())

txt = "Xorazm 90"
print(txt.isalnum())

txt = "90Xorazm"
print(txt.isalnum())



# isalpha()
txt = "Xorazm"
print(txt.isalpha())

txt = "Xorazm90"
print(txt.isalpha())

txt = "Xorazm 90"
print(txt.isalpha())



# isascii()
txt = "Hi"
print(txt.isascii())

txt = "Привет"
print(txt.isascii())

txt = "123"
print(txt.isascii())



# isdecimal()
num = "123"
print(num.isdecimal())

num = ("12.8")
print(num.isdecimal())

num = ("12.8i")
print(num.isdecimal())



# isdigit()
num = "10800"
print(num.isdigit())

num = "Hello"
print(num.isdigit())

num = "123Salom"
print(num.isdigit())



# isidentifier()
txt = "Eldar"
print(txt.isidentifier())

txt = "num 1"
print(txt.isidentifier())  # false num 1 da probel bor

txt = "1num"
print(txt.isidentifier()) # false oldida son bomaslik mumkin



# islower()
txt = "Salom Eldar"
print(txt.islower())

txt = "salom eldar"
print(txt.islower())

txt = "123salome eldar"
print(txt.islower())



# isnumeric()
num = "456"
print(num.isnumeric())

num = "456Hi"
print(num.isnumeric())

num = "-12"
print(num.isnumeric())



# isprintable()
txt = "Hello my name is Eldar"
print(txt.isprintable())

txt = "Hello I'm 20"
print(txt.isprintable())

txt = "Hello \tI'm 20"
print(txt.isprintable())



# isspace()
txt = "   "
print(txt.isspace())

txt = "  !  "
print(txt.isspace())

txt = "  \t  \n"
print(txt.isspace())



# istitle()
txt = "Hello Python"
print(txt.istitle())

txt = "hello python"
print(txt.istitle())

txt = "HELLO PYTHON"
print(txt.istitle())



# isupper()
txt = "Hello Python"
print(txt.isupper())

txt = "hello python456"
print(txt.isupper())

txt = "HELLO PYTHON"
print(txt.isupper())



# join()
words = ("one", "two", "three")
print("-".join(words))

words = ("1", "2", "3")
print("+".join(words))

a = {"name" : "Eldar" , "country": "Uzbekistan"}
b = "Xorazm"
c = b.join(a)
print(c)



# ljust()
txt = "apple"
a = txt.ljust(10)
print(a,"is fruit")

txt = "name:"
print(txt.ljust(10,"0"))

txt = "cat"
print(txt.ljust(5,"."))



# lower()
txt = "HELLO"
print(txt.lower())

txt = "Hello"
print(txt.lower())

txt = "hello"
print(txt.lower())



# lstrip()
a = "      Salom"
print(a.lstrip())

a = "            20 yoshda man"
print("Men" , a.lstrip())

a = ",,,,,,asdr....Salom"
b = a.lstrip(",asdr.")
print(b)



# maketrans()
txt = "Salom Elyar"
b = str.maketrans("y","d")
print(txt.translate(b))

txt = "Hello word good day!"
a = "day"
b = "san"
c = "hello word"
d = str.maketrans(a , b , c)
print(txt.translate(d))

txt = "Hello word good day"
a = "day"
b = "sun"
c = "ello"
print(str.maketrans(a,b,c))



# partition()
a = "Python the best"
print(a.partition("the"))

b = "I am from Uzbekistan"
print(a.partition("from"))

c = "Where are you from?"
print(c.partition("are"))



# replace()
a = "Java the best"
print(a.replace("Java","Python"))

b = "Hello word!"
print(b.replace("l","x"))

c = "Small car"
print(c.replace("Small","Big"))



# rfind()
txt = "Hello world!"
print(txt.rfind("world"))

txt = "Hello world!"
print(txt.rfind("q"))

txt = "Hello how are you have a good day!"
print(txt.rfind("0",5,20))



# rindex()
txt = "Hello world!"
print(txt.rindex("world"))

txt = "Hello world!"
print(txt.rindex("o",4,20))

txt = "Hello how are you have a good day!"
print(txt.rfind("q"))  # -1



# rjust()
a = "20"
print(a.rjust(5,"1"))

b = "banana"
print(b.rjust(20,"!"))

c = "Job"
print(c.rjust(20))



# rpartition()
num = "apple-banana-cherry"
print(num.rpartition("-"))

num2 = "I go to work, I'm working"
print(num2.rpartition("work"))

num3 = "Hello wold!"
print(num3.rpartition("o"))



# rsplit()
txt = "apple, banana, cherry"
print(txt.rsplit(", "))

txt = "a, b, c ,d"
print(txt.rsplit(",",2))

txt = "a, c, d, b, f "
print(txt.rsplit(",",2))



# rstrip()
txt = "Hello Python           "
print(txt.rstrip())


txt = "Test.py........"
print(txt.rstrip("."))

txt = "     Eldar     "
b = txt.rstrip()
print("Hello my name is", b, "nice too meet you")



# split()
num = "a b c"
print(num.split())


num2 = "apple,banana,cherry"
print(num2.split(",", 1))

num3 = "Hello Python, how are you"
print(num3.split(", "))



# splitlines()
num = "Line1\nLine2\nLine3"
print(num.splitlines())

num = "Hello have\na good day"
print(num.splitlines(True))

num = "Hello have\na good day"
print(num.splitlines())



# startswith()
txt = "Hello world"
print(txt.startswith("world"))

txt = "Hello world"
print(txt.startswith("Hello"))

txt = "Hello, welcome to my world."
print(txt.startswith("lo" , 3, 20))



# strip()
a = "  how  "
b = a.strip()
print("Hello "+b+" are  you" )


a = "sdf...hello...fgd"
print(a.strip(".sfdg"))

a = "...hello..."
print(a.strip("."))



# swapcase()
a = "Hello Eldar"
print(a.swapcase())

b = "hELLO eLDAR"
print(b.swapcase())

c = "good day!"
print(c.swapcase())



# title()
a = "hello python"
print(a.title())

a = "hello have a gOOD dAY!"
print(a.title())

a = "nICE 1c1c1c"
print(a.title())



# translate()
txt = "hello world"
table = str.maketrans({'h': 'H', 'w': 'W'})
result = txt.translate(table)
print(result)

txt = "Hello Eldar"
b = str.maketrans({"d":"y"})
c = txt.translate(b)
print(c)

a = "Hello Dython"
b = str.maketrans("D", "P")
print(a.translate(b))



# upper()
a = "Hello Python"
print(a.upper())

b = "hello"
print(b.upper())

c = "salome"
print(c.upper())



# zfill()
a = "10"
print(a.zfill(5))

b = "HI"
print(b.zfill(10))

c = "Hello to my home"
print(c.zfill(5))

