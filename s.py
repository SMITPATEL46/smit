import mysql.connector

s=mysql.connector.connect(host='localhost',user='root',password='',database='smit')
print("doon")

c=s.cursor()

c.execute("insert into r values(2,'raj')")
print("doon")
c.execute("select * from r")
r=c.fetchall()
for i in r:
    print(i)

s.commit()