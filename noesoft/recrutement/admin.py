from django.contrib import admin

from django.contrib import admin

from .models import Poste, Candidat, Poste_Candidat

admin.site.register(Poste)
admin.site.register(Candidat)
admin.site.register(Poste_Candidat)
