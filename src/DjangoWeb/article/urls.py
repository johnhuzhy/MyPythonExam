from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article_column/$', views.article_column, name="article_column"),
    url(r'^article_column/add/$', views.article_column_add, name="article_column_add"),
]