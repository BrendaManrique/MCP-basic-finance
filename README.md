# Finance Research MCP (Optimized)

This repository contains a professionally structured FastAPI application that can
be used as the basis for a Model Context Protocol (MCP) server.  The project
exposes endpoints for basic stock research (quotes, company profiles, top
movers) and placeholder market news.  It follows best practices for
maintainability and extensibility by separating configuration, schemas,
services and routing into dedicated modules.

## Features

* **Modular design**: Configuration, schemas, services and routes are split into
  their own modules for clarity and testability.
* **Type‑safe responses**: All endpoints return Pydantic models, which
  automatically validate and document the API.
* **Configurable symbols**: The list of supported stock tickers can be set via
  the `FINMCP_AVAILABLE_SYMBOLS` environment variable (comma‑separated values).
* **Caching**: Ticker information retrieved via `yfinance` is cached to
  minimize repeated network calls.
* **Error handling**: Custom exceptions and HTTP error responses provide
  meaningful messages when a symbol is unsupported or data is unavailable.

## Quick Start

1. **Clone** this repository or copy the `finance_mcp_optimized` directory.

2. **Install dependencies** (Python 3.9+ recommended):

   ```bash
   pip install fastapi uvicorn yfinance pydantic
   ```

3. **Run the server** using Uvicorn:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Explore the API** at `http://localhost:8000/docs` to view the automatically
   generated Swagger UI and test the endpoints.

## Environment Variables

The application's behavior can be customized via environment variables with the
prefix `FINMCP_`.  The `.env.example` file illustrates how to specify them.

| Variable | Description | Default |
| --- | --- | --- |
| `FINMCP_AVAILABLE_SYMBOLS` | Comma‑separated list of supported tickers | `AAPL,GOOG,MSFT,AMZN,TSLA,META,NVDA,NFLX,BRK-B,JPM,JNJ,V,PG,XOM` |

To override the default symbols, create a `.env` file based on `.env.example`
and update the `FINMCP_AVAILABLE_SYMBOLS` value.

## Deployment to MCPize

Once the API is running, you can deploy it to MCPize by pointing the **Public URL**
deployment option to your server's OpenAPI specification endpoint
(`http://your-host:8000/openapi.json`).  MCPize will analyze the spec and
generate an MCP server automatically.

## Extending the API

To add new functionality, create additional functions in `services.py` and
corresponding Pydantic models in `schemas.py`.  Then expose them through
`routes.py` by adding new endpoint functions decorated with appropriate
response models.
