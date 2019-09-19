# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Librerias en carpetas locales
from ..models.base_config import BaseConfig
from ..forms import InitForm
from ..models.company import PyCompany
from ..models.usercustom import PyUser
from ..models.currency import PyCurrency


def IndexEasy(request):
    if BaseConfig.objects.all().exists():
        template = 'base/index.html'
    else:
        template = 'base/install.html'
    context = {}
    if request.method == 'POST':
        context['form'] = InitForm(request.POST)
        if context['form'].is_valid():
            name = context['form'].cleaned_data.get('name')
            country = context['form'].cleaned_data.get('country')
            currency = PyCurrency.objects.get(country=country)
            user_name = context['form'].cleaned_data.get('user')
            password = context['form'].cleaned_data.get('password')
            BaseConfig.crear(PyCompany.crear(name, country, currency))
            # PyUser.crear(user, password, 1, 1, 1)
            user = PyUser.objects.create_user(user_name, None, password)
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.first_name = 'Admin'
            user.last_name = 'User'
            user.save()

            return HttpResponseRedirect(reverse_lazy('home:home_easy'))
    else:
        context['form'] = InitForm()

    return render(request, template, context)
