from django.urls import path
from . import views
urlpatterns = [
        path('',views.listar_tarefas,name='lista_tarefas'),
]