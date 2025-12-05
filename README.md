# JobPilot AI Backend

Backend do JobPilot AI, uma plataforma para gerenciamento de usuários, autenticação e vagas de emprego. Construído com **FastAPI**, **MongoDB** e autenticação via **JWT**.

---# 🚀 JobPilot AI - Backend

Backend do **JobPilot AI**, plataforma para gerenciamento de usuários, autenticação e vagas de emprego, desenvolvido com **FastAPI**, **MongoDB** e **JWT**.

---

## 🛠 Tecnologias

- Python 3.11+
- FastAPI
- Motor (MongoDB Async Driver)
- Pydantic Settings
- JWT (PyJWT)
- Uvicorn
- MongoDB

---

## ⚙️ Configuração

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd backend

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
DATABASE_URL=mongodb://jobpilot_user:SenhaForte123@localhost:27017/jobpilot_db
JWT_SECRET=MinhaPalavraSecretaMuitoForte!2025
JWT_ALGORITHM=HS256

🏃‍♂️ Executando
uvicorn app.main:app --reload
Acesse: http://127.0.0.1:8000

📦 Endpoints Principais
Autenticação

POST /auth/login → Login do usuário

POST /auth/refresh → Atualizar token JWT

Usuários

GET /users → Listar usuários

POST /users → Criar usuário

GET /users/{id} → Obter usuário

PUT /users/{id} → Atualizar usuário

DELETE /users/{id} → Deletar usuário

Vagas

GET /jobs → Listar vagas

POST /jobs → Criar vaga

GET /jobs/{id} → Obter vaga

PUT /jobs/{id} → Atualizar vaga

DELETE /jobs/{id} → Deletar vaga

🔗 Exemplos de Requests
cURL - Login
curl -X POST http://127.0.0.1:8000/auth/login \
-H "Content-Type: application/json" \
-d '{"email": "usuario@teste.com", "password": "123456"}'


📜 Licença

MIT License




