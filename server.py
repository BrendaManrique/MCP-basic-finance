"""Native Finance Research MCP server built with FastMCP."""
from __future__ import annotations

from fastmcp import FastMCP

from .providers import SUPPORTED_SYMBOLS, get_market_news, get_profile, get_quote, get_top_movers

mcp = FastMCP("Finance Research MCP")


@mcp.tool
def list_supported_symbols() -> list[str]:
    """Return the list of supported stock symbols."""
    return SUPPORTED_SYMBOLS


@mcp.tool
def get_stock_quote(symbol: str) -> dict:
    """Return quote data for a supported symbol, including last price and daily percent change."""
    return get_quote(symbol)


@mcp.tool
def get_company_profile(symbol: str) -> dict:
    """Return a company profile for a supported symbol."""
    return get_profile(symbol)


@mcp.tool

def get_top_movers_snapshot(limit: int = 3) -> dict:
    """Return the current top gainers and losers among supported symbols."""
    return get_top_movers(limit=limit)


@mcp.tool

def get_market_news_snapshot(limit: int = 3) -> list[dict]:
    """Return recent market headlines for quick research workflows."""
    return get_market_news(limit=limit)


if __name__ == "__main__":
    mcp.run()
