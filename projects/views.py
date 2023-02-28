from django.views.generic import ListView ,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy ,reverse
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


class ProjectUpdateView(UpdateView):
    model = models.Projects
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
#يعيد صفحة المشروع نفسها
#object  يععبر عن المشروع الحالي هو  prpject
#يعدل في نفس الصفحة

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class ProjectDeleteView(DeleteView):
    model = models.Projects
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')


#لن نحتاج الي فورم خاص سوف نضيفها في نفس فورم المشاريع
class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])