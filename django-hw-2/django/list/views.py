from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Task


class ListView(ListView):
    model = Task
    template_name = 'list/index.html'


class EditListView(UpdateView):
    model = Task
    template_name = 'list/create_task.html'
    fields = ('title', 'description', 'was_completed')

    def get_success_url(self):
        return reverse('list:task_list')


class CreateListView(CreateView):
    model = Task
    template_name = 'list/create_task.html'
    fields = ('title', 'description', )

    def get_success_url(self):
        return reverse('list:task_list')

    def form_valid(self, form):
        return super(CreateListView, self).form_valid(form)

