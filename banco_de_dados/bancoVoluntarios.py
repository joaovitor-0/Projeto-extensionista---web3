from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from datetime import datetime


class Voluntario:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__data_atual = datetime.now()

    def get_nome(self): return self.__nome

    def get_email(self): return self.__email

    def get_telefone(self): return self.__telefone

    def get_data_atual(self): return self.__data_atual


def inscricao_voluntario(request):
    if request.method == 'POST':
        nome_da_tela = request.POST.get('nome')
        email_da_tela = request.POST.get('email')
        telefone_da_tela = request.POST.get('telefone')

        if not nome_da_tela or not email_da_tela:
            messages.warning(request, "Por favor, preencha Nome e E-mail.")
            return render(request, 'inscricao.html')

        # Instancia o objeto usando sua classe
        novo_voluntario = Voluntario(nome_da_tela, email_da_tela, telefone_da_tela)

        try:
            with connection.cursor() as cursor:
                # Script de criação da tabela caso ela não exista (executa na primeira requisição)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS INSCRITOS (
                        ID_VOLUNTARIO INT PRIMARY KEY AUTO_INCREMENT,
                        NOME VARCHAR(100) NOT NULL,
                        EMAIL VARCHAR(100) NOT NULL UNIQUE,
                        TELEFONE VARCHAR(20),
                        DATA_INSCRICAO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)

                # Executa o INSERT
                comando_sql = "INSERT INTO INSCRITOS (NOME, EMAIL, TELEFONE) VALUES (%s, %s, %s)"
                valores = (novo_voluntario.get_nome(), novo_voluntario.get_email(), novo_voluntario.get_telefone())
                cursor.execute(comando_sql, valores)

            # Mensagem de sucesso
            messages.success(request, f"Voluntário {novo_voluntario.get_nome()} cadastrado com sucesso!")
            return redirect('inscricao')  # Recarrega a página limpa (substitui o limpar_campos)

        except Exception as erro:
            messages.error(request, f"Erro ao salvar no banco de dados: {erro}")
            return render(request, 'inscricao.html')

    # Se for GET, apenas exibe a tela com o formulário limpo
    return render(request, 'inscricao.html')


# 2. NOVA FUNÇÃO DE CONSULTA (Faz o SELECT e lista os inscritos)
def consultar_inscritos(request):
    try:
        with connection.cursor() as cursor:
            # Executa o SELECT na tabela
            cursor.execute(
                "SELECT ID_VOLUNTARIO, NOME, EMAIL, TELEFONE, DATA_INSCRICAO FROM INSCRITOS ORDER BY ID_VOLUNTARIO DESC")
            # fetchall() captura todas as linhas encontradas
            lista_inscritos = cursor.fetchall()

    except Exception as erro:
        messages.error(request, f"Erro ao consultar o banco: {erro}")
        lista_inscritos = []

    # Envia a lista de voluntários obtida do banco diretamente para a página de consulta
    return render(request, 'consultaVoluntarios.html', {'inscritos': lista_inscritos})