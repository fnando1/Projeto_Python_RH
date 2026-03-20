from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class Funcionario(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=80)
    salario = models.DecimalField(max_digits=12, decimal_places=2)
    data_admissao = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Ferias(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="ferias")
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"Férias de {self.funcionario.nome}: {self.data_inicio} a {self.data_fim}"
