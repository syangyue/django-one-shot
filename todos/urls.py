from django.urls import path
from todos.views import TodoListListView, TodoListDetailView, TodolistCreateView


urlpatterns = [
    path('', TodoListListView.as_view(), name="todo_list_list"),
    path('<int:pk>/', TodoListDetailView.as_view(), name="todo_list_detail"),
    path('create/', TodolistCreateView.as_view(), name="todo_list_create"),
]
