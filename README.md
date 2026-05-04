# Finance Research MCP (Native MCP)

This is a **native MCP server** version of Finance Research MCP, built with **FastMCP**. FastMCP servers are created by instantiating `FastMCP`, decorating plain Python functions with `@mcp.tool`, and starting the server with `mcp.run()` according to the official FastMCP docs. citeturn125970search3turn125970search12

## What it does

The server exposes five finance research tools:
- `list_supported_symbols`
- `get_stock_quote`
- `get_company_profile`
- `get_top_movers_snapshot`
- `get_market_news_snapshot`

For local testing and safe first deploys, the project defaults to **mock data** via `FINANCE_MCP_MOCK_DATA=true`. Set it to `false` if you want to use `yfinance` for live quotes.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m finance_native_mcp.server
```

## Local testing

### 1. Verify imports
```bash
python -c "from finance_native_mcp.server import mcp; print(mcp)"
```

### 2. Verify provider logic
```bash
python test_smoke.py
```

### 3. Optional FastMCP inspection
If you have the FastMCP CLI available, inspect or run the server through the MCP tooling documented by FastMCP.

## Deploying on MCPize

MCPize says you can deploy either by connecting GitHub and auto-deploying on push or by using `mcpize deploy`, and it notes that adding `mcpize.yaml` configures runtime, secrets, and settings. citeturn125970search5turn125970search2

This repo includes a `mcpize.yaml` starter manifest so that once you push the repo, MCPize can trigger a deployment from GitHub.

## Recommended environment variables

- `FINANCE_MCP_MOCK_DATA=true` for safe demo mode
- `FINANCE_MCP_MOCK_DATA=false` for live `yfinance` mode

## Release checklist

1. Run `python test_smoke.py`
2. Start the server locally
3. Confirm MCPize sees the tools after deployment
4. Only then switch to live market data if desired
