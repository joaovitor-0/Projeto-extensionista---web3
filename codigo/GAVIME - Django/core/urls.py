from django.contrib import admin
from django.urls import path, include
from . import views
from banco_de_dados import bancoVoluntarios
from banco_de_dados import despesas

urlpatterns = [
    path('', views.index, name='index'),
    path('doacoes/', views.doacoes, name='doacoes'),
    path('contato/', views.contato, name='contato'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    #Inscrição e Consulta de Voluntários
    path('inscricao/', bancoVoluntarios.inscricao_voluntario, name='inscricao'),
    path('consulta-painel/', bancoVoluntarios.consultar_inscritos, name='consulta'),
    #Transparência / Banco de despesas
    path('painel/despesas/', despesas.gerenciar_despesas, name='despesas'),
    path('painel/despesas/remover/<int:id_despesa>/', despesas.remover_despesa, name='remover_despesa'),
]