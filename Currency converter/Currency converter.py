import tkinter as tk
import requests

class Converter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.apilayer.com/exchangerates_data/convert"

    def convert(self, amount, from_currency, to_currency):
        url = f"{self.base_url}?amount={amount}&from={from_currency}&to={to_currency}"
        headers = {"apikey": self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()["result"]
        else:
            return None

class App:
    def __init__(self, master):
        self.master = master
        self.converter = Converter(api_key="RjbgGjELWcOY2Ofn0KNFpcyMIFS4OrIB") #entre votre clé

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1)

        self.from_label = tk.Label(master, text="From:")
        self.from_label.grid(row=1, column=0)

        self.from_entry = tk.Entry(master)
        self.from_entry.grid(row=1, column=1)

        self.to_label = tk.Label(master, text="To:")
        self.to_label.grid(row=2, column=0)

        self.to_entry = tk.Entry(master)
        self.to_entry.grid(row=2, column=1)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=4, column=0, columnspan=2)

    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_entry.get().upper()
        to_currency = self.to_entry.get().upper()

        result = self.converter.convert(amount, from_currency, to_currency)
        if result is not None:
            self.result_label.config(text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        else:
            self.result_label.config(text="Error converting currency")

root = tk.Tk()
app = App(root)
root.mainloop()