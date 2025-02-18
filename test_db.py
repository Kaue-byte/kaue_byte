import mysql.connector

def alterar_tabela():
    try:
        mydb = mysql.connector.connect(
            host="metro.proxy.rlwy.net",
            user="root",
            password="NWqLfnRFkeQDLvIVsoLYnSXrjFYnPtLq",
            database="railway",
            port=19986
        )
        mycursor = mydb.cursor()

        # Comando para modificar a coluna nome_candidato
        sql = "ALTER TABLE candidatos MODIFY nome_candidato CHAR(255);"
        mycursor.execute(sql)

        mydb.commit()
        print("Tabela alterada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao alterar a tabela: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

# Chamando a função
alterar_tabela()
