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

## Como rodar (Passo a Passo)

### A) Preparar o banco PostgreSQL
No terminal do PostgreSQL (psql):

```sql
CREATE DATABASE rh_system;
```

### B) Configurar ambiente

```bash
cd /workspaces/Projeto_Python_RH
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### C) Configurar settings.py

No `rh_system/settings.py`, configure:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rh_system',
        'USER': 'seu_usuario_postgres',
        'PASSWORD': 'sua_senha_postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### D) Migrar e rodar

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### E) Acessar
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/`

## Observações
- Se precisar de fallback SQLite para dev, exporte `DJANGO_USE_SQLITE=1`.
