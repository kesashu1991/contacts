from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk 
root= Tk()

def contvalue():
    print("saving")
    print(f"{namevalue.get(), phonevalue.get()}")

    with open("contacts.txt", "a") as c:
        c.write(f"{namevalue.get(), phonevalue.get()}\n")

def help_():
    msg.showinfo("help","hello this is a testing programme s kindly coprate with us.. Thank you")




root.geometry("295x150")

root.minsize(295,190)
root.maxsize(300,150)
image=Image.open("photo.jpg")
photo= ImageTk.PhotoImage(image)




title= Label(root,text="CONTACTS", font="comicsansms 24 bold", bg="green", fg="white", borderwidth=3, relief=SUNKEN)
title.grid(row=0,column=3, pady=10)
name= Label(root,text="NAME")
phone=Label(root,text="PHONE NO.")
name.grid(row=1,column=2,pady=10)
phone.grid(row=2,column=2,pady=10)

namevalue= StringVar()
phonevalue= StringVar()

nameentry= Entry(root, textvariable=namevalue)
phoneentry= Entry(root,textvariable=phonevalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2, column=3)

Button(text="SAVE", command=contvalue).grid(row=7,column=3,pady=10)


menu= Menu(root)
menu.add_command(label="HELP", command=help_)
root.config(menu=menu)

menu.add_command(label="EXIT", command=quit)
root.config(menu=menu)
root.mainloop()