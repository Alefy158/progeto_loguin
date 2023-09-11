from flask import Flask, render_template, request
from bancodedados import adicionar_usuario, criar_tabela, loguin

site = Flask(__name__)


@site.route('/static/<path:filename>')
@site.route("/")
def index():
    return render_template('loguin.html')


# abre o site


@site.route('/enviar', methods=['post'])
def loguim():
    email = request.form['email']
    senha = request.form['senha']
    log = loguin(email, senha)
    if log == 'senha_not':
        return 'senha incorreta'
    elif log == False:
        return render_template('registro.html')
    elif log[0] == True:
        nome = log[1]
        print(log)
        return render_template('usuario.html', nome=nome)


# loguin


@site.route('/registro', methods=['GET', 'POST'])
def nao_registrado():
    if request.method == 'POST':
        return render_template('registro.html')
    return render_template('registro.py')


# botao de registro


@site.route("/cadastro", methods=['post'])
def registro():
    nome = request.form['nome']
    data = request.form['data']
    email = request.form['email']
    senha = request.form['senha']
    criar_tabela()
    adicionar_usuario(nome, data, email, senha)
    return nome


if __name__ == "__main__":
    site.run(host='0.0.0.0', port=8000, debug=True)
