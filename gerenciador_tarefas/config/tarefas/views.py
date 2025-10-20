from django.shortcuts import render
from .models import Tarefa
from django.http HttpResponse

def listar_tarefas(request):
    tarefas_salvas = tarefa.objects.all()
    contexto = {
             "minhas_tarefas":tarefas_salvas        
    }

    return render (request, 'tarefas/lista.html',contexto)