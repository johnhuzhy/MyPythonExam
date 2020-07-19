from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='パスワード(確認)', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'password2', 'email')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 or len(password) > 20:
            raise forms.ValidationError("パスワードは8桁～20桁で、ご確認ください。")
        return password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("パスワードは不一致ので、ご確認ください。")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    birth = forms.DateField(
        label='生年月日', widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.DateField(
        label='携帯電話番号', widget=forms.DateInput(attrs={'type': 'tel'}))

    class Meta:
        model = UserProfile
        fields = ('birth', 'phone',)
