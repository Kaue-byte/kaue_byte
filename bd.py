import os
import mysql.connector

# Configurações do banco a partir das variáveis de ambiente
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv(""),
    "database": os.getenv("DB_NAME"),
}

# Conecta ao bancos
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Lê o arquivo SQL
    with open("backup.sql", "r") as f:
        sql_script = f.read()
    
    # Executa o SQL
    for statement in sql_script.split(";"):
        if statement.strip():
            cursor.execute(statement)

    conn.commit()
    cursor.close()
    conn.close()
    print("Backup importado com sucesso!")
except mysql.connector.Error as e:
    print(f"Erro ao importar backup: {e}")
