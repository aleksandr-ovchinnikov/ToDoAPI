from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addTask, name='add-task'),
    path('complete/<int:pk>/', views.completeTask, name='complete-task'),
    path('all/', views.getAllTasks, name='get-all-tasks'),
    path('get/<int:pk>/', views.getTask, name='get-task'),
    path('delete/<int:pk>/', views.deleteTask, name='delete-task')
]
