from fastapi import APIRouter

from {{ cookiecutter.package_name }}.api.default import default_router


router = APIRouter()
router.include_router(default_router)
