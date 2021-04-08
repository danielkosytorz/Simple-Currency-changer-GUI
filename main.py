import tkinter as tk
import requests
from bs4 import BeautifulSoup

# --------------------------VARIABLES----------------------
HEIGHT = 400
WIDTH = 400

result = requests.get('https://kursy-walut.mybank.pl/')
src = result.content
soup = BeautifulSoup(src, 'html.parser')

euro_data = soup.find_all(attrs={'title':'Kurs średni EUR'})
funts_data = soup.find_all(attrs={'title':'Kurs średni GBP'})
dolars_data = soup.find_all(attrs={'title':'Kurs średni USD'})
frank_data = soup.find_all(attrs={'title':'Kurs średni CHF'})

kurs_euro = float(euro_data[0].text.replace(',','.'))
kurs_funta = float(funts_data[0].text.replace(',','.'))
kurs_dolara = float(dolars_data[0].text.replace(',','.'))
kurs_franka = float(frank_data[0].text.replace(',','.'))
# ---------------------------FUNCTIONS---------------------------
def currency_exchange_option(what_currency, for_what_currency, type):
    frame = tk.Frame(window)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_input = tk.Label(frame, text=f"{what_currency.upper()}: ")
    label_input.place(relx=0.3, rely=0.15, relwidth=0.2, relheight=0.1)

    entry_value = tk.Entry(frame)
    entry_value.place(relx=0.5, rely=0.15, relwidth=0.2, relheight=0.1)

    label_output = tk.Label(frame, text=f"{for_what_currency.upper()}: ")
    label_output.place(anchor='n', relx=0.5, rely=0.5, relwidth=0.3, relheight=0.1)

    if type == 0:
        button_convert = tk.Button(frame, text="Przelicz",  command=lambda: convert(int(entry_value.get()), type, for_what_currency, label_output))
        button_convert.place(anchor='n', relx=0.5, rely=0.3, relwidth=0.3, relheight=0.1)
    elif type == 1:
        button_convert = tk.Button(frame, text="Przelicz",  command=lambda: convert(int(entry_value.get()), type, what_currency,label_output))
        button_convert.place(anchor='n', relx=0.5, rely=0.3, relwidth=0.3, relheight=0.1)

    button_back = tk.Button(frame, text="Wroc do menu", command=lambda: frame.destroy())
    button_back.place(anchor='n', relx=0.5, rely=0.8, relheight=0.1, relwidth=0.5)


def convert(value_to_convert, convert_type, currency, label):
    currency = currency.upper()
    if currency == "EURO":
        if convert_type == 0:
            result = value_to_convert / kurs_euro
            label['text'] = f'{round(result,2)} EUR0'
        elif convert_type == 1:
            result = value_to_convert * kurs_euro
            label['text'] = f'{round(result,2)} PLN'
    elif currency == "DOLAR":
        if convert_type == 0:
            result = value_to_convert / kurs_dolara
            label['text'] = f'{round(result,2)} USD'
        else:
            result = value_to_convert * kurs_dolara
            label['text'] = f'{round(result,2)} PLN'
    elif currency == "FUNT":
        if convert_type == 0:
            result = value_to_convert / kurs_funta
            label['text'] = f'{round(result,2)} GBF'
        else:
            result = value_to_convert * kurs_funta
            label['text'] = f'{round(result,2)} PLN'
    elif currency == "FRANK":
        if convert_type == 0:
            result = value_to_convert / kurs_franka
            label['text'] = f'{round(result,2)} CHF'
        else:
            result = value_to_convert * kurs_franka
            label['text'] = f'{round(result,2)} PLN'


def menu_option_1():
    frame_option_1 = tk.Frame(window)
    frame_option_1.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_euro = tk.Label(frame_option_1, text=f"Aktualny kurs euro: {round(kurs_euro,2)}")
    label_euro.place(anchor='n', relx=0.5, rely=0.05, relheight=0.1, relwidth=1)

    label_usd = tk.Label(frame_option_1, text=f"Aktualny kurs dolara: {round(kurs_dolara,2)}")
    label_usd.place(anchor='n', relx=0.5, rely=0.2, relheight=0.1, relwidth=1)

    label_funt = tk.Label(frame_option_1, text=f"Aktualny kurs funta: {round(kurs_funta,2)}")
    label_funt.place(anchor='n', relx=0.5, rely=0.35, relheight=0.1, relwidth=1)

    label_frank = tk.Label(frame_option_1, text=f"Aktualny kurs franka szwajcarskiego: {round(kurs_franka,2)}")
    label_frank.place(anchor='n', relx=0.5, rely=0.5, relheight=0.1, relwidth=1)

    button_back = tk.Button(frame_option_1, text="Wroc do menu", command=lambda: frame_option_1.destroy())
    button_back.place(anchor='n', relx=0.5, rely=0.75, relheight=0.1, relwidth=0.5)


