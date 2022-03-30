#Importing Modules
from textwrap import fill
import tkinter as tr
from tkinter import TOP, Listbox, messagebox
import pickle
from tkinter.tix import Tk


#Title
root = tr.Tk()
root.title("To-Do List")


#Declaration
height1 = 30
width1 = 100
width2 = 20
default_font = "Arial Rounded MT"
font_size = 12
saver = 2
button_color = "white"

#Functions
def add_entry():
    global saver
    task_data = entry.get()
    if task_data == "":     #Making sure no blank task
        tr.messagebox.showwarning(title="Failed",message="Blank entry can not be added")
    else:
        if saver %2 == 0:
            task_data = "❒ "+task_data
            tasks.insert(tr.END, task_data)
            entry.delete(0, tr.END)     #Clears task after input
        else:
            task_data = "❒ "+task_data
            tasks.insert(tr.END, task_data)
            entry.delete(0, tr.END)     #Clears task after input
            data = tasks.get(0,tasks.size())
            pickle.dump(data, open("To-Do.dat","wb"))
def drop_entry():
    try:
        select_entry = tasks.curselection()[0]
        tasks.delete(select_entry)
    except:
        tr.messagebox.showwarning(title="Failed",message="Please select a task to delete")
def save_entry():
    data = tasks.get(0,tasks.size())
    pickle.dump(data, open("To-Do.dat","wb"))
    tr.messagebox.showwarning(title="Successful",message="Tasks are saved at To-Do.dat")
def auto_save():
    global saver
    saver += 1
    if saver%2 != 0:
        tr.messagebox.showwarning(title="Successful",message="Auto Save Enabled")
    else:
        tr.messagebox.showwarning(title="Successful",message="Auto Save Disabled")
def delete_all():
    tasks.delete(0,tr.END)


#Design Part
framming = tr.Frame(root)
framming.pack()

scrollbar = tr.Scrollbar(framming)
scrollbar.pack(side=tr.RIGHT, fill=tr.Y)

tasks = tr.Listbox(framming, height=height1, width=width1, bg="#9cedc3", font=(default_font,font_size), cursor="dot")
tasks.pack()

tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks.yview)

entry = tr.Entry(root, width=80, bg="#c3e7fd", font=(default_font,font_size))
entry.pack()


#Buttons
button1 = tr.Button(root, command= add_entry, text= "[+] Add", width= width2, bg="#03ac13", fg=button_color, font=(default_font,font_size))
button1.pack(side=tr.RIGHT)
button2 = tr.Button(root, command= drop_entry, text= "[-] Drop", width= width2, bg="#ffa500", fg=button_color, font=(default_font,font_size))
button2.pack(side=tr.RIGHT)
button3 = tr.Button(root, command= save_entry, text= "[✔] Save", width= width2, bg= "#1260cc", fg=button_color, font=(default_font,font_size))
button3.pack(side=tr.RIGHT)
button4 = tr.Button(root, command= auto_save, text= "[✔✔] Auto Save", width= width2, bg= "#006242", fg=button_color, font=(default_font,font_size))
button4.pack(side=tr.RIGHT)
button5 = tr.Button(root, command= delete_all, text= "[🗑] Delete All", width= width2, bg= "#8b0000", fg=button_color, font=(default_font,font_size))
button5.pack(side=tr.RIGHT)
#Runner
def runner():
    try:        #For auto restoring previous state
        data = pickle.load(open("To-Do.dat", "rb"))
        tasks.delete(0, tr.END)
        for x in data:
            tasks.insert(tr.END, x)
    except:
        pass
    root.mainloop()
runner()