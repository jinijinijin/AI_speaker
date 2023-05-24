from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index),
    path('question/', views.questions),
    path('login/', views.login),
    path('', views.main),
    path('result/', views.result),

]
