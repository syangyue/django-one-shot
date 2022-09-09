
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoList, TodoItem
from sqlite3 import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_list/list.html"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todo_list/detail.html"


class TodolistCreateView(CreateView):
    model = TodoList
    template_name = "todo_list/new.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todo_list/edit.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todo_list/delete.html"
    success_url = reverse_lazy("todo_list_list")


class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todo_item/new.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.id])
