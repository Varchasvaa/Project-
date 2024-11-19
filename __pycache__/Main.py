from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector 
from datetime import datetime,timedelta
from App import register,customer
    
#win.winfoscreenheight/width() 
win=CTk()
frame=str(win.winfo_screenwidth())+'x'+str(win.winfo_screenheight())
win.geometry('1536x864')
set_appearance_mode("light")  
set_default_color_theme("blue")  
#getting the current date 
current_date = datetime.now().date()  
print("Current date:", current_date)
curdate=str(current_date)
date=curdate[len(curdate)-2:]

day = current_date.strftime("%A")
month_name = current_date.strftime("%B")

coming_day_date = current_date + timedelta(days=1)
Next_day = coming_day_date.strftime("%A")  # Full weekday name (e.g., "Monday")
 

def EnterBB3(e):
    bframe.configure(width=650)
    binfo.place(x=1110,y=310)
def LeaveBB3(e):
    bframe.configure(width=310)
    binfo.place(x=-1110,y=310)

def EnterS(e):
    sframe.configure(width=650)
    sinfo.place(x=360,y=300)
def LeaveS(e):
    sframe.configure(width=310)
    sinfo.place(x=-1110,y=310)

option=""
def option(op):
    global option
    option=str(op)
    print(option)

def back():
    th1.place(x=0,y=-3000)
    th2.place(x=0,y=-5000)
    sframe.place(x=45,y=295)
    Singham.place(x=50,y=300)
    bframe.place(x=(800-5),y=295)
    BB3.place(x=800,y=300)
    button.place(x=1234,y=12)
    dropdown.place(x=500,y=12)
    back_button.place(x=-10000,y=0)
    background_label.configure(image=background_image)
    tab.place(x=-1000,y=-23)
# Creating a pop-up window for selecting seat 
def open_seat():
    popup = CTkToplevel(win)
    popup.geometry("500x500")
    popup.title("Forced Pop-Up")

    
    popup.grab_set()  
    popup.resizable(False, False)  
    
    label = CTkLabel(popup, text="This is a forced pop-up!", font=("Arial", 16))
    label.pack(pady=20)
    
    close_button = CTkButton(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    popup.transient(win)


def movieclicked():
    back_button.place(x=1234,y=12)
    sframe.place(x=-1100,y=0)
    bframe.place(x=-1100,y=0)
    dropdown.place(x=-1100,y=0)
    button.place(x=-1100,y=0)
    BB3.place(x=-1100,y=0)
    Singham.place(x=-1150,y=300)
    background_label.configure(image=blank)

#def tabview(e):
 #   th1.configure(master=date2)
 #   th2.configure(master=date2)

def movieclicked1(e):
    global option 
    if option=="":
        back()
        print("worked")
        pass
    movieclicked()
    th1.place(x=0,y=100)
    th2.place(x=0,y=300)
    time1.place(x=400,y=180)
    tab.pack(pady=60, padx=30)

def movieclicked2(e):
    global option 
    if option=="":
        back()
        print("worked")
        pass
    movieclicked()
    th1.place(x=0,y=100)
    th2.place(x=0,y=300)
    time1.place(x=400,y=180)
    tab.pack(pady=60, padx=30)

print(frame)
#Images 

background_image =CTkImage(Image.open("whitegradient .png"), size=(win.winfo_screenwidth(), win.winfo_screenheight()))
Movie1=CTkImage(Image.open('Movie1.png'),size=(300,400))
Movie2=CTkImage(Image.open('Movie2.jpg'),size=(300,400))
infos=CTkImage(Image.open('sinfo.png'),size=(300,400))
infob=CTkImage(Image.open('Binfo.png'),size=(300,390))
blank=CTkImage(Image.open('Home.png'),size=(win.winfo_screenwidth(), win.winfo_screenheight()))
bannerS=CTkImage(Image.open('MovieBanner1.png'),size=(900,430))
banner=CTkImage(Image.open('Binfo.png'),size=(600,330))
theater1=CTkImage(Image.open('theater1.png'),size=(1543,750))
theater2=CTkImage(Image.open('theater2.png'),size=(1543,750))


#background 
background_label = CTkLabel(win, image=background_image, text="")
background_label.place(relwidth=1, relheight=1) 

banner_label=CTkFrame(win, width=1536, height=500,corner_radius=15,fg_color="purple",bg_color='white')

# Movie 1 widgets (Singham)

sframe=CTkFrame(win, width=310, height=410,corner_radius=15,fg_color="purple",bg_color='white')
sframe.place(x=45,y=295)
Singham=CTkLabel(win,image=Movie1,text='',fg_color="purple")
Singham.place(x=50,y=300)
Singham.bind("<Button-1>",movieclicked1)
banner_singham=CTkLabel(win,text="",image=bannerS)
banner_singham.place()

#animation
Singham.bind("<Leave>",LeaveS)
Singham.bind("<Enter>",EnterS)

sinfo=CTkLabel(win,image=infos,fg_color="purple",bg_color="purple",text="")
sinfo.place()


#Movie 2 widgets (BB3) 

bframe=CTkFrame(win, width=310, height=410,corner_radius=15,fg_color="purple",bg_color='white')
bframe.place(x=(800-5),y=295)
BB3=CTkLabel(win,image=Movie2,text='',fg_color="purple",bg_color='purple')
BB3.place(x=800,y=300)
BB3.bind("<Button-1>",movieclicked2)
#animation
BB3.bind("<Leave>",LeaveBB3)
BB3.bind("<Enter>",EnterBB3)

binfo=CTkLabel(win,image=infob,fg_color="purple",bg_color="purple",text="")
binfo.place()

#Theater 

tab=CTkTabview(win,width=1000,height=700,bg_color="white" ,segmented_button_selected_color="purple",segmented_button_selected_hover_color="violet",fg_color="cyan")

tab_date=str(day)+'\n'+str(date)+ '\n' +month_name
tab_date1=Next_day+'\n'+str(int(date)+1)+ '\n' +month_name

'''#tab.add(tab_date)'''
tab.add(tab_date1)
'''date1=tab.tab(tab_date)'''
date1=tab.tab(tab_date1)
'''date2.bind("<Button-1>",tabview)'''
for button in tab._segmented_button._buttons_dict.values():
    button.configure(font=("Arial", 26))  

th1=CTkLabel(date1,image=theater1,text='',fg_color='white')
th2=CTkLabel(date1,image=theater2,text='',fg_color='white')

#Time slot

time1=CTkButton(date1,text='10:30',font=("Arial", 26),fg_color='lightgray',text_color="Black",bg_color="white",hover_color="gray",corner_radius=5)


#Home widgets 


button=CTkButton(win,text="   Login/Register  ",font=(("Arial"),20),fg_color="purple",bg_color='white',command=register)
button.place(x=1234,y=12)

back_button=CTkButton(win,text="back",font=(("Arial"),20),fg_color="purple",bg_color='white',command=back)
back_button.place()


a="                                                                         "

options=["Mumbai  "+a ,"Delhi-NCR "+a]
dropdown = CTkOptionMenu(win, values=options,font=(("Arial"),20), command=option,fg_color="violet",bg_color="white",button_color="violet",button_hover_color="purple")
dropdown.set("  Select your City                                        ") 
dropdown.place(x=500,y=12)

#contact=CTkLabel(master=background_label,text="Contact",font=("arial",20),text_color="black",fg_color="#f5f5f5")
#contact.place(x=400,y=70)

book=CTkButton(win,text="Book Tickets",font=(("TimesNewRoman"),50),fg_color="purple",bg_color='white')

win.mainloop()