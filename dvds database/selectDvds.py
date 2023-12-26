import mysql.connector

# connect to database

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dvds"
)

cursor = db.cursor()
# to select all values in dvds
sql="select * from dvds"

cursor.execute(sql)
result = cursor.fetchall()
for x in result:
  print(x)

db.close()
cursor.close()