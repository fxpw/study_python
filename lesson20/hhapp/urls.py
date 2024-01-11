from django.urls import path
from hhapp import views


app_name = 'hhapp'

urlpatterns = [
    path('', views.start, name='index'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result')
]
