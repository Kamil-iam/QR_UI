import tkinter as tk
from tkinter import ttk
from tkinter import *
import cv2

#root = Tk()
#from tkFileDialog import ask
import webbrowser

app = tk.Tk()
app.title("QR Reader")
filename = "path"
#дефайн для path-button
MyText= StringVar()
def DisplayDir(Var):
    feedback = askdirectory()
    Var.set(feedback)
def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

search_label = ttk.Label(app, text='Путь к файлу:')
search_label.grid(row=0, column=0)



text_field = ttk.Entry(app, width=50)
text_field.grid(row=0, column=1)

filepath = text_field


img = cv2.imread(filename)

detector = cv2.QRCodeDetector()
# обнаружить и декодировать
#data, bbox, straight_qrcode = detector.detectAndDecode(img)

data = "Test1"
dataRes = data
dataRes_label = ttk.Label(app, text=dataRes)
dataRes_label.grid(row=1, column=0)

def search():
    if text_field.get().strip() != "":
        pass
def searchBtn():
    search()

def enterBtn(event):
    pass

btn_search = ttk.Button(app, text="Button", width=20, command=searchBtn)
btn_search.grid(row=1, column=0)

#Отслеживание события нажатия на Enter
text_field.bind('<Return>', enterBtn)

#Всегда поверх - выключено
app.wm_attributes('-topmost', False)


app.mainloop()