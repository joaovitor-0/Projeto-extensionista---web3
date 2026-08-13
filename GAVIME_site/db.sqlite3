from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CampanhaForm
from .models import Campanha

from .forms import BannerForm
from .models import (
    Atividade,
    Banner,
    Inscrito,
    Newsletter,
    Participacao,
    Transparencia,
)


def index(request):
    mensagem_newsletter = False

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cidade = request.POST.get('cidade')

        Newsletter.objects.update_or_create(
            email=email,
            defaults={
                'nome': nome,
                'telefone': telefone,
                'cidade': cidade
            }
        )

        corpo_email = f'''
Novo cadastro na newsletter do GAVIME

Nome: {nome}
E-mail: {email}
Telefone / WhatsApp: {telefone}
Cidade: {cidade}
'''

        send_mail(
            'Novo cadastro na newsletter do GAVIME',
            corpo_email,
            settings.EMAIL_HOST_USER,
            ['gavimegrupodeapoiovivermelhor@gmail.com'],
            fail_silently=False
        )

        mensagem_newsletter = True

    banners = Banner.objects.filter(
        ativo=True
    ).order_by(
        'ordem',
        'id'
    )

    return render(request, 'index.html', {
        'mensagem_newsletter': mensagem_newsletter,
        'banners': banners
    })


def doacoes(request):
    return render(request, 'doacoes.html')


def contato(request):
    mensagem_sucesso = False

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        corpo_email = f'''
Nome: {nome} {sobrenome}
E-mail: {email}
Assunto: {assunto}

Mensagem:
{mensagem}
'''

        send_mail(
            assunto,
            corpo_email,
            settings.EMAIL_HOST_USER,
            ['gavimegrupodeapoiovivermelhor@gmail.com'],
            fail_silently=False
        )

        mensagem_sucesso = True

    return render(request, 'contato.html', {
        'mensagem_sucesso': mensagem_sucesso
    })


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


@login_required
def funcionarios_inicio(request):
    return render(request, 'funcionarios_inicio.html')


@login_required
def funcionarios_atividades(request):
    if request.method == 'POST':
        Atividade.objects.create(
            nome_atividade=request.POST.get('nome_atividade'),
            descricao=request.POST.get('descricao'),
            data_atividade=request.POST.get('data_atividade') or None,
            local_atividade=request.POST.get('local_atividade'),
            quantidade_vagas=request.POST.get('quantidade_vagas') or None,
            status_atividade=request.POST.get('status_atividade')
        )

        return redirect('funcionarios_atividades')

    atividades = Atividade.objects.all()

    filtro_nome = request.GET.get('filtro_nome', '')
    filtro_data = request.GET.get('filtro_data', '')
    filtro_local = request.GET.get('filtro_local', '')
    filtro_vagas = request.GET.get('filtro_vagas', '')
    filtro_status = request.GET.get('filtro_status', '')

    if filtro_nome:
        atividades = atividades.filter(
            nome_atividade__icontains=filtro_nome
        )

    if filtro_data:
        atividades = atividades.filter(
            data_atividade=filtro_data
        )

    if filtro_local:
        atividades = atividades.filter(
            local_atividade__icontains=filtro_local
        )

    if filtro_vagas:
        atividades = atividades.filter(
            quantidade_vagas=filtro_vagas
        )

    if filtro_status:
        atividades = atividades.filter(
            status_atividade=filtro_status
        )

    return render(request, 'funcionarios_atividades.html', {
        'atividades': atividades,
        'filtro_nome': filtro_nome,
        'filtro_data': filtro_data,
        'filtro_local': filtro_local,
        'filtro_vagas': filtro_vagas,
        'filtro_status': filtro_status
    })


@login_required
def editar_atividade(request, id):
    atividade = get_object_or_404(
        Atividade,
        id=id
    )

    if request.method == 'POST':
        atividade.nome_atividade = request.POST.get('nome_atividade')
        atividade.descricao = request.POST.get('descricao')
        atividade.data_atividade = (
            request.POST.get('data_atividade') or None
        )
        atividade.local_atividade = request.POST.get('local_atividade')
        atividade.quantidade_vagas = (
            request.POST.get('quantidade_vagas') or None
        )
        atividade.status_atividade = request.POST.get('status_atividade')

        atividade.save()

        return redirect('funcionarios_atividades')

    return render(request, 'editar_atividade.html', {
        'atividade': atividade
    })


@login_required
def excluir_atividade(request, id):
    atividade = get_object_or_404(
        Atividade,
        id=id
    )

    atividade.delete()

    return redirect('funcionarios_atividades')


