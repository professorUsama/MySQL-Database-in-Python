import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "darkweb",
    database = "college"
)
data = db.cursor()
std_names = ["Usama","Ali","Mohsin","Sarim","Shakeel"]
std_data = [
    ("Amjid Ali",9,22,"BsCs"),
    ("Rasheed",5,20,"Bscs"),
    ("Abbas ",11,21,"Bs English"),
    ("Ali Khan",4,18,"Bs Zology"),
    ("Anjum",25,18,"Bs Urdu")
]
# for name_data, name in enumerate(std_names):
#     data.execute(f"INSERT INTO Students(name) VALUES('{name}')")
#     data.execute("INSERT INTO Students_records(father_name,roll_no,age,department) VALUES(%s,%s,%s,%s)",std_data[name_data])
# db.commit()
Q1 = "select name,father_name,roll_no,age,department from students inner join students_records on students_records.id = students.id"
data.execute(Q1)
for data in data:
    print(data)