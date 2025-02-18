import mysql.connector

def conectar():
    try:
        mydb = mysql.connector.connect(
            host="metro.proxy.rlwy.net",  # Host do Railway
            user="root",  # Usuário do Railway
            password="NWqLfnRFkeQDLvIVsoLYnSXrjFYnPtLq",  # Senha do Railway
            database="railway",  # Nome do banco de dados
            port=19986  # Porta do Railway
        )
        print("Conexão bem-sucedida!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None



# Testando a conexão
conexao = conectar()
if conexao:
    conexao.close()
