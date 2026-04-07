# 🎯 Sistema RH - Django

Um sistema completo de Recursos Humanos desenvolvido com Django, PostgreSQL/SQLite e Bootstrap 5. Gerencie funcionários, departamentos e período de férias com uma interface moderna e responsiva.

## ✨ Funcionalidades

### 👥 Gestão de Funcionários
- ✅ CRUD completo de funcionários
- ✅ Cadastro com CPF (validado), cargo, salário e data de admissão
- ✅ Filtro por departamento e busca por nome
- ✅ Detalhes com informações de departamento
- ✅ Exclusão com confirmação

### 🏢 Departamentos
- ✅ Cadastro de departamentos com siglas
- ✅ Associação obrigatória com funcionários
- ✅ Proteção contra exclusão (se tiver funcionários)

### 🏖️ Gestão de Férias
- ✅ Registro de períodos de férias
- ✅ Validação de datas (máx. 30 dias)
- ✅ Rastreamento de status (Planejadas/Em Andamento/Finalizada)
- ✅ Visualização por funcionário
- ✅ Dashboard com alertas de funcionários em férias

### 📊 Dashboard RH
- ✅ Total de funcionários
- ✅ Gasto com folha de pagamento
- ✅ Número de departamentos
- ✅ Funcionários em férias hoje
- ✅ Previsão de férias próximas (30 dias)
- ✅ Lista rápida de funcionários

### 🎨 Interface
- ✅ Bootstrap 5 responsivo
- ✅ Navbar com navegação
- ✅ Sidebar com menu
- ✅ Tabelas interativas
- ✅ Alertas e notificações
- ✅ Design mobile-friendly

### 🔐 Admin Django
- ✅ Painel administrativo (http://localhost:8000/admin)
- ✅ Visualização de métricas formatadas
- ✅ Filtros por departamento e período

## 🗄️ Modelo de Dados

```
DEPARTAMENTO (1) ──── (N) FUNCIONARIO ──── (N) FERIAS
    ├─ id (PK)              ├─ id (PK)          ├─ id (PK)
    ├─ nome (UK)            ├─ nome             ├─ funcionario_id (FK)
    └─ sigla (UK)           ├─ cpf (UK)         ├─ data_inicio
                            ├─ cargo            └─ data_fim
                            ├─ salario
                            ├─ data_admissao
                            └─ departamento_id (FK)
```

### Validações
- **CPF:** Formato XXX.XXX.XXX-XX, validação de dígitos
- **Salário:** Apenas valores positivos
- **Data Admissão:** Não pode ser data futura
- **Férias:** Período máximo 30 dias, fim > início

## 📋 Requisitos

- Python 3.8+
- Django 6.0+
- PostgreSQL 12+ (opcional) ou SQLite (padrão)
- pip/virtualenv

## 🚀 Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Projeto_Python_RH.git
cd Projeto_Python_RH
```

### 2️⃣ Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar banco de dados

#### Opção A: SQLite (Rápido para desenvolvimento)

```bash
python manage.py migrate
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

#### Opção B: PostgreSQL (Produção)

Criar banco de dados:
```sql
CREATE DATABASE rh_system;
CREATE USER rh_user WITH PASSWORD 'sua_senha';
ALTER ROLE rh_user SET client_encoding TO 'utf8';
ALTER ROLE rh_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE rh_user SET default_transaction_deferrable TO on;
ALTER ROLE rh_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE rh_system TO rh_user;
```

Atualizar `rh_system/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rh_system',
        'USER': 'rh_user',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Migrar:
```bash
python manage.py migrate
python manage.py runserver
```

### 5️⃣ Criar superusuário (para admin)

```bash
python manage.py createsuperuser
```

## 📍 URLs Disponíveis

### Frontend
| URL | Descrição |
|-----|-----------|
| `/` | Dashboard RH |
| `/funcionarios/` | Lista de funcionários |
| `/funcionarios/novo/` | Criar funcionário |
| `/funcionarios/<id>/` | Detalhes do funcionário |
| `/funcionarios/<id>/editar/` | Editar funcionário |
| `/funcionarios/<id>/excluir/` | Excluir funcionário |
| `/ferias/` | Lista de férias |
| `/ferias/novo/` | Registrar férias |
| `/ferias/<id>/` | Detalhes das férias |
| `/ferias/<id>/editar/` | Editar férias |
| `/ferias/<id>/excluir/` | Excluir férias |
| `/departamentos/novo/` | Criar departamento |
| `/er-diagram/` | Diagrama ER |

### Admin
| URL | Descrição |
|-----|-----------|
| `/admin/` | Painel administrativo Django |

## 💻 Como Usar

### Criar Funcionário
1. Navegue para "Funcionários" no menu
2. Clique em "+ Novo Funcionário"
3. Preencha os dados (CPF format: XXX.XXX.XXX-XX)
4. Selecione um departamento
5. Clique em "Salvar"

### Registrar Férias
1. Vá para "Férias" no menu
2. Clique em "+ Registrar Férias"
3. Selecione o funcionário
4. Informar datas (máx 30 dias)
5. Submeta o formulário

### Filtrar Funcionários
1. Na página de funcionários
2. Use a barra de busca por nome
3. Selecione um departamento no dropdown
4. Clique em "Filtrar"

### Visualizar Dashboard
1. Acesse a página inicial (/)
2. Veja métricas gerais
3. Confira funcionários em férias
4. Visualize previsão de férias próximas

## 🔧 Estrutura do Projeto

```
Projeto_Python_RH/
├── core/                          # Aplicação principal Django
│   ├── migrations/                # Migrações do banco
│   ├── templates/core/            # Templates HTML
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── funcionario_list.html
│   │   ├── funcionario_form.html
│   │   ├── funcionario_detail.html
│   │   ├── ferias_list.html
│   │   ├── ferias_form.html
│   │   ├── ferias_detail.html
│   │   └── departamento_form.html
│   ├── admin.py                   # Configuração do admin
│   ├── forms.py                   # Formulários Django
│   ├── models.py                  # Modelos de dados
│   ├── views.py                   # Views/Controladores
│   ├── urls.py                    # Rotas
│   └── tests.py                   # Testes
├── rh_system/                     # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py                      # CLI Django
├── requirements.txt               # Dependências Python
├── db.sqlite3                     # Banco SQLite (dev)
├── README.md                      # Este arquivo
└── .gitignore                     # Git ignore

```

## 📦 Dependências

```
Django==6.0.3
psycopg2-binary==2.9.11
django-crispy-forms==2.6
crispy-bootstrap5==2026.3
mysqlclient==2.2.8
```

Ver `requirements.txt` para lista completa.

## 🧪 Testes

```bash
python manage.py test core
```

## 📝 Migrações

Criar nova migração após alterar modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🐛 Resolução de Problemas

### Erro: "django.db.utils.OperationalError: no such table"
```bash
python manage.py migrate
```

### Erro: "psycopg2.OperationalError: FATAL: database does not exist"
- Crie o banco: `CREATE DATABASE rh_system;`
- Configure as credenciais em `settings.py`

### Superusuário não funciona
```bash
python manage.py createsuperuser
```

## 📄 Licença

MIT License - Veja LICENSE para detalhes

## 👨‍💻 Autor

Sistema RH desenvolvido como projeto educacional em Django.

## 🤝 Contribuições

Contributions are welcome! Por favor abra uma issue ou pull request.

---

**Status:** ✅ Produção  
**Última atualização:** Abril 2026  
**Versão:** 1.0
