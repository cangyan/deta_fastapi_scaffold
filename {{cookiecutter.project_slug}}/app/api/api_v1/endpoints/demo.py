from typing import Any

from app.base.config import settings
from app.base.logger import logger
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/config")
def config() -> Any:
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    return {"msg": "Word received", "config": settings}
