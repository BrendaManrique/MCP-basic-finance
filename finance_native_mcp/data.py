"""Fallback mock data for local testing and offline development."""

MOCK_QUOTES = {
    "AAPL": {
        "price": 175.0,
        "previous_close": 170.0,
        "name": "Apple Inc.",
        "sector": "Technology",
        "industry": "Consumer Electronics",
        "description": "Apple designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories.",
    },
    "MSFT": {
        "price": 420.0,
        "previous_close": 416.0,
        "name": "Microsoft Corporation",
        "sector": "Technology",
        "industry": "Software—Infrastructure",
        "description": "Microsoft develops and supports software, cloud services, devices, and AI platforms.",
    },
    "NVDA": {
        "price": 1110.0,
        "previous_close": 1084.0,
        "name": "NVIDIA Corporation",
        "sector": "Technology",
        "industry": "Semiconductors",
        "description": "NVIDIA builds GPUs and accelerated computing platforms used in gaming, AI, and data centers.",
    },
    "AMZN": {
        "price": 186.0,
        "previous_close": 184.0,
        "name": "Amazon.com, Inc.",
        "sector": "Consumer Cyclical",
        "industry": "Internet Retail",
        "description": "Amazon operates e-commerce, cloud computing, digital media, and logistics businesses.",
    },
    "TSLA": {
        "price": 179.0,
        "previous_close": 182.0,
        "name": "Tesla, Inc.",
        "sector": "Consumer Cyclical",
        "industry": "Auto Manufacturers",
        "description": "Tesla designs and manufactures electric vehicles, batteries, and energy generation systems.",
    },
}

MOCK_NEWS = [
    {"title": "Large-cap tech extends gains as AI spending remains strong", "source": "Mock Wire", "url": "https://example.com/ai-spending"},
    {"title": "Market participants watch inflation data ahead of Fed commentary", "source": "Mock Journal", "url": "https://example.com/inflation-fed"},
    {"title": "Semiconductor names lead momentum after bullish guidance", "source": "Mock Markets", "url": "https://example.com/semis-guidance"},
]
