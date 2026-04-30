"""Pydantic models for the Finance Research MCP API.

These models ensure consistent request and response schemas and enable
automatic validation and OpenAPI generation with FastAPI.
"""

from typing import List, Optional
from pydantic import BaseModel


class StockQuote(BaseModel):
    """Represents price data for a stock."""

    symbol: str
    price: float
    change_percent: float


class CompanyProfile(BaseModel):
    """Represents basic company profile information."""

    symbol: str
    name: str
    sector: str
    industry: str
    description: Optional[str] = None


class TopMovers(BaseModel):
    """Represents top gainers and losers among supported symbols."""

    gainers: List[StockQuote]
    losers: List[StockQuote]


class NewsItem(BaseModel):
    """Represents a news headline and link."""

    title: str
    link: str
