from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from appDeustomachInicioSesion.forms import SignupForm, LoginForm


class SignupView(View):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    def get(self, request):
        form = SignupForm()
        return render(request, 'appDeustomachInicioSesion/signup.html', {'form': form})


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('tickets_menu')
            else:
                return render(request, 'appDeustomachInicioSesion/login.html',
                              {'form': form, 'error_message': 'Invalid username or password'})
        else:
            return render(request, 'appDeustomachInicioSesion/login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'appDeustomachInicioSesion/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
