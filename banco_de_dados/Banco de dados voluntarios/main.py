import mysql.connector
from datetime import datetime

import tkinter as tk
from tkinter import messagebox

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor = conexao.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS Gavime')
cursor.execute('USE Gavime')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS INSCRITOS (
        ID_VOLUNTARIO INT PRIMARY KEY AUTO_INCREMENT,
        NOME VARCHAR(100) NOT NULL,
        EMAIL VARCHAR(100) NOT NULL UNIQUE,
        TELEFONE VARCHAR(20),
        DATA_INSCRICAO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

class Voluntario:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__data_atual = datetime.now()

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            print("Nome inválido.")

    def get_email(self):
        return self.__email

    def set_email(self, novo_email):
        if isinstance(novo_email, str) and len(novo_email) > 0:
            self.__email = novo_email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, novo_telefone):
            self.__telefone = novo_telefone

    def get_data_atual(self):
        return self.__data_atual

    def set_data_atual(self, data_atual):
        self.__data_atual = data_atual


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Gavime - Cadastro de Voluntários")
        self.master.geometry("400x350")


        self.titulo_sistema = tk.Label(self.master, text="Inscrição de Voluntário", font=("Arial", 16, "bold"))
        self.titulo_sistema.pack(pady=(0, 20))

        self.label_nome = tk.Label(self.master, text="Nome Completo:")
        self.label_nome.pack(anchor="w")
        self.entry_nome = tk.Entry(self.master, width=40)
        self.entry_nome.pack(pady=(0, 10))

        self.label_email = tk.Label(self.master, text="E-mail:")
        self.label_email.pack(anchor="w")
        self.entry_email = tk.Entry(self.master, width=40)
        self.entry_email.pack(pady=(0, 10))

        self.label_telefone = tk.Label(self.master, text="Telefone:")
        self.label_telefone.pack(anchor="w")
        self.entry_telefone = tk.Entry(self.master, width=40)
        self.entry_telefone.pack(pady=(0, 20))

        self.botao_salvar = tk.Button(self.master, text="Enviar Inscrição", command=self.salvar_voluntario)
        self.botao_salvar.pack()

    def salvar_voluntario(self):
        nome_da_tela = self.entry_nome.get()
        email_da_tela = self.entry_email.get()
        telefone_da_tela = self.entry_telefone.get()

        if not nome_da_tela or not email_da_tela:
            messagebox.showwarning("Campos Obrigatórios", "Por favor, preencha Nome e E-mail.")
            return

        novo_voluntario = Voluntario(nome_da_tela, email_da_tela, telefone_da_tela)

        comando_sql = "INSERT INTO INSCRITOS (NOME, EMAIL, TELEFONE) VALUES (%s, %s, %s)"
        valores = (novo_voluntario.get_nome(), novo_voluntario.get_email(), novo_voluntario.get_telefone())

        cursor.execute(comando_sql, valores)
        conexao.commit()

        messagebox.showinfo("Sucesso!", f"Voluntário {novo_voluntario.get_nome()} cadastrado com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)


if __name__ == "__main__":
    Janela = tk.Tk()
    meu_app = App(Janela)
    Janela.mainloop()
