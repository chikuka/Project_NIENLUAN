import base64
import mysql.connector
import pandas as pd
import tkinter as tk
from mysql.connector import MySQLConnection, Error
from tkinter import *
from  tkinter import ttk

#ConnectMySQL
try:
    # Ket noi MySQL voi Python bang ham mysql.connector.connect()
    db = mysql.connector.connect(host="127.0.0.1",
        port=3306,
        user="root",
        password="reiha123",
        database="products_lables"
    )
    print("Ket noi thanh cong!")
except: # Truong hop co loi khi ket noi
    print("Kiem tra lai thong tin ket noi!")

root=Tk()
root.title("Details")
root.geometry("1000x500")
T = Text(root, height=1000, width=500)
l = Label(root, text = "Chi tiết sản phẩm")
l.config(font =("Courier", 14))

l.pack()
T.pack()

# def input_READ():
f=open('labels_data.txt','r')
word = f.read().splitlines()
# print(word)
cursor=db.cursor()
for a in word:
    # print(a)
    cursor.callproc("Searchlabels",[a])
    # cursor.stored_results()
    for result in cursor.stored_results():
        detail=result.fetchall() 
        # print(detail[0])
    for det in detail:
        print("Label:",det[0])
        print("Nhãn hàng:",det[1])
        print("Loại sản phẩm:",det[2])
        print("Thành phần:",det[3],"\n") #det[0]=label; 1=product; 2=type; 3=ingredients
        I="""Label: """+det[0]+"""\nNhãn hàng: """+det[1]+"""\nLoại: """+det[2]+"""\nThành phần: """+det[3]+"""\n\n"""

        T.insert(1.0,I)

tk.mainloop()
cursor.close()

