from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tasks, name='tasks'),
    path('<int:id>/', views.Task, name='task'),
    path('result/<int:id>/', views.Result, name='result'),
]