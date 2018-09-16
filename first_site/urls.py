from django.urls import path
from . import views

app_name = '[first_site]'


urlpatterns = [
    path('', views.index, name='blog'),
    path('algorithm/', views.algorithm, name='algorithm'),
    path('language/', views.language, name='language'),
    path('program/', views.program, name='program'),
    path('project/', views.project, name='project'),
    path('editor/', views.editor, name='editor'),
    path('editor/process/', views.process, name='process'),
    path('editor/delete/', views.delete, name='delete'),
]

