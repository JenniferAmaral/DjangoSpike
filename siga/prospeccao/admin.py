from django.contrib import admin
from .models import DesafioInovacao
from .models import InovacaoAberta
from .models import ReuniaoGrupoPesquisa
from .models import ReuniaoEmpresa
from .models import AtendimentoEmpreendedor

admin.site.register(DesafioInovacao)
admin.site.register(InovacaoAberta)
admin.site.register(ReuniaoGrupoPesquisa)
admin.site.register(ReuniaoEmpresa)
admin.site.register(AtendimentoEmpreendedor)
# Register your models here.
