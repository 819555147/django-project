from django.urls import path, re_path
from . import views

app_name = '[spider_site]'

urlpatterns = [
    path('', views.index, name='index'),
    re_path('spiderRun/', views.spider_run, name='spiderRun'),
    path('aindex/', views.aindex),
    path('baidu/', views.get_baidu),
    re_path('aindex/article/(?P<article_id>[0-9]+)/', views.atricle_page, name='ArticlePage'),
    re_path('aindex/edit/(?P<article_id>[0-9]+)/', views.edit_page, name='edit'),
    path('aindex/edit/action/', views.edit_action, name='edit_action'),
    path('try/', views.just_try, name='try'),
    re_path('jump/(?P<item_id>[0-9]+)/', views.jump, name='jump'),
]