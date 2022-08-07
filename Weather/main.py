import tkinter as tr
from turtle import bgcolor, color
import requests
import time
from tkinter import TOP, Listbox, messagebox
from datetime import datetime


def Weather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    
    json_data = requests.get(api).json()
    now = datetime.now()
    hour = now.strftime("%H")
    if int(hour) > 12:
        hour = str(int(hour)-12)
        current_time = now.strftime(f"{hour}:%M:%S p.m.")    
    else:
        current_time = now.strftime(f"%H:%M:%S a.m.")
    try:
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 274.15)
        min_temp = int(json_data['main']['temp_min'] - 274.15)
        max_temp = int(json_data['main']['temp_max'] - 274.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
        Rain = "⛆"
        Haze = "🌫"
        Clouds = "☁"
        Sunny = "☀"
        Clear = "☾"
        sign = ""
        normal = "🌤"
        if condition == "Clear" and "p.m." in current_time and hour > 6:
            sign = Clear
        elif condition == "Rain":
            sign = Rain
        elif condition == "Haze" or condition == "Mist":
            sign = Haze
        elif condition == "Clear":
            sign = Sunny
        elif condition == "Clouds":
            sign = Clouds
        else:
            sign = normal
        
        final_info = "🌡" + str(temp) + "°C"+  "   " +condition + " "+ sign
        info_data = f"Detailed Weather Status: \n{city.upper()}"
        final_data = "Time: " + current_time + "\n" + "Temperature: " + str(min_temp) + "°C" + " / " + str(max_temp) + "°C" +"\n" + "Air Pressure: " + str(pressure) + "hPa" + "\n" + "Wind Speed: "  + str(wind) + " Km/h" "\n" +"Humidity: " + str(humidity) + "\n" + "Sunrise: " + sunrise[::-2] + " a.m." + "\n" + "Sunset: " + sunset[::-2] + " p.m."
        
        label1.config(text = final_info,bg="skyblue")
        label2.config(text = info_data,bg="yellow")
        label3.config(text = final_data,bg="orange")
    except:
        final_info = "!!!Invalid Location!!!\n\nCheck the spelling."
        final_data = ""
        info_data = ""
        label1.config(text = final_info,bg="red")
        label2.config(text = info_data)
        label3.config(text = final_data)
        

canvas = tr.Tk()
canvas.geometry("500x400")
canvas.title("Weather App")
default_font0 = ("Lucida Console", 15, "bold")
default_font1 = ("Bauhaus 93", 35, "bold")
default_font2 = ("Gill Sans MT", 25, "bold")
default_font3 = ("Lucida Console", 15, "bold")
label0 = tr.Label(canvas, font=default_font0)
label0.pack()

intro = "Enter the City/Country:"
label0.config(text = intro)

textField = tr.Entry(canvas, justify='center', width = 25, font = 50,bg="pink")
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', Weather)

label1 = tr.Label(canvas, font=default_font1)
label1.pack()
label2 = tr.Label(canvas, font=default_font2)
label2.pack()
label3 = tr.Label(canvas, font=default_font3, justify="left")
label3.pack()
canvas.mainloop()