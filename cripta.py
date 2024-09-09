
from tkinter import *
from tkinter import messagebox as mb
import requests
import json
from tkinter import ttk


def exchange():
    code=combobox.get()

    if  code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD") # потом ввести код Дениса Голикова
            response.raise_for_status() # работа с исключениями
            data = response.json()
            if code in data ["rates"]:
                exchange_rate = data['rates'][code]
                mb.showinfo("Курс обмена"), (f"Курс:{exchange_rate:.2f}{code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта{code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка",  f"Произошла ошибка: {e}")
    else:
        mb.showwarning ("Внимание", f"Введите код валюты")




# делаем окно
window = Tk()
window.title ("Курс обмерна валют") # Потом поменять на "Курс криптовалют"
window.geometry("360x300")

Label(text= "Выберите код валюты").pack(padx=10, pady=10) # потом изменить на "введите код криптовалюты"
cur = ["RUB","EUR","GBP","JPY","CNY","KZT","CHF","AED"] # потом сюда вставить название крипты
combobox =ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Полчить курс обмена к доллару", command=exchange).pack(padx=10, pady=10) # потом поставить функцию Дениса Голикова по крипте

window.mainloop()



