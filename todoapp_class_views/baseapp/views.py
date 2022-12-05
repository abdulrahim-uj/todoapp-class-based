from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TodoTaskForm


# List views model.objects.all()
class TasksListView(ListView):
    model = Task
    template_name = "baseapp/index.html"
    context_object_name = "tasks"
    

# create view insert new record into db model.save()
class TaskCreateView(CreateView):
    model = Task
    template_name = "baseapp/create.html"
    form_class = TodoTaskForm
    success_url = reverse_lazy('baseapp:home')


# Detail view model.objects.get()
class TaskDetailView(DetailView):
    model = Task
    template_name = "baseapp/detail.html"
    context_object_name = "task"


# update view update existing data
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "baseapp/update.html"
    context_object_name = "task"
    # fields = ('name', 'priority', 'status', 'created')
    form_class = TodoTaskForm

    # ONCE SUCCESSFULLY SAVED REDIRECT TO detail_view URL
    def get_success_url(self):
        return reverse_lazy('baseapp:detail_view', kwargs={'pk': self.object.id})


# delete view delete existing record
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "baseapp/delete.html"
    success_url = reverse_lazy('baseapp:home')
