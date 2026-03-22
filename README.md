# Projeto Python RH

Criação de sistema RH completo Django + PostgreSQL.

## Requisitos
- Modelos:
  - Funcionario (Nome, CPF, Cargo, Salário, Data de Admissão, Departamento)
  - Departamento (Nome, Sigla)
  - Ferias (Funcionario, Data Início, Data Fim)
- Interface responsiva Bootstrap 5 com Navbar e Sidebar
- CRUD completo de funcionários
- Busca e filtro por departamento
- Dashboard com métricas

## Como rodar

DJANGO_USE_SQLITE=1 python manage.py migrate && DJANGO_USE_SQLITE=1 python manage.py runserver 0.0.0.0:8000
