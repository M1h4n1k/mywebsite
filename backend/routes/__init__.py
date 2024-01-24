from fastapi import APIRouter
from .posts import router as posts_router
from .projects import router as projects_router
from .other import router as other_router

router = APIRouter(prefix='/api')

router.include_router(posts_router)
router.include_router(projects_router)
router.include_router(other_router)
