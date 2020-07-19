from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^register/$', views.user_register, name="user_register"),
    url(r'^register_result/$', views.user_register_result,
        name="user_register_result"),
    url(r'^password_change/$',
        views.PasswordChange.as_view(), name='password_change'),
    url(r'^password_change_done/$',
        views.PasswordChangeDone.as_view(), name="password_change_done"),
]
