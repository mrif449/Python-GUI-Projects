from operator import le
import tkinter as tr
from tkinter import messagebox

default_font = "Arial Rounded MT"
font_size = 12
button_color = "white"

root = tr.Tk()
root.title("BMI Calculator")

def Calculate():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        result = round(weight/(height**2),2)
        label_result["text"] = f"BMI: {result}"
        button_calcucate["text"] = "Reset"
        button_calcucate["command"] = Reset
        button_calcucate["bg"] = "#ed2939"
    except:
        tr.messagebox.showwarning(title="Failed",message="Entry is blank!!!")
def Reset():
    entry_height.delete(0,tr.END)
    entry_weight.delete(0,tr.END)
    label_result["text"] = "BMI: "
    button_calcucate["text"] = "Calculate"
    button_calcucate["command"] = Calculate
    button_calcucate["bg"] = "#29c5f6"
label_weight = tr.Label(root, text="Weight (KG): ")
label_weight.grid(column=0, row=0)
entry_weight = tr.Entry(root)
entry_weight.grid(column=1, row=0)
label_height = tr.Label(root, text="Height (m): ")
label_height.grid(column=0, row=1)
entry_height = tr.Entry(root)
entry_height.grid(column=1, row=1)

button_calcucate = tr.Button(root,text="Caculate",command=Calculate, bg="#29c5f6", fg=button_color, font=(default_font,font_size))
button_calcucate.grid(column=0, row=2)
label_result = tr.Label(root, text="BMI: ")
label_result.grid(column=1, row=2)