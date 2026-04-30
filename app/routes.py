"""API routes for the Finance Research MCP.

This module defines the FastAPI router and binds endpoints to the service
functions. It handles exceptions and returns Pydantic models as responses.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Dict

from . import services
from .schemas import StockQuote, CompanyProfile, TopMovers, NewsItem
from .config import settings

router = APIRouter()


@router.get("/available_symbols", response_model=List[str])
def list_available_symbols() -> List[str]:
    """Return the list of supported stock symbols."""
    return settings.get_symbols()


@router.get("/stock_quote/{symbol}", response_model=StockQuote)
def get_stock_quote(symbol: str) -> StockQuote:
    """Return price and change percent for the given symbol."""
    try:
        return services.get_stock_quote(symbol)
    except services.SymbolNotSupportedError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Symbol '{symbol}' is not supported.")
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))


@router.get("/company_profile/{symbol}", response_model=CompanyProfile)
def get_company_profile(symbol: str) -> CompanyProfile:
    """Return basic company profile for the given symbol."""
    try:
        return services.get_company_profile(symbol)
    except services.SymbolNotSupportedError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Symbol '{symbol}' is not supported.")
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))


@router.get("/top_movers", response_model=TopMovers)
def get_top_movers(count: int = 5) -> TopMovers:
    """Return top gainers and losers among supported symbols."""
    result = services.get_top_movers(count)
    return TopMovers(gainers=result["gainers"], losers=result["losers"])


@router.get("/market_news", response_model=List[NewsItem])
def get_market_news() -> List[NewsItem]:
    """Return placeholder finance news headlines."""
    news_data = services.get_market_news()
    return [NewsItem(**item) for item in news_data]
