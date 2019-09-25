# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather

COLOR_CHOICE = (
    ("#ffc", "yellow"),
    ('#cfc', 'green'),
    ('#ccf', 'magenta')
)

class PyNote(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    note = models.TextField(_("Note"))
    color = models.CharField(_("Color"), choices=COLOR_CHOICE, max_length=64, default='yellow')

    def get_absolute_url(self):
        return reverse('base:note-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("")
