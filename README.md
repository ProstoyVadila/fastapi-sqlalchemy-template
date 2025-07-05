# FastAPI application template

A Cookiecutter template for building FastAPI applications with SQLAlchemy and PostgreSQL.
Includes a ready-to-use Dockerfile and docker-compose.yaml, preconfigured default routes, a custom logger based on Loguru (optimized for both development and production), as well as helpful utilities and common boilerplate code.

## Quick Start

```bash
cookiecutter git@github.com:ProstoyVadila/fastapi-sqlalchemy-template.git
```

After a survey:
```bash
cd <your_project_slug>
```

and sync dependencies:
```bash
uv sync
```

