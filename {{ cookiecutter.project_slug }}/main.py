import uvicorn

from {{ cookiecutter.package_name }}.settings.logger import logger
from {{ cookiecutter.package_name }}.settings.config import config


def main():
    logger.info("Hello from autocare-ml-service!")


if __name__ == "__main__":
    logger.warning(config)
    uvicorn.run(
        "{{ cookiecutter.package_name }}.app:app",
        host=config.app.host,
        port=config.app.port,
        workers=config.app.workers,
        reload=config.reload,
        log_config=None,  # Disable Uvicorn's default logging config to use our custom logger
    )
