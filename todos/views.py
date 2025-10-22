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

    total = TodoItem.objects.filter(
        todolist__user=request.user).count()
    done = TodoItem.objects.filter(
        todolist__user=request.user, done=True).count()
    pending = total - done
    percent = round((done / total) * 100, 1) if total else 0
    return render(request, 'index.html', {'all_todos': all_todos, 'total': total,
                                          'done': done,
                                          'pending': pending,
                                          'percent': percent})


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

    def get_form(self, form_class=None):  # edit the behavior of form
        form = super().get_form(form_class)
        # only show lists owned by this user
        form.fields["todolist"].queryset = TodoList.objects.filter(
            user=self.request.user)
        return form


class TodoToggle(LoginRequiredMixin, UpdateView):
    model = TodoItem
    fields = ["done"]
    success_url = reverse_lazy("index-list")


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = TodoItem
    success_url = reverse_lazy("index-list")


class TodoEdit(LoginRequiredMixin, UpdateView):
    model = TodoItem
    fields = ['title', 'todolist', 'done', 'deadline']
    success_url = reverse_lazy("index-list")
    template_name = 'todos/edit_todo.html'

    # Only allow editing items that belong to the current user (Cuz via URL it's possible)
    def get_queryset(self):
        return TodoItem.objects.filter(todolist__user=self.request.user)

    # Limit ‘todolist’ dropdown to the current user’s lists while editing
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["todolist"].queryset = TodoList.objects.filter(
            user=self.request.user)
        return form


# LIST VIEWS:
class ListDelete(LoginRequiredMixin, DeleteView):
    model = TodoList
    success_url = reverse_lazy("index-list")


class ListAdd(LoginRequiredMixin, CreateView):
    model = TodoList
    fields = ["name"]
    success_url = reverse_lazy("index-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListEdit(LoginRequiredMixin, UpdateView):
    model = TodoList
    fields = ['name']
    success_url = reverse_lazy("index-list")
    template_name = 'todos/edit_list.html'

    # Only allow editing lists that belong to the current user (Cuz via URL it's possible)
    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user)
