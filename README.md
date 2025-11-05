# 🐍 FastAPI Practice App

A simple **FastAPI** application built to explore and practice core backend concepts such as:

- 🔐 Authentication and Authorization  
- 🧪 Unit and Integration Testing  
- 🗃️ Data Migration  
- 🧩 Dependency Injection  

This project serves as a learning environment to strengthen backend development skills with modern Python tools and practices.

---

## 🚀 Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** – High-performance web framework for building APIs  
- **[uv](https://docs.astral.sh/uv/)** – Ultra-fast Python package and environment manager  
- **[SQLAlchemy](https://www.sqlalchemy.org/)** – ORM for data models and migrations  
- **[Pytest](https://pytest.org/)** – Testing framework for Python  
- **[Pydantic](https://docs.pydantic.dev/)** – Data validation and settings management  

---

## 🛠️ Installation

Make sure you have **uv** installed globally:

```bash
pip install uv
```

Clone the repository and navigate into it:

```bash
git clone https://github.com/ianalt/fastapi-todo-app.git
cd fastapi-todo-app
```

Create and activate a new virtual environment with **uv**:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate.bat
```

Install dependencies:

```bash
uv sync # based on uv.lock and pyproject.toml
```

---

## ▶️ Running the Application

Start the FastAPI server using **uv** itself:

```bash
uv run fastapi dev
```

The app will be available at:

👉 [http://localhost:8000](http://localhost:8000)

You can also access the interactive API docs:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧠 Learning Goals

This repository is designed to help understand:

- How to structure a scalable FastAPI project  
- Implementing secure authentication and role-based authorization  
- Applying dependency injection effectively in FastAPI  
- Writing maintainable unit and integration tests  
- Managing data migrations with SQLAlchemy + Alembic  

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify for your own learning.

---

## ✨ Author

Developed by [Ian Alt](https://github.com/ianalt) – focused on building solid backend architectures with Python and FastAPI.