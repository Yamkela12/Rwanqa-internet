import mysql.connector

#creating database object connection along with database selection
mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "SummativeDB" # database name 
)

#print(mdb)
#creating database object connection
mycursor = mydb.cursor()

mycursor.execute("drop table if exists students")
print("table deleted") 

#creating table and columns
mycursor.execute("""create table students(id int auto_increment primary key,
                name varchar(25), email varchar(25), age varchar(25), mobile varchar(10))""")
print("table created")

#inserting values into table
sql =  "insert into students(name, email, age, mobile) values(%s , %s, %s, %s)"
val = ('Yamkela', 'rwanqayamkela@gmail.com', '27', '0781886167'), ('thando', 'thando@gmail.com', '27', '0841243567'), ('Busi', 'bvmkhize94@gmail.com', '29', '0679263708'), ('Sanle', 'sanele26@gmail.com', '15', '0812345697'),('Lindoer', 'junior@gmail.com', '33', '0712345678')

#executing sql commands 
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "records were inserted")
mydb.close()