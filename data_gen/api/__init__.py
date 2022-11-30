from fastapi import APIRouter
from .gen import router as include_router

router = APIRouter()
router.include_router(include_router)