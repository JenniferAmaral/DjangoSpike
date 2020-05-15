from django.contrib import admin
from .models import Palestra
from .models import Evento

# Register your models here.
admin.site.register(Palestra)
admin.site.register(Evento)
