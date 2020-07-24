from django import forms
from .models import ArticleColumn


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)


class ArticleColumnNewForm(forms.Form):
    new_column = forms.CharField(label='新しいコラム', max_length=64)

