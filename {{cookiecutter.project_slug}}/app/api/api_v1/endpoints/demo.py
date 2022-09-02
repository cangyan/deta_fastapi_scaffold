from typing import Any

from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/config")
def config() -> Any:
    return {"msg": "Word received"}
