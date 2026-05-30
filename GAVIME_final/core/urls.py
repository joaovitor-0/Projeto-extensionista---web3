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
]
