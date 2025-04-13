import mysql.connector
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

#connect to database   

db = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="password",
    database="todo_db"
)

cursor = db.cursor()
cursor.execute("Show Tables")

for table in cursor:
    print(table)