from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.taskList, name="task.list"),
    path('<int:pk>/', views.taskDetail, name="task.detail"),
    path('create/', views.taskCreate, name="task.new")
    
]