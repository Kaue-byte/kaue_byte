import mysql.connector
import os

# Pegando os dados do banco das variáveis de ambiente
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    if conn.is_connected():
        print("✅ Conexão com o banco de dados bem-sucedida!")
except mysql.connector.Error as err:
    print(f"❌ Erro ao conectar no banco: {err}")
