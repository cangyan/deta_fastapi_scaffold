from fastapi import FastAPI
from fastapi_events.handlers.local import local_handler
from fastapi_events.middleware import EventHandlerASGIMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import router
from app.api.app.api import router as app_router
from app.api.common.api import router as common_router
from app.base.config import settings
from app.handler.demo import *
from app.middleware.debug_api import DebugApiMiddleware
from app.middleware.timeout import TimeoutMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


app.add_middleware(DebugApiMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler])
app.add_middleware(TimeoutMiddleware, timeout=settings.TIMEOUT)

app.include_router(router, prefix=settings.API_V1_STR)
app.include_router(common_router)
app.include_router(app_router, tags=["app"])
