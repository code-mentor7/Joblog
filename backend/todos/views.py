from rest_framework import generics

from . import models
from . import serializers


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class ListCamdev(generics.ListCreateAPIView):
    queryset = models.Camdev.objects.all()
    serializer_class = serializers.CamdevSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
