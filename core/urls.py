from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("employee/<int:pk>/", views.employee_detail, name="employee_detail"),
]
