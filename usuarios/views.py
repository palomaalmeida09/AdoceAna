from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.contrib.auth import logout,authenticate,login


from django.contrib.auth.models import User
def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('username')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')
        user = Usuario.objects.filter(login__username=email).first() 
        #return HttpResponse(username)#
        if user is None:
            user = Usuario(nome=nome, email = email, telefone=telefone)
            login = User.objects.create_user(username=email)
            login.set_password(senha)
            login.is_active = True
            login.is_staff = True
            login.save()
            login
            user.login = login
            user.save()
        return redirect("usuarios:login")
    else:
        return render(request, 'cadastro.html')
            
                 

def entrar(request):
    if request.POST:
        email = request.POST.get("email")
        senha = request.POST.get("password")
        usu = authenticate(username=email, password=senha )
    
        if usu:
            print('conseguiu autenticar')
            login(request,usu)
            return redirect("usuarios:index.")
            
        else:
            print('n conseguiu autenticar',usu, email, senha)
            return redirect("usuarios:login")
        
    return render(request, 'login.html')

@login_required(login_url="usuarios:login")
def index(request):
    return render(request, 'index.html')