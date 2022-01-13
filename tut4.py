import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "darkweb",
    database = "Hellow"
)

data = db.cursor()
# data.execute("CREATE DATABASE Hellow")
# data.execute("CREATE TABLE Students(name VARCHAR(50), dob VARCHAR(20), roll_no INT PRIMARY KEY)")
data.execute("DESCRIBE Students")
for i in data:
    print(i)