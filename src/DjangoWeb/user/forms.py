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

    def clean_password2(self):
        cd = self.cleaned_data
        password = cd.get('password')
        password2 = cd.get('password2')
        if len(password) < 8 or len(password) > 20:
            raise forms.ValidationError("パスワードは8～20桁で、ご確認ください。")
        elif password != password2:
            raise forms.ValidationError("パスワードは不一致ので、ご確認ください。")
        return password2


class UserProfileForm(forms.ModelForm):
    birth = forms.DateField(
        label='生年月日', widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(
        label='携帯電話番号', max_length=11, widget=forms.NumberInput(attrs={'type': 'tel'}))

    class Meta:
        model = UserProfile
        fields = ('birth', 'phone',)
