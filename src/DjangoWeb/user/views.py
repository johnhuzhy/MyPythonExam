from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import LoginForm, RegistrationForm, UserProfileForm


def user_login(request):
    """ログイン処理"""
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
    """ログアウト処理"""
    if request.method == 'GET':
        auth.logout(request)
        return render(request, 'user/logout.html')


def user_register(request):
    """サインアップ処理"""
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_user.save()
            new_profile.save()
            return HttpResponseRedirect('/user/register_result/')
        else:
            return HttpResponse("Sorry, you can not register!")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'user/register.html', {'form': user_form, 'profile': userprofile_form})


def user_register_result(request):
    """サインアップ結果"""
    if request.method == 'GET':
        return render(request, 'user/register_result.html')


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更ビュー"""
    success_url = reverse_lazy('password_change_done')
    template_name = 'user/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'password_change'
        return context


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    """パスワード変更完了"""
    template_name = 'user/password_change_done.html'
