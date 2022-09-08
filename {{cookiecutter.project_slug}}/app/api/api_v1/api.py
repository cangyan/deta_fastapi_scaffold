from app.api.api_v1.endpoints import demo
from fastapi import APIRouter

router = APIRouter()
router.include_router(demo.router, prefix="/demo", tags=["demo"])
