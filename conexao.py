import mysql.connector


def conectar():
    try:
        mydb = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="",
            database="repre"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
