import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="123456"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")