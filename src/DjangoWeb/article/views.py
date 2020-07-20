from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn


@login_required(login_url='/user/login/')
def article_column(request):
    columns = ArticleColumn.objects.filter(user=request.user)
    return render(request, 'article/column.html', {'columns': columns})
