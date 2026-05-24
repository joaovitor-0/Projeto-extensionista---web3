from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib import messages
from .models import Inscrito, Atividade, Participacao, Transparencia
from django.db.models import Sum


def index(request):
    return render(request, 'index.html')

def doacoes(request):
    return render(request, 'doacoes.html')

def contato(request):
    return render(request, 'contato.html')

def transparencia(request):
    arrecadado_dinheiro = Transparencia.objects.filter(
        tipo='Arrecadação em dinheiro',
        exibir_no_site=True
    ).aggregate(total=Sum('valor'))['total'] or 0

    itens_arrecadados = Transparencia.objects.filter(
        tipo='Arrecadação de item',
        exibir_no_site=True
    ).order_by('-data')

    despesas = Transparencia.objects.filter(
        tipo='Despesa',
        exibir_no_site=True
    ).order_by('-data')

    return render(request, 'transparencia.html', {
        'arrecadado_dinheiro': arrecadado_dinheiro,
        'itens_arrecadados': itens_arrecadados,
        'despesas': despesas
    })

def inscricao(request):
    mensagem_sucesso = False

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        Inscrito.objects.create(
            nome=nome,
            email=email,
            telefone=telefone
        )

        mensagem_sucesso = True

    return render(request, 'inscricao.html', {
        'mensagem_sucesso': mensagem_sucesso
    })


def funcionarios_inicio(request):
    return render(request, 'funcionarios_inicio.html')

def funcionarios_atividades(request):
    if request.method == 'POST':
        Atividade.objects.create(
            nome_atividade = request.POST.get('nome_atividade'),
            descricao = request.POST.get('descricao'),
            data_atividade = request.POST.get('data_atividade') or None,
            local_atividade = request.POST.get('local_atividade'),
            quantidade_vagas = request.POST.get('quantidade_vagas') or None,
            status_atividade = request.POST.get('status_atividade')
        )

        return redirect('funcionarios_atividades')

    atividades = Atividade.objects.all()

    filtro_nome = request.GET.get('filtro_nome', '')
    filtro_data = request.GET.get('filtro_data', '')
    filtro_local = request.GET.get('filtro_local', '')
    filtro_vagas = request.GET.get('filtro_vagas', '')
    filtro_status = request.GET.get('filtro_status', '')

    if filtro_nome:
        atividades = atividades.filter(nome_atividade__icontains=filtro_nome)

    if filtro_data:
        atividades = atividades.filter(data_atividade=filtro_data)

    if filtro_local:
        atividades = atividades.filter(local_atividade__icontains=filtro_local)

    if filtro_vagas:
        atividades = atividades.filter(quantidade_vagas=filtro_vagas)

    if filtro_status:
        atividades = atividades.filter(status_atividade=filtro_status)

    return render(request, 'funcionarios_atividades.html', {
        'atividades': atividades,
        'filtro_nome': filtro_nome,
        'filtro_data': filtro_data,
        'filtro_local': filtro_local,
        'filtro_vagas': filtro_vagas,
        'filtro_status': filtro_status
    })

def editar_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)

    if request.method == 'POST':
        atividade.nome_atividade = request.POST.get('nome_atividade')
        atividade.descricao = request.POST.get('descricao')
        atividade.data_atividade = request.POST.get('data_atividade') or None
        atividade.local_atividade = request.POST.get('local_atividade')
        atividade.quantidade_vagas = request.POST.get('quantidade_vagas') or None
        atividade.status_atividade = request.POST.get('status_atividade')

        atividade.save()

        return redirect('funcionarios_atividades')

    return render(request, 'editar_atividade.html', {
        'atividade': atividade
    })

def excluir_atividade(request, id):
    atividade = get_object_or_404(Atividade, id = id)
    atividade.delete()

    return redirect('funcionarios_atividades')

def funcionarios_inscritos(request):

    inscritos = Inscrito.objects.all()

    filtro_nome = request.GET.get('filtro_nome', '')
    filtro_email = request.GET.get('filtro_email', '')
    filtro_telefone = request.GET.get('filtro_telefone', '')

    if filtro_nome:
        inscritos = inscritos.filter(nome__icontains=filtro_nome)

    if filtro_email:
        inscritos = inscritos.filter(email__icontains=filtro_email)

    if filtro_telefone:
        inscritos = inscritos.filter(telefone__icontains=filtro_telefone)

    return render(request, 'funcionarios_inscritos.html', {
        'inscritos': inscritos,
        'filtro_nome': filtro_nome,
        'filtro_email': filtro_email,
        'filtro_telefone': filtro_telefone
    })

