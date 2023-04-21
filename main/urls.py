from django.urls import path
from .import views

urlpatterns = [
   path('',views.index),
   path('question/',views.question),
   path('result/',views.question),
   path('login/', views.login),

]
