from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TodoItem, TodoList
from django.contrib.auth import logout, login
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


@login_required
def IndexList(request):
    # all TodoItems that belong to any TodoList owned by the current user.
    all_todos = TodoItem.objects.filter(
        todolist__user=request.user).order_by("todolist__name", "-created")
    return render(request, 'index.html', {'all_todos': all_todos})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index-list")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


class TodoCreate(LoginRequiredMixin, CreateView):
    model = TodoItem
    fields = ["title", "todolist", "deadline"]
    success_url = reverse_lazy("index-list")

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields["todolist"].queryset = TodoList.objects.filter(user=self.request.user)
    #     return form


class TodoToggle(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ["done"]
    success_url = reverse_lazy("todo-list")


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy("todo-list")


# LIST VIEWS:
class ListDelete():
    pass


class ListAdd():

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
