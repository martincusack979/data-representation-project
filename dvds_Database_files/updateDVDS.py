import mysql.connector

# connect to database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dvds"
)

cursor = db.cursor()
sql="update dvds set title= %s, director=%s, year=%s, price=%s  where id = %s"
values = ("The Shining","Stanley Kubrick", 1980, 20, 1)

cursor.execute(sql, values)

db.commit()
print("all done")

cursor.close()
db.close()