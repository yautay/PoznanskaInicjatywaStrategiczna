from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # app.add_middleware(HTTPSRedirectMiddleware)
    # app.add_middleware(TrustedHostMiddleware, allowed_hosts=["baza-mrowino.pl", "*.baza-mrowino.pl", "localhost"])
    create_tables()
    include_router(app)
    return app


app = start_application()
