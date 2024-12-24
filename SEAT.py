from customtkinter import * 
import mysql.connector 
win=CTk()
win.geometry('1000x1000')

rows=8
columns=8
seats={}
seat_frame=CTkFrame(win,corner_radius=15,fg_color="purple",bg_color='black')
seat_label=CTkLabel(win,text="Seat selected:None",font=("Timesnewroman",20))
seat_frame.pack()
def seat_select(s):
    print(s)
    button=seats[s]
    if button.cget('fg_color')=="lightgray":
        button.configure(fg_color="Green")
    elif button.cget('fg_color')=="Green":
        button.configure(fg_color="lightgray")



def seat_struc():
    for row in range(rows):
        for column in range(columns):
            SID=chr(65+row)+str(column+1)
            button=CTkButton(seat_frame,text=SID,fg_color="lightgray",text_color="Purple",font=("Timesnewroman",18),width=50,height=50,command=lambda s=SID:seat_select(s))
            button.grid(row=row,column=column,padx=5,pady=5)
            seats[SID]=button 
seat_struc()
win.mainloop()
'''
    popup = CTkToplevel(win)
    popup.geometry("500x500")
    popup.title("Seat number")  
    popup.grab_set()  
    popup.resizable(False, False)  
        
    label = CTkLabel(popup, text="Number of Seats U are looking for!", font=("Arial", 26))
    label.pack(pady=20)
        
    close_button = CTkButton(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    popup.transient(win)

def db():
    mydb = mysql.connector.connect(host="localhost",user="root",password="varchasva",database='Info')
    try:
        cursor=mydb.cursor()
        cursor.execute("Create table Booking_Info(Customer varchar(50),Movie varchar(25),Time varchar(20),Seats varchar(25))"  )
    except:
        mydb.close()
'''