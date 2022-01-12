import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "darkweb"
)

data = db.cursor()

data.execute("SHOW DATABASES")
for i in data:
    print(i)
