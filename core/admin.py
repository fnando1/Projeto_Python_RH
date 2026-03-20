from django.contrib import admin
from .models import Departamento, Funcionario, Ferias

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla")
    search_fields = ("nome", "sigla")


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "cargo", "departamento", "salario", "data_admissao")
    list_filter = ("departamento",)
    search_fields = ("nome", "cpf", "cargo")


@admin.register(Ferias)
class FeriasAdmin(admin.ModelAdmin):
    list_display = ("funcionario", "data_inicio", "data_fim")
    list_filter = ("data_inicio",)
