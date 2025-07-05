# FastAPI application template

This is a cookiecutter template of FastAPI application with SQLAlchemy for PostgreSQL. It contains ready `Dockerfile` and `compose.yaml`, default routes, configured custom logger (based on loguru) ready for development and production, some useful utils and common general code.

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

