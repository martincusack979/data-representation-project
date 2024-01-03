import mysql.connector

# connect to database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dvds"
)

cursor = db.cursor()
sql="insert into dvds (title, director, year, price) values (%s,%s,%s,%s)"
values = ("The Shining", "Stanley Kubrick", 1980, 20)

cursor.execute(sql, values)

db.commit()
print("record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()