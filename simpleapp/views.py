

from rest_framework import viewsets
from . import models
from . import serializers


class SimpleModelViewset(viewsets.ModelViewSet):
	queryset = models.SimpleModel.objects.all()
	serializer_class = serializers.SimpleModelSerializer
	

