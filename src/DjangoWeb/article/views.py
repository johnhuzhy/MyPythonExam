from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleColumn
from .form import ArticleColumnForm


@login_required(login_url='/user/login/')
@csrf_exempt
def article_column(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm
        return render(request, 'article/column.html', {'columns': columns, 'column_form':column_form})
    elif request.method == 'POST':
        return render(request, 'article/column_add.html')


@login_required(login_url='/user/login/')
@csrf_exempt
def article_column_add(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm
        return render(request, 'article/column_add.html', {'columns': columns, 'column_form':column_form})
    elif request.method == 'POST':
        return render(request, 'article/column.html', {'columns': columns, 'column_form':column_form})
