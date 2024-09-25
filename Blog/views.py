from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse 
from.models import Funcionario

# Create your views here.
def index(request):
    mFuncionarios=Funcionario.objects.all().values()
    
    template = loader.get_template('index.html')
    context={
        'mFuncionarios':mFuncionarios
    }
    return HttpResponse(template.render(context,request))


def create(request):
    template = loader.get_template('createPageFunc.html')
    return HttpResponse(template.render({},request))


def createDado(request):
    dado1 = request.POST['name']
    dado2 = request.POST['title']
    novoFuncionario = Funcionario(name=dado1,title=dado2)
    novoFuncionario.save()
    return HttpResponseRedirect(reverse('index'))


def deletar(request,id):
    deletarFuncionario= Funcionario.objects.get(id=id)
    deletarFuncionario.delete()
    return HttpResponseRedirect(reverse('index'))



def update(request,id):
    updateFuncionario= Funcionario.objects.get(id=id)
    template = loader.get_template('updatePageFunc.html')
    context={
        'Funcionarios':updateFuncionario
    }
    return HttpResponse(template.render(context,request))



def updateDado(request,id):
    name = request.POST['name']
    title = request.POST['title']
    updateFuncionario= Funcionario.objects.get(id=id)
    updateFuncionario.name=name
    updateFuncionario.title=title
    updateFuncionario.save()
    return HttpResponseRedirect(reverse('index'))

    
    
    
