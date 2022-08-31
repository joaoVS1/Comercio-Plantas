from multiprocessing import context
from pickle import TRUE
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
import plantas
from users.models import User
from .models import Planta
# Create your views here.

class CadastroPlantas(View):
    def get(self, request):
        return render (request, 'cadastroPlantas.html')
    def post(self, request):
        nome = request.POST.get('nome')
        nomecien = request.POST.get('nomecien')
        origem = request.POST.get('origem')
        imageurl = request.POST.get('imageurl')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        try:
            preco = preco.replace(',','.')
            preco = float(preco)
            Planta.objects.create(nome=nome, nome_cientifico=nomecien, origem=origem, preco=preco, imageurl=imageurl, descricao=descricao)
            return redirect('listaPlantas')
        except Exception:
            messages.add_message(request, messages.INFO, 'Escreva apenas números no campo de preço!!!s')
            return redirect('cadastroPlantas')

def editarPlantas(request, pk):
    planta = Planta.objects.get(pk=pk)
    if (request.method =='GET') :
        context = {
            'planta': planta,
        }
        return render (request, 'editar.html', context)
    elif (request.method == "POST"):
        nome = request.POST.get('nome')
        nomecien = request.POST.get('nomecien')
        origem = request.POST.get('origem')
        imageurl = request.POST.get('imageurl')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        preco = preco.replace(',','.')
        try:
            preco = float(preco)
            planta.nome = nome
            planta.nome_cientifico = nomecien
            planta.origem = origem
            planta.imageurl = imageurl
            planta.descricao = descricao
            planta.preco = preco
            return redirect('listaPlantas')
        except Exception:
            print('bad')
            messages.add_message(request, messages.INFO, "Escreva apenas números no campo de preço!!!")
            return redirect('editarPlantas',pk)

def deletarPlanta(request, pk):
    planta = Planta.objects.get(pk=pk)
    planta.delete()
    return redirect('listaPlantas')



class ListaPlantas(View):
    def get(self, request):
        plantas = Planta.objects.all()
        context = {
            'plantas': plantas,
        }
        if 'usuario' in request.session:
            adm = User.objects.get(pk=request.session['usuario'])
            context['adm'] = adm
            print(adm)
        
        return render(request, 'listaPlantas.html', context)
    def post(self, request):
        pass