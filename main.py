from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b50d61abcc3821890b645d416133dea4").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pres_label1.config(text=data["main"]["pressure"])




win=Tk()
win.title("python development")
win.config(bg="teal")
win.geometry("500x600")
name_label=Label(win,text="Weather App",font=("Poppins",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Weather App",values=list_name,font=("Roboto",20),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text="Weather climate",font=("Poppins",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",font=("Times New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)
wd_label=Label(win,text="Weather description",font=("Poppins",17))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1=Label(win,text="",font=("Times New Roman",17))
wd_label1.place(x=250,y=330,height=50,width=210)
temp_label=Label(win,text="Temperature",font=("Poppins",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=("Times New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)
pres_label=Label(win,text="Pressure",font=("Poppins",20))
pres_label.place(x=25,y=470,height=50,width=210)
pres_label1=Label(win,text="",font=("Times New Roman",20))
pres_label1.place(x=250,y=470,height=50,width=210)
done_button=Button(win,text="Done",font=("Poppins",20,"bold"),command=data_get) 
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()