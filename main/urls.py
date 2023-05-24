from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('question/', views.questions, name='question'),
    path('login/', views.sign, name='sign'),
    path('', views.main),
    path('result/', views.result),

]
