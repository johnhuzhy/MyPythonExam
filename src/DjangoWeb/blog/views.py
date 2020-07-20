from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogArticles


@login_required(login_url='/user/login/')
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/title.html", {'blogs': blogs})


@login_required(login_url='/user/login/')
def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {'article': article, 'publish': pub})
