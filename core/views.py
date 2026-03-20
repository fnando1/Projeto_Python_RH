from django.shortcuts import render, get_object_or_404
from .models import Employee


def home(request):
    employees = Employee.objects.select_related("position", "position__department").all()[:20]
    return render(request, "core/home.html", {"employees": employees})


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "core/employee_detail.html", {"employee": employee})
