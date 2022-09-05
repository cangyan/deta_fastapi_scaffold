
import uuid
from datetime import datetime

from app.base.config import settings
from app.base.logger import logger
from app.event.demo import DemoEvents
from app.schemas.request.demo import ReqDemoWriteLog
from app.schemas.response.common import RestfulResponse
from app.schemas.response.demo import Config, WriteLog
from fastapi import APIRouter
from fastapi_events.dispatcher import dispatch

router = APIRouter()


@router.get("/config", response_model=RestfulResponse[Config])
def config() -> RestfulResponse:
    config = Config(project_name=settings.PROJECT_NAME)

    return RestfulResponse(code=0, msg="成功", data=config)

@router.post("/write_log", response_model=RestfulResponse[WriteLog])
async def write_log(params: ReqDemoWriteLog)->RestfulResponse:
    if params.level == "info":
        logger.info(params.message)
    elif params.level == "error":
        logger.error(params.message)
    else:
        logger.debug(params.message)

    data = WriteLog(result="ok", message=params.message)
    return RestfulResponse(code=0, msg="成功", data=data)

@router.get("/event", response_model=RestfulResponse)
async def event() -> RestfulResponse:
    dispatch(
        DemoEvents.GET_CONFIG,
        {"id": uuid.uuid4(), "created_at": datetime.now()},
    )

    return RestfulResponse(code=0, msg="成功", data=None)
