from django import forms
from .models import Funcionario, Departamento


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ["nome", "cpf", "cargo", "salario", "data_admissao", "departamento"]
        widgets = {
            "data_admissao": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "salario": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ["nome", "sigla"]
