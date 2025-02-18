from conexao import conectar

def criar_tabelas():
    conexao = conectar()
    if conexao is None:
        print("Erro ao conectar ao banco. Saindo...")
        return

    cursor = conexao.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    );
    """
    
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    criar_tabelas()
