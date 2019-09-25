# Librerias Django
from django.contrib import messages
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyLog
from ..models import PyCompany, PyMeta, PyParameter, PyPlugin, PyWParameter


def _count_plugin():
    return PyPlugin.objects.all().count()

def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter

def _parameter():
    parameter = {}
    for parametro in PyParameter.objects.all():
        parameter[parametro.name] = parametro.value
    return parameter



def _web_meta():
    cad = ''
    for meta in PyMeta.objects.all():
        cad += '<meta name="'+meta.title+'" content="'+meta.content+'">' + '\n'
    return cad


class FatherTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin']= _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        return context

    class Meta:
        abstract = True

class FatherListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(
            company_id=self.request.user.active_company_id
        )
        return queryset

    class Meta:
        abstract = True

class FatherDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        return context

    class Meta:
        abstract = True

class FatherUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.um = self.request.user.pk
        self.object.save()
        return super().form_valid(form)

    class Meta:
        abstract = True


class FatherCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.uc = self.request.user.pk
        self.object.company_id = self.request.user.active_company_id
        self.object.save()
        return super().form_valid(form)

    class Meta:
        abstract = True
