import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "darkweb",
    database = "Hellow"
)

data = db.cursor()
# data.execute("CREATE TABLE Mc_School(ID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,roll_no INT UNSIGNED,name VARCHAR(50),father_name VARCHAR(50) ,date_of_birth VARCHAR(20))")
# data.execute("INSERT INTO Mc_School(roll_no,name,father_name,date_of_birth) VALUES(%s,%s,%s,%s)",(11,"Usama Amjid","Amjid Ali","16-september-2000"))
# data.execute("INSERT INTO Mc_School(roll_no,name,father_name,date_of_birth) VALUES(%s,%s,%s,%s)",(15,"Sarim Ali Khan","Ali Khan","02-january-2002"))
# data.execute("INSERT INTO Mc_School(roll_no,name,father_name,date_of_birth) VALUES(%s,%s,%s,%s)",(20,"Ali Rasheed","Rasheed","22-june-1997"))
# data.execute("INSERT INTO Mc_School(roll_no,name,father_name,date_of_birth) VALUES(%s,%s,%s,%s)",(18,"Sohaib","Rana Ijaz","28-Agust-2005"))
# data.execute("INSERT INTO Mc_School(roll_no,name,father_name,date_of_birth) VALUES(%s,%s,%s,%s)",(24,"Ahsan","Yaseen","06-March-2001"))
# data.execute("INSERT INTO Mc_School(name,age,class) VALUES(%s,%s,%s)",("Iqrq",30,"Ma Education"))
# data.execute("INSERT INTO Mc_School(name,age,class) VALUES(%s,%s,%s)",("Sarim ali khan",10,"PG"))
# db.commit()