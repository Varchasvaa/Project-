import mysql.connector 


db = mysql.connector.connect(host="localhost",user="root",password="varchasva",database='Info')
cursor=db.cursor()    
cursor.execute("select Seats from booking_info where Movie='{0}' ".format('Pushpa 2'))
list=[]
for i in cursor:
    print(i)
    list.extend(i)
print(cursor)
print(list)
dic={"A6":1,"B2":3}
print("A6"in dic )