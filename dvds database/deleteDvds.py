import mysql.connector

# connect to database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dvds"
)

cursor = db.cursor()
sql="delete from dvds where id = %s"
values = (1,)

cursor.execute(sql, values)

db.commit()
print("delete done")

cursor.close()
db.close()