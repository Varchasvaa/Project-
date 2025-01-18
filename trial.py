import mysql.connector


db = mysql.connector.connect(host="localhost",user="root",password="varchasva",database='Info')
cursor=db.cursor()

cursor.execute("select * from Customerinformation")
for i in cursor:
  #  print(i)
    print(i[0],i[1])