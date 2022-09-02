import uuid
from datetime import datetime
from typing import Any

from app.base.config import settings
from app.base.logger import logger
from app.event.demo import DemoEvents
from fastapi import APIRouter, Depends
from fastapi_events.dispatcher import dispatch

router = APIRouter()


@router.get("/config")
def config() -> Any:
    # logger.debug("debug message")
    # logger.info("info message")
    # logger.warning("warning message")
    # logger.error("error message")
    # logger.critical("critical message")

    dispatch(
        DemoEvents.GET_CONFIG,
        {"id": uuid.uuid4(), "created_at": datetime.now()},
    )

    return {"msg": "Word received", "config": settings}
