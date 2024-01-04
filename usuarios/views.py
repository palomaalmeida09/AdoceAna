from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario,Produto
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages

from django.contrib.auth.models import User
def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('username')
        email = request.POST.get('email')
        telefone = request.POST.get('tel')
        senha = request.POST.get('password')
        user = Usuario.objects.filter(acesso__username=email).first() 
        acesso = User.objects.filter(email = email).first()
        #return HttpResponse(username)#
        if user is None and acesso is None:
            usuario = Usuario(nome=nome, telefone=telefone)
            acesso = User.objects.create_user(username=email, email=email, password=senha)
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
            print('n conseguiu autenticar',usu, email, senha, teste)
            return redirect("usuarios:login")
        
    return render(request, 'login.html')

#@login_required(login_url="usuarios:login")
def index(request):
    return render(request, 'index.html')

@login_required(login_url="usuarios:login")
def catalogo(request):
    lista = Produto.objects.all()
    return render(request, 'catalogo.html', {'lista':lista})

#@login_required(login_url="usuarios:login")
def cad_produto(request):

    return render(request, 'cad_produto.html')

def comprar(request, id):

    return render(request, 'final.compra.html', {'produto_id': id})

def final_compra(request, produto_id):
    return render(request, 'usuarios/final.compra.html')