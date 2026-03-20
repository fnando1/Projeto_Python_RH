# Projeto Python RH

Sistema Django simples para RH com sistema de funcionários, cargos e departamentos.

## Como rodar

```bash
cd /workspaces/Projeto_Python_RH
source .venv/bin/activate
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Acesse:
- `http://127.0.0.1:8000/` (lista de funcionários)
- `http://127.0.0.1:8000/admin/` (admin Django)

Usuário criado automaticamente para testes:
- usuário: `admin`
- senha: `adminpass`

## Configurar PostgreSQL

Para usar PostgreSQL, exporte:

```bash
export DJANGO_USE_SQLITE=0
export POSTGRES_DB=rh_db
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

Depois rode `python manage.py migrate` e `python manage.py runserver`.
