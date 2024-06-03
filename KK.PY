import mysql.connector

d=mysql.connector.connect(host='localhost',user='root',password='',database='smit')
print("connected...")
s=d.cursor()

# s.execute("update f set name='ram' where id=2")
# print("insertedd...")
# s.execute("select * from f")
# r=s.fetchall()
s.execute("show tables")
for i in s:
    print(i)
d.commit()