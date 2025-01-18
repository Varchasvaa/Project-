from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector 
from datetime import datetime,timedelta
from App import register,customer
from tkinter import messagebox


mydb = mysql.connector.connect(host="localhost",user="root",password="varchasva",database='Info')
try:
    cursor=mydb.cursor()
    cursor.execute("Create table Booking_Info(Customer varchar(50),City varchar(30),Movie varchar(25),Time varchar(20),Seats varchar(25))"  )
except:
    mydb.close()

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
Next_day = coming_day_date.strftime("%A")  # 
 

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

def EnterPush(e):
    Pushframe.configure(width=650)
    Pushinfo.place(x=725,y=295)
def LeavePush(e):
    Pushframe.configure(width=310)
    Pushinfo.place(x=-1110,y=310)

def Enterbj(e):
    Bjframe.configure(width=650)
    Bjframe.place(x=860,y=295)
    Bjohninfo.place(x=880,y=310)
def Leavebj(e):
    Bjframe.configure(width=310)
    Bjframe.place(x=795+380,y=295)
    Bjohninfo.place(x=-1110,y=310)

option=""
def opt(op):
    global option
    option=str(op)
    print(option)

#Seat management 
rows=6
columns=8
seats={}
selected_seat=[]

def seat_select(s):
    print(s)
    button=seats[s]
    if button.cget('fg_color')=="lightgray":
        button.configure(fg_color="Green")
        selected_seat.append(button.cget('text'))
    elif button.cget('fg_color')=="Green":
        selected_seat.remove(button.cget('text'))
        button.configure(fg_color="lightgray")
    elif button.cget('fg_color')=="Red":
        pass
    s_label()
    
def s_label():
    text=seat_label.cget('text')
    Sname=''
    if selected_seat==[]:
        seat_label.configure(text="Seat selected:None")
    else:
        for i in selected_seat:
            Sname=Sname+' '+i
        seat_label.configure(text="Seat selected:"+Sname)

def seat_struc():
    for row in range(rows):
        for column in range(columns):
            SID=chr(65+row)+str(column+1)
            button=CTkButton(seat_frame,text=SID,fg_color="lightgray",text_color="Purple",font=("Timesnewroman",18),width=50,height=50,command=lambda s=SID:seat_select(s))
            button.grid(row=row,column=column,padx=5,pady=5)
            seats[SID]=button
    print("Succesfull")
    list=check_seat()
    print(list)
    for i in list:
        print(i)
        print(i,i in seats)
        if i in seats:
            but=seats[i]
            but.configure(fg_color="Red")

def check_seat():
    db = mysql.connector.connect(host="localhost",user="root",password="varchasva",database='Info')
    cursor=db.cursor() 
    print("select Seats from booking_info where Movie='{0}' and City='{1}' and Time={2} ".format(movie_selected,option.strip(),time_selected))   
    cursor.execute("select Seats from booking_info where Movie='{0}' and City='{1}'and Time='{2}'".format(movie_selected,option.strip(),time_selected))
    list=[]
    for i in cursor:
        for j in range(len(i)):
                l=i[j].split(',')
                list.extend(l)
    print("the list",list)
    return list


time_selected=''
def open_seat(time):
    global time_selected
    time_selected=time
    back_time.place(x=1234,y=12)
    book.place(x=1234,y=622)
    seat_frame.pack(pady=60, padx=35)
    seat_label.pack()
    time_clicked()
    seat_struc()

def book_confirm():
    text=seat_label.cget('text')
    if text=="Seat selected:None":
        seat_notselected.pack()
    print(customer,movie_selected,option,time_selected,selected_seat)

    response = messagebox.askyesno("Confirmation", "Do you want to proceed?")
    if response:
        messagebox.showinfo("Confirmed", "You chose to proceed.")
        l=load()
        if l==True:
            postbooking()
        else:
            pass
    else:
        messagebox.showinfo("Cancelled", "You cancelled the operation.")
    


def load():
    db = mysql.connector.connect(host="localhost",user="root",password="varchasva",database='Info')
    cursor=db.cursor()
    seatselect=""
    for i in selected_seat:
        seatselect+=i+','
    try:
        print("Insert into booking_info values('{0}','{1}','{2}','{3}','{4}') ".format(customer,option.strip(),movie_selected,time_selected,seatselect[:-1]))  
        cursor.execute("Insert into booking_info values('{0}','{1}','{2}','{3}','{4}') ".format(customer,option.strip(),movie_selected,time_selected,seatselect[:-1]))
    except:
        print("Error occured")
    db.commit()
    return True



