import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "darkweb",
    database = "Hellow"
)

data = db.cursor()
data.execute("CREATE TABLE Mc_School(ID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age SMALLINT UNSIGNED, class VARCHAR(20))")
data.execute("INSERT INTO Mc_School(name,age,class) VALUES(%s,%s,%s)",("Usama",14,"9th"))
data.execute("INSERT INTO Mc_School(name,age,class) VALUES(%s,%s,%s)",("Iqrq",30,"Ma Education"))
data.execute("INSERT INTO Mc_School(name,age,class) VALUES(%s,%s,%s)",("Sarim ali khan",10,"PG"))
db.commit()