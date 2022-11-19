# importing Modules
import shutil
from tkinter import *
from moviepy import *
from pytube import YouTube
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from tkinter import TOP, Listbox, messagebox
import tkinter as tr

# Defining Functions
def download_location():
    location= filedialog.askdirectory()
    location_label.config(text= download_location)

def video_file():
    download_link = link.get()
    user_location = location_label.cget("text")
    #display.title("Downloading...")
    tr.messagebox.askquestion("Confirmation",message="Are you proceed to Download?")
    mp4_video = YouTube(download_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_location)
    tr.messagebox.showinfo(title="Successful",message="Video Downloaded")

#App structure
display = Tk()
title = display.title("YouTube Video Downloader")
window = Canvas(display, width=500, height=450)
window.pack()
display.attributes('-alpha',0.5)

#Setting App Logo
#Image Source: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/2560px-Logo_of_YouTube_%282015-2017%29.svg.png
app_logo = PhotoImage(file="applogo.png")
app_logo = app_logo.subsample(9,12)
window.create_image(250, 80, image=app_logo)

#setting link entry
link = Entry(display, width=40, font=('Arial', 15) )
link_label = Label(display, text="Enter Download Link: ", font=('Arial', 15))

#download path
location_label = Label(window, text="Enter YouTube Video Link", bg="yellow",font=('Arial', 15))
select_btn =  Button(window, text="Select Download Location", bg='blue', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_location)
window.create_window(250, 280, window=location_label)
window.create_window(250, 330, window=select_btn)
window.create_window(250, 280, window=location_label)
window.create_window(250, 330, window=select_btn)
window.create_window(250, 170, window=location_label)
window.create_window(250, 220, window=link)

#Making download button
download_button = Button(window, text="Download Video",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=video_file)
window.create_window(250, 390, window=download_button)

window.mainloop()


