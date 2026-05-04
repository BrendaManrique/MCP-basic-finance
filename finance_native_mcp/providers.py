"""Finance data access layer with real and mock providers."""
from __future__ import annotations

import os
from typing import Any, Dict, List

from .data import MOCK_NEWS, MOCK_QUOTES

SUPPORTED_SYMBOLS = sorted(MOCK_QUOTES.keys())


def _use_mock_data() -> bool:
    return os.getenv("FINANCE_MCP_MOCK_DATA", "true").lower() in {"1", "true", "yes"}


def get_quote(symbol: str) -> Dict[str, Any]:
    symbol = symbol.upper()
    if symbol not in SUPPORTED_SYMBOLS:
        raise ValueError(f"Unsupported symbol '{symbol}'. Supported: {', '.join(SUPPORTED_SYMBOLS)}")

    if _use_mock_data():
        item = MOCK_QUOTES[symbol]
        change_pct = ((item["price"] - item["previous_close"]) / item["previous_close"]) * 100
        return {
            "symbol": symbol,
            "price": item["price"],
            "previous_close": item["previous_close"],
            "change_percent": round(change_pct, 2),
        }

    try:
        import yfinance as yf
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("yfinance is required when FINANCE_MCP_MOCK_DATA=false") from exc

    ticker = yf.Ticker(symbol)
    info = ticker.info
    price = info.get("regularMarketPrice")
    prev_close = info.get("regularMarketPreviousClose")
    if price is None or prev_close in (None, 0):
        raise RuntimeError(f"Price data unavailable for {symbol}")
    change_pct = ((price - prev_close) / prev_close) * 100
    return {
        "symbol": symbol,
        "price": price,
        "previous_close": prev_close,
        "change_percent": round(change_pct, 2),
    }


def get_profile(symbol: str) -> Dict[str, Any]:
    symbol = symbol.upper()
    if symbol not in SUPPORTED_SYMBOLS:
        raise ValueError(f"Unsupported symbol '{symbol}'. Supported: {', '.join(SUPPORTED_SYMBOLS)}")

    if _use_mock_data():
        item = MOCK_QUOTES[symbol]
        return {
            "symbol": symbol,
            "name": item["name"],
            "sector": item["sector"],
            "industry": item["industry"],
            "description": item["description"],
        }

    try:
        import yfinance as yf
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("yfinance is required when FINANCE_MCP_MOCK_DATA=false") from exc

    ticker = yf.Ticker(symbol)
    info = ticker.info
    name = info.get("shortName") or info.get("longName")
    if not name:
        raise RuntimeError(f"Profile data unavailable for {symbol}")
    return {
        "symbol": symbol,
        "name": name,
        "sector": info.get("sector") or "N/A",
        "industry": info.get("industry") or "N/A",
        "description": (info.get("longBusinessSummary") or "N/A")[:700],
    }


def get_top_movers(limit: int = 3) -> Dict[str, List[Dict[str, Any]]]:
    quotes = [get_quote(symbol) for symbol in SUPPORTED_SYMBOLS]
    ranked = sorted(quotes, key=lambda q: q["change_percent"], reverse=True)
    return {
        "gainers": ranked[:limit],
        "losers": list(reversed(ranked[-limit:])),
    }


def get_market_news(limit: int = 3) -> List[Dict[str, Any]]:
    if _use_mock_data():
        return MOCK_NEWS[:limit]
    # In a real deployment, wire this to your preferred news provider.
    return MOCK_NEWS[:limit]