def postbooking():
    seat_notselected.place(x=-1199,y=-129)
    background_label.configure(image=blank)
    QRcode.pack(padx=100,pady=100)
    QRbutton.pack()
    pb()


def pb():
    back_time.place(x=-1234,y=12)
    book.place(x=-1234,y=622)
    seat_frame.place(y=60, x=-1135)
    seat_label.place(x=-1234,y=622)

def back():
    th1.place(x=0,y=-3000)
    th2.place(x=0,y=-5000)
    mth.place(x=0,y=-5000)
    sframe.place(x=45,y=295)
    Singham.place(x=50,y=300)
    bframe.place(x=(800-5),y=295)
    BB3.place(x=800,y=300)
    button.place(x=1234,y=12)
    dropdown.place(x=500,y=12)
    Pushframe.place(x=45+380,y=295)
    Pushpa.place(x=50+380,y=300)
    Bjohn.place(x=800+380,y=300)
    Bjframe.place(x=795+380,y=295)
    Bjframe.configure(fg_color="purple")
    back_button.place(x=-10000,y=0)
    background_label.configure(image=background_image)
    tab.place(x=-1000,y=-23)
    seat_label.place(x=-1234,y=12)
    QRcode.place(x=-1234,y=12)
    QRbutton.place(x=-1234,y=12)
    advertf.place(x=110,y=130)

