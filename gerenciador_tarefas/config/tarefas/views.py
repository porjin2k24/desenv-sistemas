from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Tarefa

from django.http  import HttpResponse 


def listar_tarefas(request):
    tarefas_salvas = Tarefa.objects.all()
    contexto = {
        "minhas_tarefas" : tarefas_salvas        
    }

    return render(request, 'tarefas\lista.html', contexto)

def detalhe_tarefa (request, tarefa_id):
    tarefa =  get_object_or_404(Tarefa, pk=tarefa_id)

    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})


def adicionar_tarefa(request):
    
    if request.method =='POST':

        titulo = request.POST.get('titulo')

        descricao = request.POST.get('descricao')
        
        Tarefa.objects.create(titulo=titulo,descricao=descricao)

        return redirect('lista_tarefas')
    return render(request,'tarefas/form_tarefa.html')

def alterar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.concluida = request.POST.get('concluida') == 'on'
        tarefa.save()  # salva as alterações no objeto existente
        return redirect('lista_tarefas')
    
    return render(request, 'tarefas/form_tarefa.html', {'tarefa': tarefa})


def excluir_tarefa(request, tarefa_id):
    tarefa= get_object_or_404(Tarefa, pk= tarefa_id)
    if request.method=='POST':
        tarefa.delete()#delete o objeto no banco
        return redirect('lista_tarefas')
    return render(request, 'tarefas/confirmar_exclusao.html',{'tarefa':tarefa})