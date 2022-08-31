from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import User
from django.contrib import messages
from hashlib import sha256

# Create your views here.
class CadastroUsers(View):
    def get(self, request):
        if 'usuario' in request.session:
            email = User.objects.get(id = request.session['usuario']).email
            return render(request, 'cadastroUser.html', {'email': email})
        else:
            return render(request, 'cadastroUser.html')
    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha = sha256(senha.encode()).hexdigest()

        usuario = User.objects.filter(email=email)
        
        if len(usuario) == 0:
            try:
                User.objects.create(nome=nome, email=email, senha=senha)
                messages.add_message(request, messages.INFO, 'Usuário criado com sucesso')
                return redirect('login')
            except Exception:
                messages.add_message(request, messages.INFO, 'Erro do sistema')
                return redirect('cadastroUsers')
        elif len(usuario) > 0:
            messages.add_message(request, messages.INFO, 'Esse email já está cadastrado!')
            return redirect('cadastroUsers')
        

class Login(View):
    def get(self, request):
        if 'usuario' in request.session:
            email = User.objects.get(id = request.session['usuario']).email
            return render(request, 'login.html', {'email': email})
        else:
            return render(request, 'login.html')
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha = sha256(senha.encode()).hexdigest()

        usuario = User.objects.filter(email=email).filter(senha=senha)
        if len(usuario) == 0:
            messages.add_message(request, messages.INFO, 'Usuário não existente ou senha incorreta!')
            return redirect('login')
        elif len(usuario)>0:
            request.session['usuario'] = usuario[0].id
            return redirect(f'/?id_usuario={request.session["usuario"]}')

def sair(request):
    request.session.flush()
    return redirect('home')