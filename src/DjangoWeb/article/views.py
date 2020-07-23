from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleColumn
from .form import ArticleColumnForm, ArticleColumnAddForm
import re


@login_required(login_url='/user/login/')
@csrf_exempt
def article_column(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            return HttpResponseRedirect('/article/article_column/add/')
        elif 'upd' in request.POST:
            column_id = request.POST['column_id']
            return HttpResponseRedirect('/article/article_column/upd/' + column_id, column_id)
        elif 'del' in request.POST:
            column_id = request.POST['column_id']
            return HttpResponseRedirect('/article/article_column/del/' + column_id, column_id)
    else:
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm
        return render(request, 'article/column.html', {'columns': columns, 'column_form': column_form})


@login_required(login_url='/user/login/')
@csrf_exempt
def article_column_add(request):
    if request.method == 'POST':
        new_column_name = request.POST['new_column']
        columns = ArticleColumn.objects.filter(
            user=request.user, column=new_column_name)
        if columns:
            column_add_form = ArticleColumnAddForm(request.POST)
            column_add_form.add_error('new_column', 'コラムは既に存在しているので、ご確認ください。')
            return render(request, 'article/column_add.html', {'form': column_add_form, })
        else:
            ArticleColumn.objects.create(
                user=request.user, column=new_column_name)
            return HttpResponseRedirect('/article/article_column/')
    else:
        column_add_form = ArticleColumnAddForm
        return render(request, 'article/column_add.html', {'form': column_add_form})


@login_required(login_url='/user/login/')
@csrf_exempt
def article_column_del(request, column_id):
    if request.method == 'POST':
        columns = ArticleColumn.objects.filter(user=request.user, id=column_id)
        if columns:
            columns.delete()
            return HttpResponseRedirect('/article/article_column/')
        else:
            return HttpResponseRedirect('/article/article_column/')
    else:
        column_del = get_object_or_404(ArticleColumn, id=column_id)
        return render(request, 'article/column_del.html', {'form': column_del})

@login_required(login_url='/user/login/')
@csrf_exempt
def article_column_upd(request, column_id):
    if request.method == 'POST':
        columns = ArticleColumn.objects.filter(user=request.user, id=column_id)
        if columns:
            return HttpResponseRedirect('/article/article_column/')
        else:
            return HttpResponseRedirect('/article/article_column/')
    else:
        column_upd = get_object_or_404(ArticleColumn, id=column_id)
        return render(request, 'article/column_upd.html', {'form': column_upd})