"""Entry point for the Finance Research MCP FastAPI application.

This module creates the FastAPI application, configures routers and
middleware, and exposes it for use with ASGI servers like Uvicorn.
"""

from fastapi import FastAPI

from .routes import router as api_router

app = FastAPI(
    title="Finance Research API",
    description="Optimized API for basic stock research and news.",
    version="1.0.0",
)

app.include_router(api_router)
