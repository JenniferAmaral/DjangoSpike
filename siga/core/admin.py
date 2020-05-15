from django.contrib import admin
from .models import NucleoIncubador, Servidor
# Register your models here.


class NucleoIncubadorAdmin(admin.ModelAdmin):  # para personalização da exibição
    empty_value_display = 'Nenhum'
    list_display = ('name',)  # exibir nome
    search_fields = (['name', ])  # pesquisa por nome


admin.site.register(NucleoIncubador, NucleoIncubadorAdmin)
admin.site.register(Servidor)
