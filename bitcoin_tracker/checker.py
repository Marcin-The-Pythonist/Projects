import requests
from tkinter import *


def get_price():
        global label_price
        api = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,PLN')
        prices = dict(api.json())
        price_usd = prices.get('USD')
        label_price.config(text=f"{price_usd}$")
        
        

    
api = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,PLN')

#Main window
root = Tk()
root.title("Bitcoin check!")
root.iconbitmap('bitcoin.ico')
root.geometry("400x450")
root.minsize(400,450)
root.maxsize(400,450)
root.config(bg='black')
root.config(pady='5px')



#Image 
image = PhotoImage(file="btc.png")
label_btc_img = Label(root, image = image)
label_btc_img.pack()

#Price display
prices = dict(api.json())
price_usd = prices.get('USD')
label_price = Label(root, text=f"{price_usd}$", font="arial_black", pady='10px', bg='black', fg='white')
label_price.pack()

#Button to request the current price
button = Button(root, command=get_price, text="Check current price", font='arial_black', pady='10px', bg='black', fg='white')
button.pack()

root.mainloop()
