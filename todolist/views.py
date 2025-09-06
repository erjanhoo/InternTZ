from django.shortcuts import render
from django.views import generic
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import *
from .serializers import TaskSerializer


class AllTasks(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTask(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskInfo(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTask(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTask(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer