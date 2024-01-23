from fastapi import APIRouter
from .posts import router as posts_router
from .projects import router as projects_router

router = APIRouter(prefix='/api')

router.include_router(posts_router)
router.include_router(projects_router)
