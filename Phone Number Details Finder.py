#!/usr/bin/env python
# coding: utf-8

# # Phone Number Details Finder

# In[74]:


import tkinter
import phonenumbers
from tkinter import *
from tkinter import messagebox
from phonenumbers import timezone,geocoder,carrier as phone_carrier

def abc():
    
    user_input = name.get()
    try:
        phone = phonenumbers.parse(user_input)
        time = timezone.time_zones_for_number(phone)  # it gives timezone
        carrier = phone_carrier.name_for_number(phone, "en")  # Use the renamed 'carrier' module
        region = geocoder.description_for_number(phone, "en")  # it gives location
        
        result_text = f"Phone number:\n{phone}\nTimezone: {time}\nCarrier: {carrier}\nRegion: {region}"
        messagebox.showinfo("Phone Details", result_text)
        
    except phonenumbers.phonenumberutil.NumberParseException as e:
        messagebox.showerror("Error", f"Invalid phone number: {e}")
            

    
    
        

root= Tk()
root.geometry("600x400")
root.title("Phone Number Details Finder")
root.config(bg="powder blue")

lbltitle=Label(root,text="Phone Number Details Finder",bg="white",fg="black",bd=10,relief=RAISED,font=("times new roman",25,"bold"))
lbltitle.place(x=50,y=10,width=500,height=50)


name=Label(root,font=("times new roman",18,"bold"),text="Enter the no. with Country code",bg="powder blue")
name.place(x=100,y=100,width=400,height=50)
name=Entry(root,font=("times new roman",20,"bold"),width=40)
name.place(x=150,y=170,width=300,height=30)


    

button = Button(root, text="Go", font=("Times New Roman",25),command=abc)
button.place(x=180,y=230,width=240,height=35)

note=Label(root,font=("times new roman",15),text="Note: The result shown to you will be older information about your number.\nIf you port your sim it will not give new sim company name,etc.",bg="powder blue")
note.place(x=0,y=325,width=600,height=50)

root.mainloop()


# In[ ]:




