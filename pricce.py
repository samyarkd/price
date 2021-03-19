import requests
import tkinter as tk

req = requests.get('https://www.digikala.com/')

canvas = tk.Tk()
canvas.geometry('1700x900')
canvas.title('Price')

lable1 = tk.Label(canvas)
lable1.config(text = str(req.text))
lable1.pack()

tk.mainloop()
