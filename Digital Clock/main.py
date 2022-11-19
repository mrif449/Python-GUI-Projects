from time import strftime
from tkinter import *
from tkinter.ttk import *

display= Tk()
display.title("Digital Clock")
def digitalClock():
	text = strftime(" %H:%M:%S %p ")
	label.config(text = text)
	label.after(1000,digitalClock)
label = Label(display, font= ("Digit Dream Regular", 100, "bold"), background="black",foreground="#00FF7F")
label.pack(anchor="center")
digitalClock()
mainloop()