def confirm_location():
    global option
    if option=="":
        popup = CTkToplevel(win)
        popup.geometry("500x200")
        popup.title("Location not choosen")  
        popup.grab_set()  
        popup.resizable(False, False)  
        
        label = CTkLabel(popup, text="Pleases select location first", font=("Arial", 26))
        label.pack(pady=20)
        
        close_button = CTkButton(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

        popup.transient(win)
    else:
        pass


def movieclicked():
    global customer
    button.configure(text=customer)
    back_button.place(x=1234,y=12)
    sframe.place(x=-1100,y=0)
    bframe.place(x=-1100,y=0)
    dropdown.place(x=-1100,y=0)
    button.place(x=-1100,y=0)
    BB3.place(x=-1100,y=0)
    Pushpa.place(x=-1100,y=0)
    Pushframe.place(x=-1100,y=0)
    Bjframe.place(x=-1100,y=0)
    Bjohn.place(x=-1100,y=0)
    Singham.place(x=-1150,y=300)
    background_label.configure(image=blank)

    back_time.place(x=-1234,y=12)
    seat_frame.place(x=-1234,y=12)
    seat_label.place(x=-1234,y=12)
    advertf.place(x=-1110,y=-1130)
    time1.place(x=-1110,y=-1130)
    time2.place(x=-1110,y=-1130)
    time3.place(x=-1110,y=-1130)
    time4.place(x=-1110,y=-1130)

def seat_back():
    global selected_seat,option
    seat_label.configure(text="Seat selected:None")
    selected_seat=[]
    back_button.place(x=1234,y=12)
    th1.place(x=0,y=100)
    th2.place(x=0,y=300)
    if option=="Delhi-NCR":
        time1.place(x=400,y=180)
        time3.place(x=400,y=380)
    elif option=="Mumbai":
        time2.place(x=500,y=180)
        time4.place(x=500,y=380)        
    tab.pack(pady=60, padx=30)
    background_label.configure(image=blank)
    back_time.place(x=-1234,y=12)
    seat_frame.place(x=-1234,y=12)
    seat_label.place(x=-1234,y=12)
    book.place(x=-1234,y=12)

def time_clicked():
        back_button.place(x=-1234,y=12)
        th1.place(x=0,y=-1100)
        th2.place(x=0,y=-1300)
        time1.place(x=400,y=-1180)
        time3.place(x=400,y=-1180)
        tab.place(x=-1999,y=0)
        background_label.configure(image=Cinema_image)


movie_selected=''
def movieclicked1(e):
    global option,movie_selected
    movie_selected="Singham Again"
    if option=="":
        back()
        confirm_location()
        print("worked")
    elif option.strip()=="Delhi-NCR":
        movieclicked()
        th1.place(x=0,y=100)
        th2.place(x=0,y=300)
        time1.place(x=400,y=180)
        time3.place(x=400,y=380)
        tab.pack(pady=60, padx=30)
    elif option.strip()=="Mumbai":
        movieclicked()
        mth.place(x=0,y=100)
        time2.place(x=500,y=180)
        time4.place(x=500,y=380)
        tab.pack(pady=60, padx=30)
        print("changed")

def movieclicked2(e):
    global option,movie_selected
    movie_selected="bhool bhulaiya 3"
    if option=="":
        back()
        confirm_location()
        print("worked")
    elif option.strip()=="Delhi-NCR":
        movieclicked()
        th1.place(x=0,y=100)
        th2.place(x=0,y=300)
        time1.place(x=400,y=180)
        time3.place(x=400,y=380)
        tab.pack(pady=60, padx=30)
    elif option.strip()=="Mumbai":
        movieclicked()
        mth.place(x=0,y=100)
        time2.place(x=500,y=180)
        time4.place(x=500,y=380)
        tab.pack(pady=60, padx=30)
        print("changed")


def movieclicked3(e):
    global option,movie_selected
    movie_selected="Pushpa 2"
    if option=="":
        back()
        confirm_location()
        print("worked")
    elif option.strip()=="Delhi-NCR":
        movieclicked()
        th1.place(x=0,y=100)
        th2.place(x=0,y=300)
        time1.place(x=400,y=180)
        time3.place(x=400,y=380)
        tab.pack(pady=60, padx=30)
    elif option.strip()=="Mumbai":
        movieclicked()
        mth.place(x=0,y=100)
        time2.place(x=500,y=180)
        time4.place(x=500,y=380)
        tab.pack(pady=60, padx=30)
        print("changed")

def movieclicked4(e):
    global option,movie_selected
    movie_selected="Baby John"
    if option=="":
        back()
        confirm_location()
        print("worked")
    elif option.strip()=="Delhi-NCR":
        movieclicked()
        Bjframe.configure(fg_color="white")
        th1.place(x=0,y=100)
        th2.place(x=0,y=300)
        time1.place(x=400,y=180)
        time3.place(x=400,y=380)
        tab.pack(pady=60, padx=30)
    elif option.strip()=="Mumbai":
        Bjframe.configure(fg_color="white")
        movieclicked()
        mth.place(x=0,y=100)
        time2.place(x=500,y=180)
        time4.place(x=500,y=380)
        tab.pack(pady=60, padx=30)
        print("changed")


print(frame)
#Images 

QR=CTkImage(Image.open('My QR CODE.png'),size=(400,500))

background_image =CTkImage(Image.open("whitegradient .png"), size=(win.winfo_screenwidth(), win.winfo_screenheight()))
Cinema_image=CTkImage(Image.open('cinema.png'),size=(1536,864))

Movie1=CTkImage(Image.open('Movie1.png'),size=(300,400))
Movie2=CTkImage(Image.open('Movie2.jpg'),size=(300,400))
Movie3=CTkImage(Image.open('Movie3.png'),size=(300,400))
Movie4=CTkImage(Image.open('Movie4.png'),size=(300,400))

infos=CTkImage(Image.open('sinfo.png'),size=(300,400))
infob=CTkImage(Image.open('Binfo.png'),size=(300,390))
infoP=CTkImage(Image.open('Pinfo.png'),size=(300,400))
infoBJ=CTkImage(Image.open('Bjinfo.png'),size=(300,390))


blank=CTkImage(Image.open('Home.png'),size=(win.winfo_screenwidth(), win.winfo_screenheight()))
bannerS=CTkImage(Image.open('MovieBanner1.png'),size=(900,430))
banner=CTkImage(Image.open('Binfo.png'),size=(600,330))

mtheater=CTkImage(Image.open('MumTheater.png'),size=(1234,567))
theater1=CTkImage(Image.open('theater1.png'),size=(1543,750))
theater2=CTkImage(Image.open('theater2.png'),size=(1543,750))

advert=CTkImage(Image.open('Movie_banner.png'),size=(1300,150))

#background 
background_label = CTkLabel(win, image=background_image, text="")
background_label.place(relwidth=1, relheight=1) 

banner_label=CTkFrame(win, width=1536, height=500,corner_radius=15,fg_color="purple",bg_color='white')

advertf=CTkLabel(win,image=advert,fg_color="purple",bg_color='white',text="")
advertf.place(x=110,y=130)


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




#Movie 2 widgets (BB3) 

bframe=CTkFrame(win, width=310, height=410,corner_radius=15,fg_color="purple",bg_color='white')
bframe.place(x=795,y=295)
BB3=CTkLabel(win,image=Movie2,text='',fg_color="purple",bg_color='purple')
BB3.place(x=800,y=300)
BB3.bind("<Button-1>",movieclicked2)
#animation
BB3.bind("<Leave>",LeaveBB3)
BB3.bind("<Enter>",EnterBB3)



#Movie 3 widgets 
Pushframe=CTkFrame(win, width=310, height=410,corner_radius=15,fg_color="purple",bg_color='white')
Pushframe.place(x=45+380,y=295)
Pushpa=CTkLabel(win,image=Movie3,text='',fg_color="purple")
Pushpa.place(x=50+380,y=300)
Pushpa.bind("<Button-1>",movieclicked3)
#animation
Pushpa.bind("<Leave>",LeavePush)
Pushpa.bind("<Enter>",EnterPush)


#Movie4
Bjframe=CTkFrame(win, width=310, height=410,corner_radius=15,fg_color="purple",bg_color='white')
Bjframe.place(x=795+380,y=295)
Bjohn=CTkLabel(win,image=Movie4,text='',fg_color="purple")
Bjohn.place(x=800+380,y=300)
Bjohn.bind("<Button-1>",movieclicked4)
#animation
Bjohn.bind("<Leave>",Leavebj)
Bjohn.bind("<Enter>",Enterbj)



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
mth=CTkLabel(date1,image=mtheater,text='',fg_color='white')
#Time slot

time1=CTkButton(date1,command=lambda:open_seat('10:30 am'),text='10:30 am',font=("Arial", 26),fg_color='lightgray',text_color="Black",bg_color="white",hover_color="gray",corner_radius=5)
time2=CTkButton(date1,command=lambda:open_seat('02:00 pm'),text='01:00 pm',font=("Arial", 26),fg_color='lightgray',text_color="Black",bg_color="white",hover_color="gray",corner_radius=5)
time3=CTkButton(date1,command=lambda:open_seat('09:00 pm'),text='09:00 pm',font=("Arial", 26),fg_color='lightgray',text_color="Black",bg_color="white",hover_color="gray",corner_radius=5)
time4=CTkButton(date1,command=lambda:open_seat('08:00 pm'),text='08:00 pm',font=("Arial", 26),fg_color='lightgray',text_color="Black",bg_color="white",hover_color="gray",corner_radius=5)

#Home widgets 


button=CTkButton(win,text="   "+customer+"  ",font=(("Arial"),20),fg_color="purple",bg_color='white',command=register)
button.place(x=1234,y=12)

back_button=CTkButton(win,text="back",font=(("Arial"),20),fg_color="purple",bg_color='white',command=back)
back_button.place()


a="                                                                         "

options=["Mumbai  "+a ,"Delhi-NCR "+a]
dropdown = CTkOptionMenu(win, values=options,font=(("Arial"),20), command=opt,fg_color="violet",bg_color="white",button_color="violet",button_hover_color="purple")
dropdown.set("  Select your City"+a) 
dropdown.place(x=500,y=12)

#contact=CTkLabel(master=background_label,text="Contact",font=("arial",20),text_color="black",fg_color="#f5f5f5")
#contact.place(x=400,y=70)

book=CTkButton(win,command=book_confirm,text="Confirm Booking",font=(("TimesNewRoman"),30),fg_color="purple",bg_color='white')


back_time=CTkButton(win,text="back",font=(("Arial"),20),fg_color="purple",bg_color='white',command=seat_back)
seat_frame=CTkFrame(win, width=510, height=510,corner_radius=15,fg_color="purple",bg_color='white')
seat_label=CTkLabel(win,text="Seat selected:None",font=("Timesnewroman",20),text_color="black")

#Info label
binfo=CTkLabel(win,image=infob,fg_color="purple",bg_color="purple",text="")
binfo.place()
Bjohninfo=CTkLabel(win,image=infoBJ,fg_color="purple",bg_color="purple",text="")
Bjohninfo.place()
Pushinfo=CTkLabel(win,image=infoP,fg_color="purple",bg_color="purple",text="")
Pushinfo.place()
sinfo=CTkLabel(win,image=infos,fg_color="purple",bg_color="purple",text="")
sinfo.place()

seat_notselected=CTkLabel(win,text="No Seats are Selected",font=("Timesnewroman",20),text_color="black")

QRcode=CTkLabel(win,image=QR,text='',fg_color="white")
QRbutton=CTkButton(win,command=back,text="Back to Home ",font=("TimesNewRoman",20))


if customer!="":
    win.mainloop()

#1234x567
