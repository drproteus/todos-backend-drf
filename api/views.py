from django.http import Http404

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Todo
from api.serializers import TodoSerializer


class TodoListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        serializer = TodoSerializer(Todo.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.POST)
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
        todo = TodoSerializer(instance=self.todo).update(self.todo, request.POST)
        return Response(TodoSerializer(instance=todo).data)

    def delete(self, request):
        self.todo.delete()
        return Response(TodoSerializer(instance=self.todo).data)
