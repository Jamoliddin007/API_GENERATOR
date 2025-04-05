README - API Generator (FastAPI)
📘 Project Overview
API Generator is a dynamic backend automation platform built using FastAPI. It allows users to create, manage, and expose project-specific CRUD APIs on separate subdomains without writing custom backend code for each project. This system is designed to serve multiple clients, automate schema-based API generation, control method-level access, and allow third-party backend integration.
🚀 Features
• Multi-project API generation with isolated databases and subdomains.
• Dynamic creation of CRUD endpoints with custom fields and data types.
• Admin and Client API separation for access control.
• Method-level permissions per endpoint (e.g., create only for admin, read for client).
• Bearer token-based authentication for secure API access.
• Automatic subdomain routing with project-level configurations.
• Integration support for external backend services (fallback, forward, hybrid use cases).
• Swagger UI generation for every project’s endpoint documentation.
🧱 Tech Stack
• FastAPI - backend framework
• SQLAlchemy - ORM
• PostgreSQL - relational database
• Alembic - database migrations
• Uvicorn - ASGI server
• Docker - containerization
• NGINX - reverse proxy & subdomain management
• JWT - authentication via Bearer token
📂 Folder Structure

api-generator-backend/
├── app/
│   ├── core/            # Configurations, DB connectors, routers
│   ├── models/          # SQLAlchemy database models
│   ├── schemas/         # Pydantic request/response schemas
│   ├── routers/         # Admin and Client API endpoints
│   ├── services/        # Business logic and dynamic code generation
│   └── __init__.py
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── .env                 # Environment configurations
├── alembic/             # DB migrations
├── Dockerfile           # Docker container
└── README.md            # Project documentation

⚙️ Getting Started
1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/api-generator-backend.git
   cd api-generator-backend
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  (or venv\Scripts\activate on Windows)
3. Install dependencies:
   pip install -r requirements.txt
4. Configure environment variables in `.env`:

PROJECT_NAME=API Generator
DATABASE_URL=postgresql://user:password@localhost:5432/api_generator
SECRET_KEY=your_super_secret_key

5. Run migrations and start the server:
   alembic upgrade head
   uvicorn main:app --reload
🔐 Authentication & Permissions
Each generated API project includes two tokens — one for /admin access and one for /client access. Endpoints are protected via Bearer token authentication. Permissions are managed per method.
🌐 Example Usage

Example project: Gazeta
Subdomain: https://gazeta.api-generator.uz
CRUDs: news, categories

Admin API:
POST /admin/news/
GET /admin/news/{id}
DELETE /admin/news/{id}

Client API:
GET /client/news/

📄 License
MIT License © 2025
👤 Author
Created by Your Name — https://github.com/YOUR_USERNAME
