import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "darkweb",
    database = "Hellow"
)
data = db.cursor()
# data.execute("ALTER TABLE Mc_School ADD COLUMN gender VARCHAR(20)")
# data.execute("ALTER TABLE Mc_School RENAME COLUMN gender TO father_name")
data.execute("ALTER TABLE Mc_School DROP father_name")
