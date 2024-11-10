from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector 
win=CTk()

win.geometry('600x400')
win.title('Log-in')
set_appearance_mode('dark')
set_default_color_theme('green')





x=0
def welcome():
    global x 
    a="Welcome to <Name> "
    wel.configure(text=str(wel.cget("text")+a[x]))
    x+=1
    if x<=len(a):
        wel.after(80,welcome)
    

frame = CTkFrame(win, width=300, height=400,corner_radius=15)
def starts():
    Ssub.place(x=200,y=280)
    frame.place(x= 150, y=50)
    #~~~~~~~~~~~~~~~~~~~~~~~
    user.place(x=170,y=180)
    sign.place(x=245,y=110)
    pas.place(x=170,y=220)
    username.place(x=270,y=180)
    password.place(x=270,y=220)
    #~~~~~~~~~~~~~~~~~~~~~~~
    login.place(x=-1100,y=180)
    signup.place(x=-2110,y=180)
    bk.place(x=450,y=400) 
    wel.place(x=150,y=-1100)
    win.geometry('600x500')
def startl():
    #~~~~~~~~~~~~~~~~~~~~~~~
    Lsub.place(x=200,y=280)
    frame.place(x=150, y=50)
    log.place(x=260,y=110)
    user.place(x=170,y=180)
    pas.place(x=170,y=220)
    username.place(x=270,y=180)
    password.place(x=270,y=220)
    #~~~~~~~~~~~~~~~~~~~~~~~
    login.place(x=-1000,y=180)
    signup.place(x=-8210,y=180)
    bk.place(x=450,y=400) 
    win.geometry('600x500')
    wel.place(x=-1150,y=100)
def back():
    Ssub.place(x=-2200,y=280)
    Lsub.place(x=-2200,y=280)
    wel.place(x=150,y=100)
    user.place(x=150,y=180)
    frame.place(x=-100000,y=2)
    log.place(x=200,y=-999)
    sign.place(x=200,y=-990)
    pas.place(x=-1150,y=220)
    login.place(x=150,y=180)
    signup.place(x=320,y=180)   
    username.place(x=-150,y=180)
    password.place(x=-200,y=180)
    bk.place(x=-200,y=200)
    win.geometry('600x400')

def submit(log):
    db = mysql.connector.connect(host="localhost",user="root",password="varchasva",database='Info')
    cursor=db.cursor()
    Email=username.get()
    Password=password.get()
    try:
        cursor.execute('create table Customerinformation( Email varchar(50) Primary key ,Password varchar(50))')
    except:
        pass
    if log=="Sign-in":
        try:
            cursor.execute('insert into Customerinformation values("'+Email+'",'+'"'+Password+'")')
        except:
            print('ERrrrrr-OR')
    elif log=="Login":
        cursor.execute("select * from Customerinformation")
        for i in cursor:
            if (Email,Password) in i:
                pass
            else:
                print("User does not exist") 
        


wel=CTkLabel(win,text=" ",font=("Comic sans",30))
wel.place(x=150,y=100)

log=CTkLabel(win,text="Log In",font=('TimesNewRoman',27),)
sign=CTkLabel(win,text="Register",font=('TimesNewRoman',27),)

username=CTkEntry(win)
user=CTkLabel(win,text="Enter Email",font=('Arial',13))
password=CTkEntry(win,show="*") 
pas=CTkLabel(win,text='Password',font=('Arial',13))

login=CTkButton(win,text=" Log-in" ,hover_color="blue",font=('Arial',16),corner_radius=32,command=lambda:startl())
signup=CTkButton(win,text=" Sign-up",hover_color="blue",font=('Arial',16),corner_radius=32,command=lambda:starts())
login.place(x=150,y=180)
signup.place(x=320,y=180)

bk=CTkButton(win,text='Back',hover_color="blue",font=('Arial',18),corner_radius=32,command=lambda:back())
bk.place()

Lsub=CTkButton(master=frame,text="Submit ",font=('Arial',18),corner_radius=32,command=lambda:submit('Login'))
Ssub=CTkButton(win,text="Submit",font=('Arial',18),corner_radius=32,command=lambda:submit("Sign-in"))

welcome()
win.mainloop()
