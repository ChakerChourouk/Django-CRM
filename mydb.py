import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

dataBase = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD")
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")
