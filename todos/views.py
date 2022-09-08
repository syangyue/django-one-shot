from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoList, TodoItem


class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_list/list.html"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todo_list/detail.html"
