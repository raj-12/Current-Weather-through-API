import requests
from tkinter import *
import time
#openweathermap.org
#https://openweathermap.org/data/2.5/weather?q={}&appid=6fda34b14b8847c4db226e262b371c59
def weather():
    city = city_listbox.get()
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=6fda34b14b8847c4db226e262b371c59".format(city)
    res = requests.get(url)
    output = res.json()
    weather_status = output['weather'][0]['description']
    temprature = output['main']['temp']
    humidity = output['main']['humidity']
    wind_speed = output['wind']['speed']
    max_temp=output['main']['temp_max']
    pressure=output['main']['pressure']

    weather_status_label.configure(text = "Weather status :"+weather_status)
    temprature_label.configure(text="Temprature status:" + str(temprature))
    humidity_label.configure(text="Humidity status :" + str(humidity))
    wind_speed_label.configure(text="Wind speed status :" + str(wind_speed))
    pressure_label.configure(text="Pressure status :"+str(pressure))
    max_temp_label.configure(text="Maximum temprature :"+str(max_temp))

    current_date=time.strftime("%d:%m:%y")
    current_time=time.strftime("%H:%M:%S")
    time_label.configure(text="Current Time : "+ current_time)

    date_label.configure(text="Current Date : "+ current_date)


window =Tk()
window.title("Weather Detector")
window.geometry("600x300")

city_name_list = ["Pune","Hiwarkhed","Akola","Nashik","Amravati","Mumbai","Delhi"]
city_listbox = StringVar(window)
city_listbox.set("Select the City")
#t=input()
option = OptionMenu(window,city_listbox,*city_name_list)
option.grid(row=1,column =5,padx = 150,pady =10)
b1 = Button(window,text ="Submit",width =15,command =weather)
b1.grid(row= 5,column =5,padx = 150)

weather_status_label = Label(window,font=("times",10,"bold"))
weather_status_label.grid(row=10,column=5)

temprature_label = Label(window,font=("times",10,"bold"))
temprature_label.grid(row=13,column=5)

humidity_label = Label(window,font=("times",10,"bold"))
humidity_label.grid(row=14,column=5)

wind_speed_label = Label(window,font=("times",10,"bold"))
wind_speed_label.grid(row=16,column=5)

max_temp_label = Label(window,font=("times",10,"bold"))
max_temp_label.grid(row=18,column=5)

pressure_label=Label(window,font=("times",10,"bold"))
pressure_label.grid(row=20,column=5)

time_label=Label(window,font=("times",10,"bold"))
time_label.grid(row=20,column=6)

date_label=Label(window,font=("times",10,"bold"))
date_label.grid(row=22,column=6)

window.mainloop()