@login_required
def funcionarios_inscritos(request):
    inscritos = Inscrito.objects.all()

    filtro_nome = request.GET.get('filtro_nome', '')
    filtro_email = request.GET.get('filtro_email', '')
    filtro_telefone = request.GET.get('filtro_telefone', '')

    if filtro_nome:
        inscritos = inscritos.filter(
            nome__icontains=filtro_nome
        )

    if filtro_email:
        inscritos = inscritos.filter(
            email__icontains=filtro_email
        )

    if filtro_telefone:
        inscritos = inscritos.filter(
            telefone__icontains=filtro_telefone
        )

    return render(request, 'funcionarios_inscritos.html', {
        'inscritos': inscritos,
        'filtro_nome': filtro_nome,
        'filtro_email': filtro_email,
        'filtro_telefone': filtro_telefone
    })


@login_required
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


@login_required
def funcionarios_voluntarios(request):
    if request.method == 'POST':
        inscrito_id = request.POST.get('inscrito')
        atividade_id = request.POST.get('atividade')

        inscrito = get_object_or_404(
            Inscrito,
            id=inscrito_id
        )

        atividade = get_object_or_404(
            Atividade,
            id=atividade_id
        )

        Participacao.objects.create(
            voluntario=inscrito,
            atividade=atividade
        )

        return redirect('funcionarios_voluntarios')

    inscritos = Inscrito.objects.filter(
        ativo=True
    )

    atividades = Atividade.objects.all()
    participacoes = Participacao.objects.all()

    filtro_inscrito = request.GET.get('filtro_inscrito', '')
    filtro_email = request.GET.get('filtro_email', '')
    filtro_atividade = request.GET.get('filtro_atividade', '')
    filtro_data = request.GET.get('filtro_data', '')

    if filtro_inscrito:
        participacoes = participacoes.filter(
            voluntario__nome__icontains=filtro_inscrito
        )

    if filtro_email:
        participacoes = participacoes.filter(
            voluntario__email__icontains=filtro_email
        )

    if filtro_atividade:
        participacoes = participacoes.filter(
            atividade__nome_atividade__icontains=filtro_atividade
        )

    if filtro_data:
        participacoes = participacoes.filter(
            atividade__data_atividade=filtro_data
        )

    return render(request, 'funcionarios_voluntarios.html', {
        'inscritos': inscritos,
        'atividades': atividades,
        'participacoes': participacoes,
        'filtro_inscrito': filtro_inscrito,
        'filtro_email': filtro_email,
        'filtro_atividade': filtro_atividade,
        'filtro_data': filtro_data
    })


@login_required
def excluir_voluntario(request, id):
    participacao = Participacao.objects.filter(
        id=id
    ).first()

    if participacao:
        participacao.delete()

    return redirect('funcionarios_voluntarios')


@login_required
def editar_voluntario(request, id):
    participacao = get_object_or_404(
        Participacao,
        id=id
    )

    if request.method == 'POST':
        inscrito_id = request.POST.get('inscrito')
        atividade_id = request.POST.get('atividade')

        participacao.voluntario = get_object_or_404(
            Inscrito,
            id=inscrito_id
        )

        participacao.atividade = get_object_or_404(
            Atividade,
            id=atividade_id
        )

        participacao.save()

        return redirect('funcionarios_voluntarios')

    inscritos = Inscrito.objects.all()
    atividades = Atividade.objects.all()

    return render(request, 'editar_voluntario.html', {
        'participacao': participacao,
        'inscritos': inscritos,
        'atividades': atividades
    })


@login_required
def editar_inscrito(request, id):
    inscrito = get_object_or_404(
        Inscrito,
        id=id
    )

    if request.method == 'POST':
        inscrito.nome = request.POST.get('nome')
        inscrito.email = request.POST.get('email')
        inscrito.telefone = request.POST.get('telefone')

        inscrito.save()

        return redirect('funcionarios_inscritos')

    return render(request, 'editar_inscrito.html', {
        'inscrito': inscrito
    })


@login_required
def gerenciar_despesas(request):
    if request.method == 'POST':
        Transparencia.objects.create(
            descricao=request.POST.get('descricao'),
            tipo=request.POST.get('tipo'),
            valor=request.POST.get('valor') or None,
            quantidade=request.POST.get('quantidade') or None,
            data=request.POST.get('data'),
            exibir_no_site=(
                request.POST.get('exibir_no_site') == 'on'
            )
        )

        return redirect('despesas')

    registros = Transparencia.objects.all().order_by(
        '-data'
    )

    return render(request, 'despesas.html', {
        'despesas': registros
    })


@login_required
def remover_despesa(request, id_despesa):
    registro = get_object_or_404(
        Transparencia,
        id=id_despesa
    )

    registro.delete()

    return redirect('despesas')


