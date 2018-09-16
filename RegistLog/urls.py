from django.urls import path
from . import views

app_name = '[RegistLog]'

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('validate/', views.validate, name='validate'),
    path('logout/', views.logout, name='logout')
]
