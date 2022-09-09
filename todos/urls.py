from django.urls import path
from todos.views import TodoListListView, TodoListDetailView, TodolistCreateView, TodoListUpdateView, TodoListDeleteView


urlpatterns = [
    path('', TodoListListView.as_view(), name="todo_list_list"),
    path('<int:pk>/', TodoListDetailView.as_view(), name="todo_list_detail"),
    path('create/', TodolistCreateView.as_view(), name="todo_list_create"),
    path('<int:pk>/edit/', TodoListUpdateView.as_view(), name="todo_list_update"),
    path('<int:pk>/delete/', TodoListDeleteView.as_view(), name="todo_list_delete"),
]