@login_required
def editar_transparencia(request, id):
    registro = get_object_or_404(
        Transparencia,
        id=id
    )

    if request.method == 'POST':
        registro.descricao = request.POST.get('descricao')
        registro.tipo = request.POST.get('tipo')
        registro.valor = request.POST.get('valor') or None
        registro.quantidade = request.POST.get('quantidade') or None
        registro.data = request.POST.get('data')
        registro.exibir_no_site = (
            request.POST.get('exibir_no_site') == 'on'
        )

        registro.save()

        return redirect('despesas')

    return render(request, 'editar_transparencia.html', {
        'registro': registro
    })


@login_required
def excluir_inscrito(request, id):
    inscrito = get_object_or_404(
        Inscrito,
        id=id
    )

    inscrito.delete()

    return redirect('funcionarios_inscritos')


@login_required
def funcionarios_newsletter(request):
    inscritos_newsletter = Newsletter.objects.all()

    filtro_nome = request.GET.get('filtro_nome', '')
    filtro_email = request.GET.get('filtro_email', '')
    filtro_telefone = request.GET.get('filtro_telefone', '')
    filtro_cidade = request.GET.get('filtro_cidade', '')

    if filtro_nome:
        inscritos_newsletter = inscritos_newsletter.filter(
            nome__icontains=filtro_nome
        )

    if filtro_email:
        inscritos_newsletter = inscritos_newsletter.filter(
            email__icontains=filtro_email
        )

    if filtro_telefone:
        inscritos_newsletter = inscritos_newsletter.filter(
            telefone__icontains=filtro_telefone
        )

    if filtro_cidade:
        inscritos_newsletter = inscritos_newsletter.filter(
            cidade__icontains=filtro_cidade
        )

    inscritos_newsletter = inscritos_newsletter.order_by(
        '-data_cadastro'
    )

    return render(request, 'funcionarios_newsletter.html', {
        'inscritos_newsletter': inscritos_newsletter,
        'filtro_nome': filtro_nome,
        'filtro_email': filtro_email,
        'filtro_telefone': filtro_telefone,
        'filtro_cidade': filtro_cidade
    })


@login_required
def editar_newsletter(request, id):
    inscrito = get_object_or_404(
        Newsletter,
        id=id
    )

    if request.method == 'POST':
        inscrito.nome = request.POST.get('nome')
        inscrito.email = request.POST.get('email')
        inscrito.telefone = request.POST.get('telefone')
        inscrito.cidade = request.POST.get('cidade')

        inscrito.save()

        return redirect('funcionarios_newsletter')

    return render(request, 'editar_newsletter.html', {
        'inscrito': inscrito
    })


@login_required
def excluir_newsletter(request, id):
    inscrito = get_object_or_404(
        Newsletter,
        id=id
    )

    inscrito.delete()

    return redirect('funcionarios_newsletter')


@login_required
def desativar_inscrito(request, id):
    inscrito = get_object_or_404(
        Inscrito,
        id=id
    )

    inscrito.ativo = False
    inscrito.save()

    return redirect('funcionarios_inscritos')


@login_required
def ativar_inscrito(request, id):
    inscrito = get_object_or_404(
        Inscrito,
        id=id
    )

    inscrito.ativo = True
    inscrito.save()

    return redirect('funcionarios_inscritos')


@login_required
def funcionarios_banner(request):
    filtro_titulo = request.GET.get(
        'titulo',
        ''
    ).strip()

    filtro_status = request.GET.get(
        'status',
        ''
    ).strip()

    banners = Banner.objects.all().order_by(
        'ordem',
        'id'
    )

    if filtro_titulo:
        banners = banners.filter(
            titulo__icontains=filtro_titulo
        )

    if filtro_status == 'ativo':
        banners = banners.filter(
            ativo=True
        )

    elif filtro_status == 'inativo':
        banners = banners.filter(
            ativo=False
        )

    contexto = {
        'banners': banners,
        'filtro_titulo': filtro_titulo,
        'filtro_status': filtro_status
    }

    return render(
        request,
        'funcionarios_banner.html',
        contexto
    )


@login_required
def funcionarios_banner_cadastrar(request):
    if request.method == 'POST':
        formulario = BannerForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Banner cadastrado com sucesso.'
            )

            return redirect(
                'funcionarios_banner'
            )

    else:
        formulario = BannerForm()

    contexto = {
        'form': formulario,
        'titulo_pagina': 'Cadastrar banner',
        'texto_botao': 'Cadastrar banner'
    }

    return render(
        request,
        'funcionarios_banner_formulario.html',
        contexto
    )


