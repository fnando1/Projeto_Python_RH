from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import Funcionario, Departamento
from .forms import FuncionarioForm, DepartamentoForm


def dashboard(request):
    total_funcionarios = Funcionario.objects.count()
    total_folha = Funcionario.objects.aggregate(total=Sum("salario"))["total"] or 0
    departamentos = Departamento.objects.order_by("nome")
    context = {
        "total_funcionarios": total_funcionarios,
        "total_folha": total_folha,
        "departamentos": departamentos,
    }
    return render(request, "core/dashboard.html", context)


def funcionario_list(request):
    search = request.GET.get("search", "")
    dept_id = request.GET.get("departamento", "")
    funcionarios = Funcionario.objects.select_related("departamento").all()
    if search:
        funcionarios = funcionarios.filter(nome__icontains=search)
    if dept_id:
        funcionarios = funcionarios.filter(departamento__id=dept_id)
    departamentos = Departamento.objects.all()
    return render(request, "core/funcionario_list.html", {
        "funcionarios": funcionarios,
        "departamentos": departamentos,
        "search": search,
        "departamento_atual": dept_id,
    })


def funcionario_detail(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(request, "core/funcionario_detail.html", {"funcionario": funcionario})


def funcionario_create(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:funcionario_list")
    else:
        form = FuncionarioForm()
    return render(request, "core/funcionario_form.html", {"form": form, "titulo": "Novo Funcionário"})


def funcionario_update(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect("core:funcionario_detail", pk=funcionario.pk)
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, "core/funcionario_form.html", {"form": form, "titulo": "Editar Funcionário"})


def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        funcionario.delete()
        return redirect("core:funcionario_list")
    return render(request, "core/funcionario_confirm_delete.html", {"funcionario": funcionario})


def departamento_create(request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:dashboard")  # ou para uma lista de departamentos
    else:
        form = DepartamentoForm()
    return render(request, "core/departamento_form.html", {"form": form, "titulo": "Novo Departamento"})
