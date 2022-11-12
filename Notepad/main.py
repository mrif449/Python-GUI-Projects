#import modules
from tkinter import *

#setting variables
background = "#3D3D3D"
font_color = "white"
resolution1 = "1250x805"
resolution2 = "560x50"
app_title = "Python Notepad"
width1 = 50
text_color = "white"
#building structure
def run():
    display = Tk()
    app = window(display)
    app.display.mainloop()

class window:
    def __init__(self,display) -> None:
        self.display = display
        self.display.geometry(resolution1)
        self.display.title(app_title)

        #Creating text
        self.text = Text(self.display,font="Fira 20 bold",bg=background,fg=text_color)
        self.text.grid(row=1, column=1)

        #creating buttons
        Button(self.display, text="Open", command= self.open, bg="black", fg="white").grid(row=0, column=0)
        Button(self.display, text="Save", command= self.save, bg="black", fg="white").grid(row=0, column=1)

        pass
    
    def save(self):
        save_data = Tk()
        save_data.geometry(resolution2)
        filecontent = self.text.get(0,0,END)

        def writedata():
            with open(file_name.get()+".txt","w+") as file:
                file.write(filecontent)
                save_data.destroy()
            return None
        
        Label(save_data, text = "Enter File Name:").grid(row=0, column=0)
        file_name = Entry(save_data, width=width1)
        file_name.grid(row=0, column=1)

        Button(save_data, text="Save", command=writedata).grid(row=0, column=2)
        return None
    
    def open(self):
        open_data = Tk()
        open_data.geometry(resolution2)

        def open_file():
            try:
                with open (file_name.get(),"r") as file:
                    self.text.delete(0,0,END)
                    self.text.insert(0,0,file.read())
                    file.close()
                    open_data.destroy()
            except FileExistsError:
                file_name.delete(0,0,END)
                file_name.insert(0,0,"!File Not Found, Try Again!")
            return None

        Label(open_data, text="Enter File Name: ").grid(row=0, column=0)
        
        file_name = Entry(open_data, width=width1)
        file_name.grid(row=0, column=1)
        
        Button(open_data, text = "Open", command = open_file).grid(row=0, column = 2)
        return None
    pass
run()