@login_required
def funcionarios_banner_editar(request, banner_id):
    banner = get_object_or_404(
        Banner,
        id=banner_id
    )

    if request.method == 'POST':
        formulario = BannerForm(
            request.POST,
            request.FILES,
            instance=banner
        )

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Banner atualizado com sucesso.'
            )

            return redirect(
                'funcionarios_banner'
            )

    else:
        formulario = BannerForm(
            instance=banner
        )

    contexto = {
        'form': formulario,
        'banner': banner,
        'titulo_pagina': 'Editar banner',
        'texto_botao': 'Salvar alterações'
    }

    return render(
        request,
        'funcionarios_banner_formulario.html',
        contexto
    )


@login_required
def funcionarios_banner_excluir(request, banner_id):
    if request.method != 'POST':
        return redirect(
            'funcionarios_banner'
        )

    banner = get_object_or_404(
        Banner,
        id=banner_id
    )

    imagem = banner.imagem

    banner.delete()

    if imagem:
        try:
            imagem.delete(save=False)
        except Exception:
            pass

    messages.success(
        request,
        'Banner excluído com sucesso.'
    )

    return redirect(
        'funcionarios_banner'
    )


@login_required
def funcionarios_banner_alterar_status(request, banner_id):
    if request.method != 'POST':
        return redirect(
            'funcionarios_banner'
        )

    banner = get_object_or_404(
        Banner,
        id=banner_id
    )

    banner.ativo = not banner.ativo

    banner.save(
        update_fields=['ativo']
    )

    messages.success(
        request,
        'Status do banner alterado com sucesso.'
    )

    return redirect(
        'funcionarios_banner'
    )

def campanhas(request):
    campanhas_ativas = Campanha.objects.filter(
        ativa=True
    ).order_by(
        'ordem',
        '-criada_em'
    )

    return render(
        request,
        'campanhas.html',
        {
            'campanhas': campanhas_ativas
        }
    )


@login_required
def funcionarios_campanhas(request):
    busca = request.GET.get('busca', '').strip()
    status = request.GET.get('status', '').strip()

    campanhas = Campanha.objects.all().order_by(
        'ordem',
        '-criada_em'
    )

    if busca:
        campanhas = campanhas.filter(
            titulo__icontains=busca
        )

    if status == 'ativas':
        campanhas = campanhas.filter(
            ativa=True,
            concluida=False
        )

    elif status == 'inativas':
        campanhas = campanhas.filter(
            ativa=False
        )

    elif status == 'concluidas':
        campanhas = campanhas.filter(
            concluida=True
        )

    return render(
        request,
        'funcionarios_campanhas.html',
        {
            'campanhas': campanhas,
            'busca': busca,
            'status': status,
        }
    )


@login_required
def funcionarios_campanha_criar(request):
    if request.method == 'POST':
        form = CampanhaForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            campanha = form.save()

            messages.success(
                request,
                f'A campanha “{campanha.titulo}” foi cadastrada com sucesso.'
            )

            return redirect('funcionarios_campanhas')

    else:
        form = CampanhaForm()

    return render(
        request,
        'funcionarios_campanha_form.html',
        {
            'form': form,
            'titulo_pagina': 'Cadastrar campanha',
            'texto_botao': 'Cadastrar campanha',
        }
    )


@login_required
def funcionarios_campanha_editar(request, campanha_id):
    campanha = get_object_or_404(
        Campanha,
        id=campanha_id
    )

    if request.method == 'POST':
        form = CampanhaForm(
            request.POST,
            request.FILES,
            instance=campanha
        )

        if form.is_valid():
            campanha = form.save()

            messages.success(
                request,
                f'A campanha “{campanha.titulo}” foi atualizada com sucesso.'
            )

            return redirect('funcionarios_campanhas')

    else:
        form = CampanhaForm(
            instance=campanha
        )

    return render(
        request,
        'funcionarios_campanha_form.html',
        {
            'form': form,
            'campanha': campanha,
            'titulo_pagina': 'Editar campanha',
            'texto_botao': 'Salvar alterações',
        }
    )


@login_required
def funcionarios_campanha_alterar_status(request, campanha_id):
    if request.method != 'POST':
        return redirect('funcionarios_campanhas')

    campanha = get_object_or_404(
        Campanha,
        id=campanha_id
    )

    campanha.ativa = not campanha.ativa
    campanha.save(
        update_fields=[
            'ativa',
            'atualizada_em'
        ]
    )

    if campanha.ativa:
        mensagem = 'A campanha foi ativada.'
    else:
        mensagem = 'A campanha foi desativada.'

    messages.success(
        request,
        mensagem
    )

    return redirect('funcionarios_campanhas')


@login_required
def funcionarios_campanha_excluir(request, campanha_id):
    if request.method != 'POST':
        return redirect('funcionarios_campanhas')

    campanha = get_object_or_404(
        Campanha,
        id=campanha_id
    )

    titulo = campanha.titulo
    campanha.delete()

    messages.success(
        request,
        f'A campanha “{titulo}” foi excluída.'
    )

    return redirect('funcionarios_campanhas')
