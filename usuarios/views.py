from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages

from django.contrib.auth.models import User
def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('username')
        email = request.POST.get('email')
        telefone = request.POST.get('tel')
        senha = request.POST.get('senha')
        user = Usuario.objects.filter(acesso__username=email).first() 
        acesso = User.objects.filter(email = email).first()
        #return HttpResponse(username)#
        if user is None and acesso is None:
            usuario = Usuario(nome=nome, telefone=telefone)
            acesso = User.objects.create_user(username=email, email=email)
            acesso.set_password(senha)
            acesso.is_active = True
            acesso.is_staff = True
            acesso.save()
            acesso
            usuario.acesso = acesso
            usuario.save()
            return redirect("usuarios:login")
        elif user is not None:
            messages.error(request, 'Erro: já existe usuário com esse email cadastrado')
        elif acesso is not None:
            messages.error(request, 'Erro: já existe acesso com esse email cadastrado')
        return render(request, 'cadastro.html')
    else:
        
        return render(request, 'cadastro.html')
            
                 

def entrar(request):
    if request.POST:
        email = request.POST.get("email_or_username")
        senha = request.POST.get("password")
        usu = authenticate(username=email, password=senha)
    
        if usu:
            print('conseguiu autenticar')
            login(request,usu)
            return redirect("usuarios:catalogo")
            
        else:
            print('n conseguiu autenticar',usu, email, senha)
            return redirect("usuarios:login")
        
    return render(request, 'login.html')

#@login_required(login_url="usuarios:login")
def index(request):
    return render(request, 'index.html')

@login_required(login_url="usuarios:login")
def catalogo(request):
    return render(request, 'catalogo.html')

@login_required(login_url="usuarios:cad_produto")
def cad_produto(request):
    return render(request, 'cad_produto.html')

@login_required(login_url="usuarios:carrinho")
def carrinho(request):
    return render(request, 'carrinho')