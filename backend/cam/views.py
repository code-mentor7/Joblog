from rest_framework import generics

from . import models
from . import serializers

class ListJOBLOG(generics.ListCreateAPIView):
    queryset = models.JOB_LOG.objects.all()
    serializer_class = serializers.JOBLOGSerializer
