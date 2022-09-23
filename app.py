import tkinter as tk
from tkinter import ttk
import webbrowser

app = tk.Tk()
app.title("QR Reader")

search_label = ttk.Label(app, text='Путь')
search_label.grid(row=0, column=0)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=0, column=1)

def search():
    if text_field.get().strip() != "":
        pass
def searchBtn():
    search()

def enterBtn(event):
    pass

btn_search = ttk.Button(app, text="Button", width=20, command=searchBtn)
btn_search.grid(row=1, column=0)

text_field.bind('<Return>', enterBtn)

app.mainloop()