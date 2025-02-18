from conexao import conectar

def criar_tabelas():
    mydb = conectar()
    if mydb:
        cursor = mydb.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS candidatos (
                matricula INT PRIMARY KEY NOT NULL,
                nome_candidato VARCHAR(255) NOT NULL,
                votos INT DEFAULT 0
            )
        """)
        print("Tabela verificada/criada com sucesso!")
        cursor.close()
        mydb.close()

if __name__ == "__main__":
    criar_tabelas()
