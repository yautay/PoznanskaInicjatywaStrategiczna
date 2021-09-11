from fastapi import APIRouter

from apis.version_1 import \
    route_users, \
    route_articles, \
    route_login, \
    route_bgg

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/user", tags=["user"])
api_router.include_router(route_articles.router, prefix="/article", tags=["article"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
# api_router.include_router(route_bgg.router, prefix="/bgg", tags=["bgg"])
