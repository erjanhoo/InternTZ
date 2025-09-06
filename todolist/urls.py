from django.urls import path
from .views import *

urlpatterns = [
    path('task_list/', AllTasks.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskInfo.as_view(), name='task'),
    path('update_task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]