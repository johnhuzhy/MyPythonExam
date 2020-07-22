from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleColumn
from .form import ArticleColumnForm, ArticleColumnAddForm


@login_required(login_url='/user/login/')
@csrf_exempt
def article_column(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            return HttpResponseRedirect('/article/article_column/add/')
        elif 'upd' in request.POST:
            return render(request, 'article/column_upd.html')
        elif 'del' in request.POST:
            return render(request, 'article/column_del.html')
    else:
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm
        return render(request, 'article/column.html', {'columns': columns, 'column_form': column_form})


@login_required(login_url='/user/login/')
@csrf_exempt
def article_column_add(request):
    if request.method == 'POST':
        new_column_name = request.POST['new_column']
        columns = ArticleColumn.objects.filter(user=request.user, column=new_column_name)
        if columns:
            column_add_form = ArticleColumnAddForm(request.POST)
            column_add_form.add_error('new_column','コラムは既に存在しているので、ご確認ください。')
            return render(request, 'article/column_add.html', {'form': column_add_form, })
        else:
            ArticleColumn.objects.create(user=request.user, column=new_column_name)
            return HttpResponseRedirect('/article/article_column/')
    else:
        column_add_form = ArticleColumnAddForm
        return render(request, 'article/column_add.html', {'form': column_add_form})
