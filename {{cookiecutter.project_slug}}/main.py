from typing import Union

import uvicorn
from fastapi import FastAPI

from app.api.api_v1.api import router
from app.config import settings

app = FastAPI()

app.include_router(router, prefix=settings.API_V1_STR)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