def menu_option_2():
    frame_option_2 = tk.Frame(window)
    frame_option_2.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_currency = tk.Label(frame_option_2, text="Wybierz walute:")
    label_currency.place(anchor='n', relx=0.5, rely=0.05, relwidth=1, relheight=0.2)

    button_euro = tk.Button(frame_option_2, text="Euro", command=lambda: currency_exchange_option("pln","euro",0))
    button_euro.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.5, relheight=0.1)

    button_dolar = tk.Button(frame_option_2, text="Dolar", command=lambda: currency_exchange_option("pln","dolar",0))
    button_dolar.place(anchor='n', relx=0.5, rely=0.37, relwidth=0.5, relheight=0.1)

    button_funt = tk.Button(frame_option_2, text="Funt", command=lambda: currency_exchange_option("pln","funt",0))
    button_funt.place(anchor='n', relx=0.5, rely=0.49, relwidth=0.5, relheight=0.1)

    button_frank = tk.Button(frame_option_2, text="Frank szwajcarski", command=lambda: currency_exchange_option("pln",
                                                                                                               "frank",0))
    button_frank.place(anchor='n', relx=0.5, rely=0.61, relwidth=0.5, relheight=0.1)

    button_back = tk.Button(frame_option_2, text="Wroc do menu", command=lambda: frame_option_2.destroy())
    button_back.place(anchor='n', relx=0.5, rely=0.8, relheight=0.1, relwidth=0.5)

def menu_option_3():
    frame_option_3 = tk.Frame(window)
    frame_option_3.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_currency = tk.Label(frame_option_3, text="Wybierz walute:")
    label_currency.place(anchor='n', relx=0.5, rely=0.05, relwidth=1, relheight=0.2)

    button_euro = tk.Button(frame_option_3, text="Euro", command=lambda: currency_exchange_option("euro","pln",1))
    button_euro.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.5, relheight=0.1)

    button_dolar = tk.Button(frame_option_3, text="Dolar", command=lambda: currency_exchange_option("dolar","pln",1))
    button_dolar.place(anchor='n', relx=0.5, rely=0.37, relwidth=0.5, relheight=0.1)

    button_funt = tk.Button(frame_option_3, text="Funt", command=lambda: currency_exchange_option("funt","pln",1))
    button_funt.place(anchor='n', relx=0.5, rely=0.49, relwidth=0.5, relheight=0.1)

    button_frank = tk.Button(frame_option_3, text="Frank szwajcarski", command=lambda: currency_exchange_option(
        "frank","pln",1))
    button_frank.place(anchor='n', relx=0.5, rely=0.61, relwidth=0.5, relheight=0.1)

    button_back = tk.Button(frame_option_3, text="Wroc do menu", command=lambda: frame_option_3.destroy())
    button_back.place(anchor='n', relx=0.5, rely=0.8, relheight=0.1, relwidth=0.5)

# ----------------------------WINDOW SETTINGS--------------------
window = tk.Tk()
window.title("Przelicznik walut")

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

top_frame = tk.Frame(window, bg='#bfbfbf')
top_frame.place(relx=0.5, rely=0, relwidth=1, relheight=0.4, anchor='n')

menu_label = tk.Label(top_frame, text="Przelicznik walut", font=("Helvetica, 22"))
menu_label.place(relx=0.5, rely=0.3, relwidth=1, relheight=0.5, anchor='n')

lower_frame = tk.Frame(window, bg='#a6a6a6')
lower_frame.place(relx=0.5, rely=0.4, relwidth=1, relheight=0.6, anchor='n')

button_aktualne_kursy = tk.Button(lower_frame, text='Sprawdz aktualne kursy walut', command=lambda: menu_option_1())
button_aktualne_kursy.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.5, relheight=0.15)

button_convert_pln = tk.Button(lower_frame, text="Przelicz z PLN na wybraną walutę", command=lambda: menu_option_2())
button_convert_pln.place(anchor='n', relx=0.5, rely=0.3, relwidth=0.5, relheight=0.15)

button_convert_dowolna = tk.Button(lower_frame, text="Przelicz z dowolnej waluty na PLN", command=lambda:
menu_option_3())
button_convert_dowolna.place(anchor='n', relx=0.5, rely=0.5, relwidth=0.5, relheight=0.15)

button_quit = tk.Button(lower_frame, text="Wyjdz", command=lambda: quit())
button_quit.place(anchor='n', relx=0.5, rely=0.7, relwidth=0.5, relheight=0.15)

window.mainloop()