from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.taskList),
    path('tasks/<int:pk>/', views.taskDetail),
    
]