from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article_column/$', views.article_column, name="article_column"),
    url(r'^article_column/add/$', views.article_column_add, name="article_column_add"),
    url(r'^article_column/del/(?P<column_id>\d*)$', views.article_column_del, name="article_column_del"),
    url(r'^article_column/upd/(?P<column_id>\d*)$', views.article_column_upd, name="article_column_upd"),
]