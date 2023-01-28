import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def select_file():
    filename = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mkv;*.avi;*.flv")])
    if filename:
        convert_to_audio(filename)

def convert_to_audio(filename):
    video = VideoFileClip(filename)
    audio = video.audio
    new_audio_filename = filename.split(".")[0] + ".mp3"
    audio.write_audiofile(new_audio_filename)
    video.close()
    audio.close()
    print("File converted and saved as:", new_audio_filename)

root = tk.Tk()
root.title("Video to Audio Converter")
root.geometry("350x100")

select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.pack()

root.mainloop()