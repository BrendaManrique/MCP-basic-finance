"""Application configuration for Finance Research MCP.

This module defines a simple settings class for configuring runtime options.
Use environment variables to override defaults. You can extend this class to
include API keys or other settings.
"""

from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Configuration values loaded from environment variables.

    Attributes:
        available_symbols: A comma‑separated string of stock tickers that the
            application supports. Defaults to a curated list of tech and
            consumer blue‑chip stocks.
    """

    available_symbols: str = (
        "AAPL,GOOG,MSFT,AMZN,TSLA,META,NVDA,NFLX,BRK-B,JPM,JNJ,V,PG,XOM"
    )

    class Config:
        env_prefix = "FINMCP_"

    def get_symbols(self) -> List[str]:
        """Return the list of supported symbols as upper-case strings."""
        return [sym.strip().upper() for sym in self.available_symbols.split(",") if sym.strip()]


# Singleton settings instance
settings = Settings()
