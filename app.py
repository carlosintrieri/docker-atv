from flask import Flask, render_template, request, redirect, url_for, flash
import MySQLdb.cursors
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'carlos123'

# Configurações do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'carlos'
app.config['MYSQL_DB'] = 'contato'

mysql = MySQL(app)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST' and all(field in request.form for field in ['nome', 'email', 'senha', 'confirmar_senha']):
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']

        # Verifica se as senhas coincidem
        if senha != confirmar_senha:
            flash('As senhas não coincidem!', 'danger')
        else:
            try:
                # Inserindo os dados no banco de dados
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
                mysql.connection.commit()
                cursor.close()
                flash('Você se registrou com sucesso!', 'success')
                return redirect(url_for('contato'))
            except MySQLdb.Error as e:
                flash(f'Ocorreu um erro no registro: {str(e)}', 'danger')

    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cardapio")
def cardapio():
    return render_template('cardapio.html')

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')

@app.route("/tinto1")
def tintoum():
    return render_template('tinto1.html')

@app.route("/tinto2")
def tintodois():
    return render_template('tinto2.html')

@app.route("/tinto3")
def tintotres():
    return render_template('tinto3.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
