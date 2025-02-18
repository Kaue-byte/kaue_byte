import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def conectar():
    try:
        mydb = mysql.connector.connect(
            host="DB_HOST", 
            user="DB_USER",
            password="DB_PASSWORD",
            database="DB_NAME"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
