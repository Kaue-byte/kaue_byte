from conexao import conectar

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