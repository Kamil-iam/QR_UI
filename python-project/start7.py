import os
from frontend import *
#библа для интерфейса
from tkinter import *
#библы для пдф
import fitz
#библы для qr
from pyzbar import pyzbar
import cv2
from glob import glob
#работа с интерфейсом ---------------
windows = Tk()
#windows.title("QR test")
#windows.mainloop()
def qr_scan (file_path):                    #указать нужный нам файл
    pdf_file = fitz.open(file_path)         #открыть файл с пдф
    number_of_pages = len(pdf_file)         #число страниц в файле
    for page in pdf_file:                   #цикл для преоброзование все страниц в пнг
        pix = page.get_pixmap(dpi = 400)    #рендер pdf to png так-же выбираем качество картинки
        pix.save(f"page_{123}.png")
        break
    filename = "page_123.png"               #адресс к файлу с qr кодом
    img = cv2.imread(filename)              #массив данных из 255
    print (img)
    qrcodes = pyzbar.decode(img)            #расшифровка qr кода в массив параметров
    print (qrcodes)
    print (qrcodes[0].data)
    os.remove(f"page_123.png")
 
qr_scan("a4a.pdf")