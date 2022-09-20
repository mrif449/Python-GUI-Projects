import random
from tkinter import *
import os
from tkinter import ttk
import tkinter as tr
import random
import tkinter.messagebox
def copypass(text):
    command = "echo " + text.strip() + "| clip"
    os.system(command)
digits=['1','2','3','4','5','6','7','8','9','0']
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['#','$','%','&','(',')','*','+','-','.','/',':','<','=','>','?','@','[',']','^','_','{','}','/', ' ']
display = Tk()
display.geometry("300x270")
display.title("Password Generator")
display.resizable(0,0)
password_string=StringVar()
def Copy_password():
        copypass(password_string.get())
def generate():
    global letters
    global digits
    global symbols
    try:
        length = int(entry.get())
    except:
        tkinter.messagebox.showerror("Invalid Length")
    together = []
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
        tkinter.messagebox.showinfo("Selection the options")
    if var1.get() == 1:
        for x in letters:
            together.append(x)
    if var2.get() == 1:
        for x in digits:
            together.append(x)
    if var3.get() == 1:
        for x in symbols:
            together.append(x)
    password = ""
    for x in range(length):
        password += together[random.randint(0,len(together)-1)]
    password_string.set("".join(password))
var1 = tr.IntVar()
var2 = tr.IntVar()
var3 = tr.IntVar()
heading = tr.Label(display, text = "Generate Your Password" , font ='arial 15 bold').pack()
label1 = tr. Label(display,text="Includes: ",font ='Arial 13 bold').pack()
checkbox1 = Checkbutton(display, text="Letters", variable=var1, onvalue=1, offvalue=0, anchor="w").pack()
var1.set(1)
checkbox2 = Checkbutton(display, text="Digits", variable=var2, onvalue=1, offvalue=0, anchor="w").pack()
var2.set(1)
checkbox3 = Checkbutton(display, text="Symbols", variable=var3, onvalue=1, offvalue=0, anchor="w").pack()
var3.set(1)
label1 = tr. Label(display,text="Enter Length of Password: ",font ='Arial 13 bold').pack()
entry= ttk.Entry(display,font=('Arial 12'),width=10,justify=CENTER)
entry.pack()
generate =ttk.Button(display, text="Generate Password",command=generate).pack()
ttk.Entry(display, textvariable=password_string,font=('Arial 12',), width=30, justify=CENTER).pack()
copy=ttk.Button(display, text = 'Copy', command = Copy_password).pack()
display.mainloop()