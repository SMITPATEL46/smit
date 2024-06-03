import mysql.connector

c=mysql.connector.connect(host='localhost',user='root',password='',database='student')

db=c.cursor()
# db.execute("create database student")
print("doon")
db.execute("CREATE TABEL data(id int, name varcher(20))")


print("doon")
c.commit()