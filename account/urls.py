from django.conf.urls import url,re_path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns = [
#    re_path(r'^login/$', views.user_login, name="user_login"),
    re_path(r'^login/$', auth_views.login, name="user_login"),
    re_path(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"}),
    re_path(r'^logout/$', auth_views.logout, name='user_logout'),

]
