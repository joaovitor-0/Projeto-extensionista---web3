from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def gerenciar_despesas(request):
    # 1. FUNÇÃO DE ADICIONAR (INSERT)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        data = request.POST.get('data')

        try:
            with connection.cursor() as cursor:
                # Garante que a tabela existe no banco
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS DESPESAS (
                        ID_DESPESA INT PRIMARY KEY AUTO_INCREMENT,
                        NOME VARCHAR(100) NOT NULL,
                        PRECO DECIMAL(10, 2) NOT NULL,
                        DATA_DESPESA DATE NOT NULL
                    )
                """)
                # Executa o INSERT
                cursor.execute(
                    "INSERT INTO DESPESAS (NOME, PRECO, DATA_DESPESA) VALUES (%s, %s, %s)",
                    [nome, preco, data]
                )
            messages.success(request, "Despesa adicionada com sucesso!")
            return redirect('despesas')  # Evita reenvio do formulário ao atualizar a página
        except Exception as erro:
            messages.error(request, f"Erro ao adicionar despesa: {erro}")

    # 2. FUNÇÃO DE CONSULTA (SELECT)
    lista_despesas = []
    try:
        with connection.cursor() as cursor:
            # Busca as despesas ordenando da mais recente para a mais antiga
            cursor.execute("SELECT ID_DESPESA, NOME, PRECO, DATA_DESPESA FROM DESPESAS ORDER BY DATA_DESPESA DESC")
            lista_despesas = cursor.fetchall()
    except Exception:
        # Se a tabela ainda não existir, ignora o erro e retorna uma lista vazia
        pass

    return render(request, 'controleDespesas.html', {'despesas': lista_despesas})


# 3. FUNÇÃO DE REMOVER (DELETE)
@login_required(login_url='/login/')
def remover_despesa(request, id_despesa):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM DESPESAS WHERE ID_DESPESA = %s", [id_despesa])
        messages.success(request, "Despesa removida com sucesso!")
    except Exception as erro:
        messages.error(request, f"Erro ao remover: {erro}")

    return redirect('despesas')