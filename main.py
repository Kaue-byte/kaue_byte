from flask import Flask, render_template, request, jsonify, redirect, url_for
from conexao import conectar
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home_vota.html")

@app.route('/get_buttons')
def get_buttons():
    try:
        mydb = conectar() 
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT nome_candidato, matricula FROM candidatos;")
        candidatos = mycursor.fetchall()  

        if not candidatos:
            return jsonify({"error": "Nenhum candidato encontrado"}), 404

        botoes = [{"nome": candidato[0], "matricula": candidato[1]} for candidato in candidatos] 
        
        return jsonify(botoes)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

@app.route('/receber', methods=['POST'])
def receber():
    mydb = None
    mycursor = None
    try:
        # 🚀 Verifica se a requisição contém JSON

        data = request.get_json()
        matricula = data['matricula']
        
        mydb = conectar()
        mycursor = mydb.cursor()
        
        sql = "UPDATE candidatos SET votos = votos + 1 WHERE matricula = %s"
        mycursor.execute(sql, (matricula,))
        mydb.commit()

        if mycursor.rowcount == 0:
            return jsonify({"error": "Candidato não encontrado"}), 404

        return jsonify({"message": "Voto registrado com sucesso!", "redirect": url_for('voto_feito')})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if mycursor is not None:
            mycursor.close()
        if mydb is not None:
            mydb.close()

@app.route("/voto_feito")
def voto_feito():
    return render_template("voto_feito.html")  # Criar esta página no seu projeto

@app.route('/get_votos')
def get_votos():
    try:
        mydb = conectar()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT nome_candidato, votos FROM candidatos;")
        candidatos = mycursor.fetchall()

        if not candidatos:
            return jsonify({"error": "Nenhum candidato encontrado"}), 404

        return jsonify([{"nome": c[0], "votos": c[1]} for c in candidatos])

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    try:
        data = request.get_json()
        nome_candidato = data['nome_candidato']
        matricula = data['matricula']

        mydb = conectar()
        mycursor = mydb.cursor()

        sql = "INSERT INTO candidatos (nome_candidato, matricula, votos) VALUES (%s, %s, 0)"
        mycursor.execute(sql, (nome_candidato, matricula))
        mydb.commit()

        return jsonify({"message": "Candidato cadastrado com sucesso!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

@app.route('/get_candidatos')
def get_candidatos():
    """Retorna todos os candidatos do banco"""
    try:
        mydb = conectar()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT nome_candidato, matricula FROM candidatos;")
        candidatos = mycursor.fetchall()

        return jsonify([{"nome": c[0], "matricula": c[1]} for c in candidatos])

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()


@app.route('/deletar', methods=['POST'])
def deletar():
    """Deleta um candidato pelo número de matrícula"""
    try:
        data = request.get_json()
        matricula = data['matricula']

        mydb = conectar()
        mycursor = mydb.cursor()

        sql = "DELETE FROM candidatos WHERE matricula = %s"
        mycursor.execute(sql, (matricula,))
        mydb.commit()

        if mycursor.rowcount == 0:
            return jsonify({"error": "Candidato não encontrado"}), 404

        return jsonify({"message": "Candidato deletado com sucesso!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()



if __name__ == "__main__":
    app.run(debug=True)
