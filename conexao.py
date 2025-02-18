import mysql.connector

def conectar():
    try:
        mydb = mysql.connector.connect(
            host="metro.proxy.rlwy.net",
            user="root",
            password="NWqLfnRFkeQDLvIVsoLYnSXrjFYnPtLq",
            database="railway",
            port=19986,
            ssl_disabled=True  
        )
        print("Conexão bem-sucedida!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
