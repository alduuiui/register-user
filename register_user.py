from tkinter import *
import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="register_user"
)
cursor = mydb.cursor()

def register_user(name, family, address):
    q = f"INSERT INTO `nazli`(`name`, `family`, `address`) VALUES ('{name}','{family}','{address}')"
    cursor.execute(q)
    mydb.commit()
    if cursor.rowcount == 0:
        messagebox.showerror("Error", "User not registered")
    else:
        messagebox.showinfo("Success", "User registered successfully")
    

window = Tk()
window.title("Register User")
window.geometry("500x500")
window.resizable(False, False)
name = StringVar()
family = StringVar()
address = StringVar()


lab_name = Label(window, text="Name", font=("Arial", 15))
lab_name.place(x=100, y=100)
lab_family = Label(window, text="Family", font=("Arial", 15))
lab_family.place(x=100, y=150)
lab_address = Label(window, text="Address", font=("Arial", 15))
lab_address.place(x=100, y=200)
ent_name = Entry(window, textvariable=name)
ent_name.place(x=200, y=100)
ent_family = Entry(window, textvariable=family)
ent_family.place(x=200, y=150)
ent_address = Entry(window, textvariable=address)
ent_address.place(x=200, y=200)
btn_save = Button(window, text="Save", command=lambda: register_user(name.get(), family.get(), address.get())).place(x=200, y=250)



window.mainloop()