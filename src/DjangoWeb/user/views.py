from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Welcome you, you have been authenticated sucessfully!")
            else:
                return HttpResponse("Usrname or Password is not right!")
        else:
            return HttpResponse('Invalid login!')
    elif request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'user/login.html', {'form': login_form})
