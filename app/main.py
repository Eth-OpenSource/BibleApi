from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        description="Ethiopic Open Bible API supporting 81-book EOTC canon",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # Update for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "ok"}

    # TODO: Include domain routers here
    # app.include_router(translations.router, prefix=settings.API_V1_STR)

    return app

app = create_app()
