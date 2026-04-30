"""Business logic for the Finance Research MCP.

This module abstracts the data retrieval logic away from the API layer. It
handles interactions with the yfinance library and provides a clean API
surface for the routes to consume.

If you wish to substitute yfinance with another data source (e.g., a database
or a premium API), you can modify or extend the functions here.
"""

from functools import lru_cache
from typing import List, Dict

import yfinance as yf

from .config import settings
from .schemas import StockQuote, CompanyProfile


class SymbolNotSupportedError(Exception):
    """Raised when an unsupported symbol is requested."""


@lru_cache(maxsize=128)
def fetch_ticker_info(symbol: str) -> Dict:
    """Fetch and cache ticker info using yfinance.

    This function caches the result to avoid multiple HTTP requests for the
    same symbol during the server's lifetime.

    Args:
        symbol: Ticker symbol.

    Returns:
        A dictionary with the ticker information.
    """
    ticker = yf.Ticker(symbol)
    return ticker.info


def get_stock_quote(symbol: str) -> StockQuote:
    """Return price and change percent for the given symbol.

    Args:
        symbol: Ticker symbol.

    Returns:
        StockQuote with price and percent change.

    Raises:
        SymbolNotSupportedError: If the symbol is not in the allowed list.
        ValueError: If price information is unavailable.
    """
    symbol = symbol.upper()
    if symbol not in settings.get_symbols():
        raise SymbolNotSupportedError(symbol)

    info = fetch_ticker_info(symbol)
    price = info.get("regularMarketPrice")
    prev_close = info.get("regularMarketPreviousClose")
    if price is None or prev_close is None or prev_close == 0:
        raise ValueError(f"Price data unavailable for symbol {symbol}.")

    change_pct = (price - prev_close) / prev_close * 100
    return StockQuote(symbol=symbol, price=price, change_percent=round(change_pct, 2))


def get_company_profile(symbol: str) -> CompanyProfile:
    """Return basic profile information for the given symbol.

    Args:
        symbol: Ticker symbol.

    Returns:
        CompanyProfile with name, sector, industry and description.

    Raises:
        SymbolNotSupportedError: If the symbol is not in the allowed list.
        ValueError: If company information is unavailable.
    """
    symbol = symbol.upper()
    if symbol not in settings.get_symbols():
        raise SymbolNotSupportedError(symbol)

    info = fetch_ticker_info(symbol)
    name = info.get("shortName") or info.get("longName")
    if not name:
        raise ValueError(f"Company name unavailable for symbol {symbol}.")
    sector = info.get("sector") or "N/A"
    industry = info.get("industry") or "N/A"
    description = info.get("longBusinessSummary") or "N/A"
    if description and len(description) > 500:
        description = description[:500] + "..."

    return CompanyProfile(
        symbol=symbol,
        name=name,
        sector=sector,
        industry=industry,
        description=description,
    )


def get_top_movers(count: int = 5) -> Dict[str, List[StockQuote]]:
    """Return top gainers and losers among supported symbols.

    Args:
        count: Number of gainers and losers to return.

    Returns:
        Dictionary with 'gainers' and 'losers' lists of StockQuote.
    """
    quotes: List[StockQuote] = []
    for symbol in settings.get_symbols():
        try:
            quotes.append(get_stock_quote(symbol))
        except Exception:
            continue
    if not quotes:
        return {"gainers": [], "losers": []}
    sorted_quotes = sorted(quotes, key=lambda q: q.change_percent, reverse=True)
    gainers = sorted_quotes[:count]
    losers = sorted_quotes[-count:][::-1]
    return {"gainers": gainers, "losers": losers}


def get_market_news() -> List[Dict[str, str]]:
    """Return placeholder finance news headlines.

    Replace this function's implementation with a call to a real news API
    as desired. The return value must be a list of dictionaries with
    'title' and 'link' keys to satisfy the expected schema.
    """
    return [
        {"title": "U.S. stocks rally on earnings optimism", "link": "https://example.com/news1"},
        {"title": "Tech sector leads gains amid strong AI demand", "link": "https://example.com/news2"},
        {"title": "Energy stocks slip as oil prices retreat", "link": "https://example.com/news3"},
    ]
