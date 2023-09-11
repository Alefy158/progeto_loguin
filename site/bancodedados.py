import sqlite3


def criar_tabela():
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()


def adicionar_usuario(nome, data, email, senha):
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO usuarios (nome, data, email, senha) VALUES (?, ?, ?, ?)", (nome, data, email, senha))

    conexao.commit()
    conexao.close()


def listar_usuarios():
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, data: {usuario[2]}, email: {usuario[3]}, senha: {usuario[4]}")

    conexao.close()


def loguin(email, senha):
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    emv = False

    for usuario in usuarios:
        if email == usuario[3]:
            emv = True
            if senha == usuario[4]:
                return True, usuario[1]
            else:
                emv = False
    if emv == False:
        emv = "senha_not"
        return emv


if __name__ == "__main__":
    criar_tabela()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar Usuário")
        print("2 - Listar Usuários")
        print("3 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome:")
            data = input('data:')
            email = input("Email:")
            senha = input('senha')
            adicionar_usuario(nome, data, email, senha)
            print("Usuário adicionado com sucesso!")

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            break
