from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("/ping", response_class=PlainTextResponse, include_in_schema=False)
def ping() -> str:
    return "OK"
