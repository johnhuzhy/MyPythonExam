from django import forms
from .models import ArticleColumn

class ArticleColumn(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)