from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector

x=0
customer=""
def register():
    win=CTk()

    win.geometry('600x400')
    win.title('Log-in')
    set_appearance_mode('dark')
    set_default_color_theme('green')

    def welcome():
        global x 
        a="Welcome to <Name> "
        wel.configure(text=str(wel.cget("text")+a[x]))
        x+=1
        if x<=len(a):
            wel.after(80,welcome)
        

    frame = CTkFrame(win, width=300, height=400,corner_radius=15)
    def starts():
        Ssub.place(x=120,y=280)
        frame.place(x= 150, y=50)
        #~~~~~~~~~~~~~~~~~~~~~~~
        sign.place(x=110,y=80)
        user.place(x=20,y=150)
        pas.place(x=20,y=200)
        username.place(x=90,y=150)
        password.place(x=90,y=200)
        #~~~~~~~~~~~~~~~~~~~~~~~
        login.place(x=-1100,y=180)
        signup.place(x=-2110,y=180)
        bk.place(x=455,y=400)
        wel.place(x=150,y=-1100)
        win.geometry('600x500')
    def startl():
        #~~~~~~~~~~~~~~~~~~~~~~~
        Lsub.place(x=120,y=280)
        frame.place(x=150, y=50)
        log.place(x=110,y=80)
        user.place(x=20,y=150)
        pas.place(x=20,y=200)
        username.place(x=90,y=150)
        password.place(x=90,y=200)
        #~~~~~~~~~~~~~~~~~~~~~~~
        login.place(x=-1000,y=180)
        signup.place(x=-8210,y=180)
        bk.place(x=455,y=400) 
        win.geometry('600x500')
        wel.place(x=-1150,y=100)
    def back():
        Ssub.place(x=-110,y=-280)
        Lsub.place(x=-120,y=-280)
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
                cursor.execute('insert into Customerinformation values("'+Email.lower()+'",'+'"'+Password+'")')
                db.commit()
                starts()
            except:
                print('ERrrrrr-OR')
        elif log=="Login":
            cursor.execute("select * from Customerinformation")
            for i in cursor:
                print(i)
                if i[0]==Email.lower()and i[1]==Password:
                    global customer
                    customer=Email.lower().split("@")[0]
                    print(customer)
                    win.destroy()
                else:
                    print("User does not exist")
                
        db.commit()


    wel=CTkLabel(win,text=" ",font=("Comic sans",30))
    wel.place(x=150,y=100)

    log=CTkLabel(frame,text="Log In",font=('TimesNewRoman',27),)
    sign=CTkLabel(frame,text="Register",font=('TimesNewRoman',27),)

    username=CTkEntry(frame)
    user=CTkLabel(frame,text="Enter Email",font=('Arial',13))
    password=CTkEntry(frame,show="*") 
    pas=CTkLabel(frame,text='Password',font=('Arial',13))

    login=CTkButton(win,text=" Log-in" ,hover_color="blue",font=('Arial',16),corner_radius=32,command=lambda:startl())
    signup=CTkButton(win,text=" Sign-up",hover_color="blue",font=('Arial',16),corner_radius=32,command=lambda:starts())
    login.place(x=150,y=180)
    signup.place(x=320,y=180)

    bk=CTkButton(win,text='Back',hover_color="blue",font=('Arial',18),corner_radius=32,command=lambda:back())
    bk.place()

    Lsub=CTkButton(frame,text="Submit ",font=('Arial',18),corner_radius=32,command=lambda:submit('Sign-in'))
    Ssub=CTkButton(frame,text="Submit",font=('Arial',18),corner_radius=32,command=lambda:submit("Login"))


    welcome()
    win.mainloop()
 