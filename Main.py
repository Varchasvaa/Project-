from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector 
#win.winfoscreenheight/width() 
win=CTk()
frame=str(win.winfo_screenwidth())+'x'+str(win.winfo_screenheight())
win.geometry(frame)
set_appearance_mode("light")  
set_default_color_theme("blue")  

def option(op):
    print(op)

def movieclicked1(e):
    print('Singham')

def movieclicked2(e):
    print('BB3')

print(frame)
background_image =CTkImage(Image.open("whitegradient .png"), size=(win.winfo_screenwidth(), win.winfo_screenheight()))
Movie1=CTkImage(Image.open('Movie1.png'),size=(300,400))
Movie2=CTkImage(Image.open('Movie2.jpg'),size=(300,400))
infos=CTkImage(Image.open('sinfo.png'),size=(300,400))

background_label = CTkLabel(win, image=background_image, text="")
background_label.place(relwidth=1, relheight=1) 


# Movie 1 widgets (Singham)

sframe=CTkFrame(win, width=650, height=410,corner_radius=15,fg_color="purple",bg_color='white')
sframe.place(x=45,y=295)
Singham=CTkLabel(win,image=Movie1,text='',fg_color="purple")
Singham.place(x=50,y=300)
Singham.bind("<Button-1>",movieclicked1)

sinfo=CTkLabel(win,image=infos,fg_color="purple",bg_color="purple",text="")
sinfo.place(x=360,y=300)


#Movie 2 widgets (BB3) 

bframe=CTkFrame(win, width=600, height=410,corner_radius=15,fg_color="purple",bg_color='white')
bframe.place(x=(800-5),y=295)
BB3=CTkLabel(win,image=Movie2,text='',fg_color="purple",bg_color='purple')
BB3.place(x=800,y=300)
BB3.bind("<Button-1>",movieclicked2)

#Home widgets 


button=CTkButton(win,text="   Login/Register  ",font=(("Arial"),20),fg_color="purple",bg_color='white')
button.place(x=1234,y=12)
options=["Mumbai  " ,"Delhi-NCR ","Bengaluru  ",'Hyderabad                                                                                              ']
dropdown = CTkOptionMenu(win, values=options,font=(("Arial"),20), command=option,fg_color="violet",bg_color="white",button_color="violet",button_hover_color="purple")
dropdown.set("  Select your City                                        ") 
dropdown.place(x=500,y=12)



win.mainloop()