from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from {{ cookiecutter.package_name }}.lifespan import lifespan
from {{ cookiecutter.package_name }}.api.middlewares import ThrottlingMiddleware
from {{ cookiecutter.package_name }}.api.router import router


app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    version="0.0.1",
    lifespan=lifespan,
)


# metrics
Instrumentator().instrument(app).expose(app)

# middlewares
app.add_middleware(ThrottlingMiddleware)

# routers
app.include_router(router)
