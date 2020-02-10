import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="123456"
)

print(mydb)

# install dnspython