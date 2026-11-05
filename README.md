# SukaKasir Backend

REST API backend for **SukaKasir**, a cashier application that provides product data management and transaction recording. This repository focuses on providing APIs and database integration, allowing client applications to communicate with data in a structured manner.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
</p>

## Table of Contents

- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Technologies](#technologies)
- [Architecture](#architecture)
- [Running the Project Locally](#running-the-project-locally)
- [Documentation and Endpoints](#documentation-and-endpoints)
- [Related Repository](#related-repository)

## About the Project

SukaKasir Backend is a backend service designed to support data management requirements for a cashier application. It provides endpoints for entities such as categories, units, products, suppliers, transactions, and transaction items.

This project was developed as part of the SukaKasir application development process and as a backend development portfolio project. Its implementation focuses on REST API design, separation of responsibilities between application layers, relational database integration, data validation, and database schema change management.

## Key Features

| Module | Description |
|---|---|
| **Category Management** | Manage categories used to organize products. |
| **Unit Management** | Manage units of measurement used by products. |
| **Product Management** | Provide APIs for managing product data. |
| **Supplier Management** | Manage supplier information. |
| **Product–Supplier** | Manage relationships between products and suppliers. |
| **Transaction Management** | Manage transaction records. |
| **Transaction Items** | Store and manage item details associated with transactions. |
| **Transaction Types** | Manage transaction types. |

## Technologies

| Technology | Role |
|---|---|
| [Python](https://www.python.org/) | Backend programming language. |
| [FastAPI](https://fastapi.tiangolo.com/) | Framework for building REST APIs. |
| [Pydantic](https://docs.pydantic.dev/) | Request and response data validation and structuring. |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM for database interaction. |
| [PostgreSQL](https://www.postgresql.org/) | Relational database. |
| [Alembic](https://alembic.sqlalchemy.org/) | Database schema migration management. |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server for running the FastAPI application. |
| [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | Python SDK available for integration with S3-based storage services. |

## Architecture

In general, requests from the frontend or API client are forwarded to FastAPI routers, processed using schemas and application logic, and then interact with the database through SQLAlchemy.

```text
Frontend / API Client
        |
        | HTTP Request
        v
   FastAPI Router
        |
        v
      Schema
        |
        v
      Service
        |
        v
    Repository
        |
        v
  SQLAlchemy ORM
        |
        v
    PostgreSQL
        |
        v
   HTTP Response
```

### Repository Structure

```text
SukaKasir_backend/
├── alembic/          # Database migration history and configuration
├── api/              # API routers and endpoints
├── core/             # Application configuration and core components
├── database/         # Database connections and sessions
├── helper/           # Utility functions used by the application
├── models/           # Database models/entities
├── repository/       # Data access layer
├── schemas/          # Request and response schemas
├── service/          # Application service logic
├── .env.example      # Example environment variables
├── alembic.ini       # Alembic configuration
├── main.py           # FastAPI application entry point
└── requirements.txt  # Python dependencies
```

## Running the Project Locally

### Prerequisites

Make sure the following tools are installed on your machine:

- Python and `pip`.
- PostgreSQL.
- Git.

### 1. Clone the Repository

```bash
git clone https://github.com/Fariz1703/SukaKasir_backend.git
cd SukaKasir_backend
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up the Database and Environment Variables

Create a PostgreSQL database, for example:

```sql
CREATE DATABASE sukakasir;
```

Copy the example environment file:

```bash
cp .env.example .env
```

On Windows Command Prompt, use `copy .env.example .env` instead.

Next, review and adjust the `.env` file according to your local configuration. Example environment variables:

```env
DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost:5432/sukakasir
FILEBASE_ACCESS_KEY=your_access_key
FILEBASE_SECRET_KEY=your_secret_key
FILEBASE_BUCKET=product-images
```

Adjust the username, password, host, port, database name, and storage credentials according to your environment.

Do not commit the `.env` file or actual credentials to a public repository.

### 5. Run Database Migrations

```bash
alembic upgrade head
```

This command applies the available Alembic migrations to the configured database.

### 6. Run the Development Server

```bash
uvicorn main:app --reload
```

By default, the application will be accessible at:

`http://127.0.0.1:8000`

## Documentation and Endpoints

FastAPI provides interactive documentation for viewing endpoints, schemas, parameters, and testing requests and responses.

**Local Environment:**

- **Local Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Local Web Swagger UI:** [http://127.0.0.1:8000/web/docs](http://127.0.0.1:8000/web/docs)
- **Local Mobile Swagger UI:** [http://127.0.0.1:8000/mobile/docs](http://127.0.0.1:8000/mobile/docs)

**Deployment Environment:**

- **Deployment Base URL:** [https://suka-kasir-backend.vercel.app](https://suka-kasir-backend.vercel.app)
- **Deployment Web Swagger UI:** [https://suka-kasir-backend.vercel.app/web/docs](https://suka-kasir-backend.vercel.app/web/docs)
- **Deployment Mobile Swagger UI:** [https://suka-kasir-backend.vercel.app/mobile/docs](https://suka-kasir-backend.vercel.app/mobile/docs)

The following health-check endpoints are defined directly in the application:

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Checks whether the API is running. |
| `GET` | `/test-db` | Checks the database connection using a simple query. |

Endpoints for category, unit, product, supplier, and transaction modules can be explored through Swagger UI after starting the server.

Specific paths and payload formats are not listed here to ensure they remain consistent with the actual implementation.

## Related Repository

- **Android Application:** [LackFos/suka-kasir-mobile](https://github.com/LackFos/suka-kasir-mobile)

---

Developed as the backend for the SukaKasir application using Python, FastAPI, and PostgreSQL.
