from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = auth.authenticate(
                username=cd['username'], password=cd['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/blog/')
                # return HttpResponse("Welcome you, you have been authenticated sucessfully!")
            else:
                return HttpResponse("Usrname or Password is not right!")
        else:
            return HttpResponse('Invalid login!')
    elif request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'user/login.html', {'form': login_form})


def user_logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return render(request, 'user/logout.html')
