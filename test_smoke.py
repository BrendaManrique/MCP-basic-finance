"""Smoke tests for Finance Research MCP business logic.

This file tests provider functions directly so you can validate the package even if
FastMCP is not installed in your current local environment yet.
"""
from finance_native_mcp.providers import get_market_news, get_profile, get_quote, get_top_movers, SUPPORTED_SYMBOLS


def main() -> None:
    assert SUPPORTED_SYMBOLS, "supported symbol list should not be empty"
    quote = get_quote("AAPL")
    assert quote["symbol"] == "AAPL"
    assert "price" in quote

    profile = get_profile("MSFT")
    assert profile["symbol"] == "MSFT"
    assert profile["name"]

    movers = get_top_movers(limit=2)
    assert len(movers["gainers"]) == 2
    assert len(movers["losers"]) == 2

    news = get_market_news(limit=2)
    assert len(news) == 2
    print("Smoke tests passed.")


if __name__ == "__main__":
    main()
