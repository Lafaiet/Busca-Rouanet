from django.contrib import admin
from .models import Projeto, Proponente, Incentivador, Doacao


class ProjetoAdmin(admin.ModelAdmin):
	list_display = ('PRONAC', )

class ProponenteAdmin(admin.ModelAdmin):
	list_display = ('cgccpf', )

class IncentivadorAdmin(admin.ModelAdmin):
	list_display = ('cgccpf', )

class DoacaoAdmin(admin.ModelAdmin):
	list_display = ('PRONAC', 'nome_projeto', 'nome_doador', 'valor')


admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Proponente, ProponenteAdmin)
admin.site.register(Incentivador, IncentivadorAdmin)
admin.site.register(Doacao, DoacaoAdmin)

