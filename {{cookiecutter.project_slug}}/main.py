import uvicorn
from fastapi import FastAPI
from fastapi_events.handlers.local import local_handler
from fastapi_events.middleware import EventHandlerASGIMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import router
from app.api.common.api import router as common_router
from app.base.config import settings
from app.handler import *
from app.middleware.debug_api import DebugApiMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

@app.on_event("startup")
async def startup() -> None:
    Instrumentator().instrument(app).expose(app, include_in_schema=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler])

app.add_middleware(DebugApiMiddleware)

app.include_router(router, prefix=settings.API_V1_STR)
app.include_router(common_router)


def start() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run(
        "main:app", host="0.0.0.0", port=8000, reload=True, loop="asyncio"
    )
