from django.views.generic import ListView ,CreateView
from django.urls import reverse_lazy
from . import models
from . import forms


class ProjectListView(ListView):
    models = models.Projects
    template_name = 'project/list.html'

    def get_queryset(self):
        #"""دالة تعيد المشاريع""
        return models.Projects.objects.order_by('id')


class ProjectCreateView(CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')