def adicionar_inscrito(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        Inscrito.objects.create(
            nome=nome,
            email=email,
            telefone=telefone
        )

        return redirect('funcionarios_inscritos')

    return render(request, 'adicionar_inscrito.html')

def funcionarios_voluntarios(request):

    if request.method == 'POST':

        inscrito_id = request.POST.get('inscrito')
        atividade_id = request.POST.get('atividade')

        inscrito = get_object_or_404(Inscrito, id=inscrito_id)
        atividade = get_object_or_404(Atividade, id=atividade_id)

        Participacao.objects.create(
            voluntario=inscrito,
            atividade=atividade
        )

        return redirect('funcionarios_voluntarios')

    inscritos = Inscrito.objects.all()
    atividades = Atividade.objects.all()
    participacoes = Participacao.objects.all()

    filtro_inscrito = request.GET.get('filtro_inscrito', '')
    filtro_email = request.GET.get('filtro_email', '')
    filtro_atividade = request.GET.get('filtro_atividade', '')
    filtro_data = request.GET.get('filtro_data', '')

    if filtro_inscrito:
        participacoes = participacoes.filter(voluntario__nome__icontains=filtro_inscrito)

    if filtro_email:
        participacoes = participacoes.filter(voluntario__email__icontains=filtro_email)

    if filtro_atividade:
        participacoes = participacoes.filter(atividade__nome_atividade__icontains=filtro_atividade)

    if filtro_data:
        participacoes = participacoes.filter(atividade__data_atividade=filtro_data)

    return render(request, 'funcionarios_voluntarios.html', {
        'inscritos': inscritos,
        'atividades': atividades,
        'participacoes': participacoes,
        'filtro_inscrito': filtro_inscrito,
        'filtro_email': filtro_email,
        'filtro_atividade': filtro_atividade,
        'filtro_data': filtro_data
    })

def excluir_voluntario(request, id):

    participacao = get_object_or_404(Participacao, id=id)

    participacao.delete()

    return redirect('funcionarios_voluntarios')

def editar_voluntario(request, id):

    participacao = get_object_or_404(Participacao, id=id)

    if request.method == 'POST':

        inscrito_id = request.POST.get('inscrito')
        atividade_id = request.POST.get('atividade')

        participacao.voluntario = get_object_or_404(Inscrito, id=inscrito_id)
        participacao.atividade = get_object_or_404(Atividade, id=atividade_id)

        participacao.save()

        return redirect('funcionarios_voluntarios')

    inscritos = Inscrito.objects.all()
    atividades = Atividade.objects.all()

    return render(request, 'editar_voluntario.html', {
        'participacao': participacao,
        'inscritos': inscritos,
        'atividades': atividades
    })

def editar_inscrito(request, id):

    inscrito = get_object_or_404(Inscrito, id=id)

    if request.method == 'POST':

        inscrito.nome = request.POST.get('nome')
        inscrito.email = request.POST.get('email')
        inscrito.telefone = request.POST.get('telefone')

        inscrito.save()

        return redirect('funcionarios_inscritos')

    return render(request, 'editar_inscrito.html', {
        'inscrito': inscrito
    })


def gerenciar_despesas(request):
    if request.method == 'POST':
        Transparencia.objects.create(
            descricao=request.POST.get('descricao'),
            tipo=request.POST.get('tipo'),
            valor=request.POST.get('valor') or None,
            quantidade=request.POST.get('quantidade') or None,
            data=request.POST.get('data'),
            exibir_no_site=True if request.POST.get('exibir_no_site') == 'on' else False
        )

        return redirect('despesas')

    registros = Transparencia.objects.all().order_by('-data')

    return render(request, 'despesas.html', {
        'despesas': registros
    })

def remover_despesa(request, id_despesa):
    registro = get_object_or_404(Transparencia, id=id_despesa)
    registro.delete()

    return redirect('despesas')

def editar_transparencia(request, id):
    registro = get_object_or_404(Transparencia, id=id)

    if request.method == 'POST':
        registro.descricao = request.POST.get('descricao')
        registro.tipo = request.POST.get('tipo')
        registro.valor = request.POST.get('valor') or None
        registro.quantidade = request.POST.get('quantidade') or None
        registro.data = request.POST.get('data')
        registro.exibir_no_site = True if request.POST.get('exibir_no_site') == 'on' else False

        registro.save()

        return redirect('despesas')

    return render(request, 'editar_transparencia.html', {
        'registro': registro
    })