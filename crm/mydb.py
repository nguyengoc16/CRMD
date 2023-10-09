import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234567890!@qw'
)

cursorObject = database.cursor()

cursorObject.execute("DROP DATABASE CRMDB")

cursorObject.execute("CREATE DATABASE CRMDB")

print("DOnee")