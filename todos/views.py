from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, UpdateView, DeleteView


from .models import TodoList


class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_list/list.html"
