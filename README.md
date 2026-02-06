# Super Tools MCP Server

A Model Context Protocol (MCP) server that provides trending keyword tools.

## Tools

1.  **`get_tech_trends`**: Returns trending technology keywords (e.g., "AI Agents", "Rust").
2.  **`get_finance_trends`**: Returns trending finance keywords (e.g., "Crypto ETFs", "Green Bonds").
3.  **`get_entertainment_trends`**: Returns trending entertainment keywords (e.g., "Immersive VR", "Indie Game Revival").

## How to Consume (Usage Methods)

### Method 1: Claude Desktop (Recommended)

To use these tools within Claude Desktop:

1.  Make sure you have [Claude Desktop](https://claude.ai/download) installed.
2.  Locate your config file:
    *   **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
    *   **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
3.  Add the server to the configuration:

```json
{
  "mcpServers": {
    "super-tools": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp",
        "python",
        "d:\\00_DS-ML-Workspace\\super-tools-mcp-server\\main.py"
      ]
    }
  }
}
```
*Note: Adjust the path if you moved the project.*

4.  Restart Claude Desktop. The hammer icon should appear, letting you attach these tools to your chats.

### Method 2: MCP Inspector (Development & Testing)

The MCP Inspector is a web-based tool to test and inspect your server.

**Run directly with `mcp` CLI:**

```bash
# Make sure mcp CLI is installed
pip install mcp-cli

# Run the inspector
mcp dev main.py
```

Or if using `uv`:

```bash
uvx mcp-cli dev main.py
```

This will open a URL (usually `localhost:5173`) where you can list tools and simulate calls.

### Method 3: Programmatic (MCP Client)

You can connect to this server programmatically using any MCP-compliant client library (Python, TypeScript, etc.).

**example_client.py** (Python):

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    server_params = StdioServerParameters(
        command="python",
        args=["main.py"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize
            await session.initialize()

            # List tools
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")

            # Call a tool
            result = await session.call_tool("get_tech_trends")
            print(f"Tech Trends: {result.content}")

if __name__ == "__main__":
    asyncio.run(run())
```