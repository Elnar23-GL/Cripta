import requests
import json
import pprint
from tkinter import messagebox as mb, Label





# делаем окно
window = Tk()
window.title ("Курс обмерна валют") # Потом поменять на "Курс криптовалют"
window.geometry("360x300")

Label(text= "Введите код валюты").pack(padx=10, pady=10) # потом изменить на "введите код криптовалюты"

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Полчить курс обмена к доллару", command=exchange).pack(padx=10, pady=10) # потом поставить функцию Дениса Голикова по крипте

window.mainloop()



result = requests.get("https://open.er-api.com/v6/latest/USD")  #https://api.coingecko.com/api/v3/simple/price
data = json.loads(result.text) # данные в строчку
p = pprint.PrettyPrinter(indent=4) #  pprint красиво делает с 4 отступа для красоты

p.pprint (data)