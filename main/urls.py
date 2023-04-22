from django.urls import path
from .import views

urlpatterns = [
   path('',views.index),
   path('question/',views.question),
   path('result/',views.result),
   path('login/', views.login),

]
