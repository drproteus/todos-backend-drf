from django.http import Http404

from rest_framework import viewsets

from api.models import Todo
from api.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
