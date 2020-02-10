import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="123456",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)