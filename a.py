import mysql.connector
d=mysql.connector.connect(host="localhost",user="root",password="",database="smit")
print("connected")
s=d.cursor()
s.execute("creat table raj(id int, name varchar(20))")
print("table madded")
d.commit()