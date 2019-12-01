from django.http import Http404
import json

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from todos.models import Todo

from api.serializers import TodoSerializer


class TodoListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        todos = Todo.objects.all().order_by("-order", "updated_at")
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(request.body)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            todo = serializer.save()
            return Response(TodoSerializer(instance=todo).data)
        return Response(serializer.errors)

    def delete(self, request):
        todos = Todo.objects.all()
        todos.delete()
        return Response(TodoSerializer(todos, many=True).data)


class TodoView(APIView):
    def dispatch(self, request, pk=None):
        try:
            self.todo = Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            raise Http404
        return super().dispatch(request)

    def get(self, request):
        return Response(TodoSerializer(instance=self.todo).data)

    def post(self, request):
        data = json.loads(request.body)
        todo = TodoSerializer(instance=self.todo).update(self.todo, data)
        return Response(TodoSerializer(instance=todo).data)

    def delete(self, request):
        self.todo.delete()
        return Response(TodoSerializer(instance=self.todo).data)
