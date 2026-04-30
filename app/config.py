"""Application configuration for the Finance Research MCP.

This module provides a lightweight configuration object without relying on
`pydantic` or external dependencies.  The original version used
`pydantic.BaseSettings`, which has been removed in Pydantic 2.x.  To keep
the project runnable in constrained environments, we implement a basic
settings class that reads from environment variables and supplies
defaults.

If you prefer to use `pydantic-settings` in your own environment, you can
replace this implementation with the appropriate class.
"""

import os
from typing import List


class Settings:
    """Minimal settings container for the Finance Research MCP.

    This class reads configuration from environment variables prefixed with
    ``FINMCP_``.  Only the ``available_symbols`` variable is currently
    supported.  Additional configuration options can be added as
    attributes with appropriate default values.
    """

    def __init__(self) -> None:
        default_symbols = (
            "AAPL,GOOG,MSFT,AMZN,TSLA,META,NVDA,NFLX,BRK-B,JPM,JNJ,V,PG,XOM"
        )
        # Read from environment; fall back to defaults if not set.
        self.available_symbols: str = os.getenv(
            "FINMCP_AVAILABLE_SYMBOLS", default_symbols
        )

    def get_symbols(self) -> List[str]:
        """Return the list of supported symbols as upper-case strings."""
        return [
            sym.strip().upper()
            for sym in self.available_symbols.split(",")
            if sym.strip()
        ]


# Singleton settings instance
settings = Settings()
