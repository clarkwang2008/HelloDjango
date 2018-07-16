from django.conf.urls import url
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.blog_title, name='blog_title'),
    re_path(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
]