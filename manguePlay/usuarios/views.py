from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Usando auth_login para evitar conflito
                messages.success(request, f'Bem-vindo, {username}!')
                
                # Verifica se o usuário é admin
                user_profile = UserProfile.objects.get(user=user)
                if user_profile.is_admin:
                    return render(request, 'admin_dashboard.html')  # Redireciona para a página de admin
                else:
                    return render(request, 'user_dashboard.html')  # Redireciona para a página de usuário
                
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('home')

def cadastro(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados e tente novamente.')
    
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'cadastro.html', {'user_form': user_form, 'profile_form': profile_form})

def home(request):
    return render(request, 'home.html')