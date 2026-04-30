"""A minimal stub implementation of the `yfinance` package used for testing.

This stub allows the Finance Research MCP to be run and tested in environments
where the real ``yfinance`` package is unavailable (e.g. offline or restricted
build systems).  It defines a ``Ticker`` class that returns hardcoded data for
several well‑known stock symbols.  If a symbol is not recognized, the stub
returns an empty ``info`` dictionary.

Note: This stub is **not** intended for production use.  It exists solely to
facilitate local testing of the MCP without requiring network access.
"""

from typing import Dict


class Ticker:
    """Return a minimal representation of a stock ticker.

    The `info` attribute emulates the dictionary returned by the real
    ``yfinance.Ticker.info`` property.  It contains fields such as
    ``regularMarketPrice``, ``regularMarketPreviousClose``, ``shortName``,
    ``longName``, ``sector``, ``industry`` and ``longBusinessSummary``.

    Args:
        symbol: The stock symbol (case insensitive).
    """

    _mock_data: Dict[str, Dict[str, object]] = {
        "AAPL": {
            "regularMarketPrice": 175.0,
            "regularMarketPreviousClose": 170.0,
            "shortName": "Apple Inc.",
            "longName": "Apple Inc.",
            "sector": "Technology",
            "industry": "Consumer Electronics",
            "longBusinessSummary": "Apple Inc. designs, manufactures, and sells smartphones, personal computers, tablets, wearables, and accessories worldwide.",
        },
        "GOOG": {
            "regularMarketPrice": 120.0,
            "regularMarketPreviousClose": 118.0,
            "shortName": "Alphabet Inc.",
            "longName": "Alphabet Inc.",
            "sector": "Communication Services",
            "industry": "Internet Content & Information",
            "longBusinessSummary": "Alphabet Inc. provides online advertising services in the United States and internationally.",
        },
        "MSFT": {
            "regularMarketPrice": 310.0,
            "regularMarketPreviousClose": 305.0,
            "shortName": "Microsoft Corporation",
            "longName": "Microsoft Corporation",
            "sector": "Technology",
            "industry": "Software—Infrastructure",
            "longBusinessSummary": "Microsoft Corporation develops, licenses, and supports software products, services, and devices worldwide.",
        },
        "AMZN": {
            "regularMarketPrice": 140.0,
            "regularMarketPreviousClose": 138.0,
            "shortName": "Amazon.com, Inc.",
            "longName": "Amazon.com, Inc.",
            "sector": "Consumer Cyclical",
            "industry": "Internet Retail",
            "longBusinessSummary": "Amazon.com, Inc. engages in the retail sale of consumer products and subscriptions worldwide.",
        },
        "TSLA": {
            "regularMarketPrice": 220.0,
            "regularMarketPreviousClose": 215.0,
            "shortName": "Tesla, Inc.",
            "longName": "Tesla, Inc.",
            "sector": "Consumer Cyclical",
            "industry": "Auto Manufacturers",
            "longBusinessSummary": "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles and energy generation and storage systems.",
        },
    }

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol.upper()

    @property
    def info(self) -> Dict[str, object]:
        """Return mock ticker information for the symbol.

        If the symbol is not in the predefined mock data, return an empty
        dictionary.  The Finance MCP will handle missing fields by raising
        appropriate errors.
        """
        return self._mock_data.get(self.symbol, {})


__all__ = ["Ticker"]
