import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "darkweb",
    database = "Hellow"
)
data = db.cursor()
# data.execute("SELECT * FROM Mc_School")
# print(data.fetchone())
# print(data.fetchall())
# for i in data:
#     print(i)
# data.execute("SELECT * FROM Mc_School WHERE roll_no = 20")
# data.execute("SELECT name,father_name FROM Mc_School WHERE roll_no = 18")
# for i in data:
#     print(i)
name = input("Enter name: ")
Q1 = f"SELECT * FROM Mc_School WHERE name = '{name.capitalize()}'"
data.execute(Q1)
for i in data:
    print(i)