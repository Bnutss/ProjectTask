from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:pk>/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/complete/', views.complete_task, name='complete_task'),
]
