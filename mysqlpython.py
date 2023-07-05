
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username ="root",
    password = ""
)

mycursor = mydb.cursor()

mycursor.execute("create database summativeDB")
print("database created")