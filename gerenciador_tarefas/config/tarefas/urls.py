from django.urls import path
from . import views 
urlpatterns = [

    #DETALHES DA TAREFA
    #<int:tarefa_id>- captura um numero da URL 
    path('', views.listar_tarefas, name='lista_tarefas'),
    path('<int:tarefa_id>/', views.detalhe_tarefa, name='detalhe_tarefa'),

    path ('adicionar/', views.adicionar_tarefa, name = 'adicionar_tarefa'),

    path('<int:tarefa_id>/alterar/', views.alterar_tarefa ,name= 'alterar_tarefa'),

    path('<int:tarefa_id>/excluir/', views.excluir_tarefa,name='excluir_tarefa'),
]