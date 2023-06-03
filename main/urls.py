from django.urls import path
from .import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('question/', views.questions, name='question'),
    path('login/', views.login_register, name='login'),
    path('', views.main),
    path('result/', views.result),
    #path('result/survey/', views.survey_form, name='survey_form'),

]
