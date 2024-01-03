import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dvds"
)

cursor = db.cursor()
sql="CREATE TABLE dvds (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(100), director VARCHAR(100), year INT, price INT)"

cursor.execute(sql)
print ("all done")
db.close()
cursor.close()