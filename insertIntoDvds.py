import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dvds"
)

cursor = db.cursor()
sql="insert into dvds (title, director, year, price) values (%s,%s, %s, %s)"
values = ("Blue Velvet", "David Lynch", 1986, 28)

cursor.execute(sql, values)

db.commit()
print("record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()