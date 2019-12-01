from django.urls import path, include

from rest_framework import routers

from api.views import TodoListView, TodoView

urlpatterns = [
    path(r"todos/", TodoListView.as_view(), name="todos"),
    path(r"todos/<uuid:pk>/", TodoView.as_view(), name="todo-detail"),
]
