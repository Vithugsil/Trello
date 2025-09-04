
# 🚀 Como rodar o projeto Trello

## 📋 Pré-requisitos
- Python 3.8+ instalado
- Django instalado (`pip install django`)

## ⚡ Passos para executar

### 1. Clone e navegue até o projeto
```bash
cd caminho/para/pasta/Trello
```

### 2. Rode o projeto para que o DB SQLITE seja criado
```bash
python manage.py runserver
```
Após executar e verificar que o arquivo **db.sqlite3** foi criado, cancele a execução do programa com <kbd>CTRL</kbd>+<kbd>C</kbd> e siga para o próximo passo.

### 3. Aplique as migrações do banco de dados
```bash
python manage.py migrate
```

### 4. Configure os dados iniciais (Status, usuários e tarefas de exemplo)
```bash
python manage.py setup_initial_data
```

### 5. Inicie o servidor
```bash
python manage.py runserver
```

### 6. Acesse o projeto
Abra seu navegador e vá para: `http://localhost:8000/`

---

## 👤 Usuários de teste

Ao ter executado o comando `setup_initial_data`, você pode fazer login com:

- **Usuário:** `joao` | **Senha:** `123456`
- **Usuário:** `maria` | **Senha:** `123456`
- **Usuário:** `admin` | **Senha:** `admin123`

---

## 🎯 Funcionalidades

### 📱 **Páginas disponíveis:**
- **`/`** - Página inicial (suas tarefas)
- **`/login/`** - Login
- **`/signup/`** - Cadastro
- **`/dashboard/`** - Dashboard geral com todas as tarefas ⭐
- **`/newtask/`** - Criar nova tarefa
- **`/logout/`** - Sair

### ✨ **Principais recursos:**
- ✅ Sistema de login/logout
- ✅ Criação, edição e exclusão de tarefas
- ✅ Atribuição de tarefas a outros usuários
- ✅ Status das tarefas (Pendente, Em Andamento, Concluída)
- ✅ Filtros por status e usuário
- ✅ Dashboard com estatísticas gerais
- ✅ Interface responsiva

---

## 🔄 Comandos úteis

### Para recriar o banco do zero:
```bash
# Apague o arquivo de banco
rm db.sqlite3
# (No Windows: del db.sqlite3)

# Recrie as migrações
python manage.py migrate
python manage.py setup_initial_data
```

### Para usar uma porta diferente:
```bash
python manage.py runserver 8001
```

### Para criar um superusuário (acesso ao admin):
```bash
python manage.py createsuperuser
```

---

## 🎉 Pronto para usar!


**⭐ Destaque:** Acesse o **Dashboard** em `/dashboard/` para ver todas as tarefas do sistema com estatísticas!
