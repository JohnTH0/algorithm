from fastapi import APIRouter

from app.api.endpoint import users, boards, posts

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(boards.router, prefix="/boards", tags=["boards"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])