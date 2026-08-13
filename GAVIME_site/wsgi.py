from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('doacoes/', views.doacoes, name='doacoes'),
    path('contato/', views.contato, name='contato'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('inscricao/', views.inscricao, name='inscricao'),

    path('funcionarios/', views.funcionarios_inicio, name='funcionarios_inicio'),
    path('funcionarios/atividades/', views.funcionarios_atividades, name='funcionarios_atividades'),

    path(
        'funcionarios/atividades/editar/<int:id>/',
        views.editar_atividade,
        name='editar_atividade'
    ),

    path(
        'funcionarios/atividades/excluir/<int:id>/',
        views.excluir_atividade,
        name='excluir_atividade'
    ),

    path(
        'funcionarios/inscritos/',
        views.funcionarios_inscritos,
        name='funcionarios_inscritos'
    ),

    path(
        'funcionarios/inscritos/adicionar/',
        views.adicionar_inscrito,
        name='adicionar_inscrito'
    ),

    path(
        'funcionarios/voluntarios/',
        views.funcionarios_voluntarios,
        name='funcionarios_voluntarios'
    ),

    path(
        'funcionarios/voluntarios/excluir/<int:id>/',
        views.excluir_voluntario,
        name='excluir_voluntario'
    ),

    path(
        'funcionarios/voluntarios/editar/<int:id>/',
        views.editar_voluntario,
        name='editar_voluntario'
    ),

    path(
        'funcionarios/inscritos/editar/<int:id>/',
        views.editar_inscrito,
        name='editar_inscrito'
    ),

    path(
        'funcionarios/inscritos/excluir/<int:id>/',
        views.excluir_inscrito,
        name='excluir_inscrito'
    ),

    path('funcionarios/despesas/',
         views.gerenciar_despesas,
         name='despesas'
    ),

    path('funcionarios/despesas/remover/<int:id_despesa>/',
         views.remover_despesa,
         name='remover_despesa'
    ),

    path(
        'funcionarios/despesas/editar/<int:id>/',
        views.editar_transparencia,
        name='editar_transparencia'
    ),

    path(
        'funcionarios/despesas/excluir/<int:id_despesa>/',
        views.remover_despesa,
        name='remover_despesa'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'funcionarios/newsletter/',
        views.funcionarios_newsletter,
        name='funcionarios_newsletter'
    ),

    path(
        'funcionarios/newsletter/editar/<int:id>/',
        views.editar_newsletter,
        name='editar_newsletter'
    ),

    path(
        'funcionarios/newsletter/excluir/<int:id>/',
        views.excluir_newsletter,
        name='excluir_newsletter'
    ),

    path(
        'funcionarios/inscritos/desativar/<int:id>/',
        views.desativar_inscrito,
        name='desativar_inscrito'
    ),

    path(
        'funcionarios/inscritos/ativar/<int:id>/',
        views.ativar_inscrito,
        name='ativar_inscrito'
    ),

    path(
        'funcionarios/banners/',
        views.funcionarios_banner,
        name='funcionarios_banner'
    ),

    path(
        'funcionarios/banners/cadastrar/',
        views.funcionarios_banner_cadastrar,
        name='funcionarios_banner_cadastrar'
    ),

    path(
        'funcionarios/banners/<int:banner_id>/editar/',
        views.funcionarios_banner_editar,
        name='funcionarios_banner_editar'
    ),

    path(
        'funcionarios/banners/<int:banner_id>/excluir/',
        views.funcionarios_banner_excluir,
        name='funcionarios_banner_excluir'
    ),

    path(
        'funcionarios/banners/<int:banner_id>/status/',
        views.funcionarios_banner_alterar_status,
        name='funcionarios_banner_alterar_status'
    ),

    path(
        'campanhas/',
        views.campanhas,
        name='campanhas'
    ),

    path(
        'funcionarios/campanhas/',
        views.funcionarios_campanhas,
        name='funcionarios_campanhas'
    ),

    path(
        'funcionarios/campanhas/cadastrar/',
        views.funcionarios_campanha_criar,
        name='funcionarios_campanha_criar'
    ),

    path(
        'funcionarios/campanhas/<int:campanha_id>/editar/',
        views.funcionarios_campanha_editar,
        name='funcionarios_campanha_editar'
    ),

    path(
        'funcionarios/campanhas/<int:campanha_id>/status/',
        views.funcionarios_campanha_alterar_status,
        name='funcionarios_campanha_alterar_status'
    ),

    path(
        'funcionarios/campanhas/<int:campanha_id>/excluir/',
        views.funcionarios_campanha_excluir,
        name='funcionarios_campanha_excluir'
    ),
]
