import requests
from bs4 import BeautifulSoup

link = "https://www.w3schools.com/python/python_virtualenv.asp"
a = requests.get(link)

soup = BeautifulSoup(a.text,"html.parser")
book = soup.find_all(class_="w3-col l10 m12 ")
print(book[0].text)





url = "https://kinogo.ec/55075-dzhon-uik-4-2023.html"
b = requests.get(url)

soup = BeautifulSoup(b.text,"html.parser")
film = soup.find_all(class_="fullstory__title")
print(film[0].text)