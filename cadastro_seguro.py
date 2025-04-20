import sqlite3
import bcrypt

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL
)
''')
conn.commit()

def cadastrar_usuario(nome, email, senha):
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    try:
        cursor.execute('INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)', (nome, email, senha_hash))
        conn.commit()
        print("Usuário cadastrado com segurança!")
    except sqlite3.IntegrityError:
        print("Erro: E-mail já cadastrado.")

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")
cadastrar_usuario(nome, email, senha)

conn.close()