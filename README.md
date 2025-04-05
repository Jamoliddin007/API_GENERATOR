# 🚀 API Generator (FastAPI)

API Generator is a dynamic backend automation platform built with **FastAPI**.  
It allows users to create, manage, and expose project-specific CRUD APIs on separate subdomains **without writing backend code** for each new project.

This platform is designed to:
- Support multiple independent projects
- Dynamically generate APIs based on user-defined models
- Separate admin and client permissions
- Provide secure access via Bearer tokens
- Allow integration with external backend services

---

## ✨ Features

- ✅ Multi-project API generation (each with its own DB and subdomain)
- ✅ Dynamic CRUD builder with custom fields and data types
- ✅ Separate API access: `/admin` and `/client`
- ✅ Method-level access control (e.g. create for admin only, read for clients)
- ✅ Auto-generated Bearer tokens
- ✅ Subdomain routing: `project.api-generator.uz`
- ✅ Swagger docs for every project: `/docs`
- ✅ External backend integration (connect third-party services)

---

## 🧱 Tech Stack

- **Backend:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Migrations:** Alembic
- **Auth:** JWT (Bearer Tokens)
- **Server:** Uvicorn
- **Containerization:** Docker
- **Routing:** NGINX (for subdomain support)

---
