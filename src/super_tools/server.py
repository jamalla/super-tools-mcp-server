from mcp.server.fastmcp import FastMCP
from super_tools.tools.tech import get_tech_trends
from super_tools.tools.finance import get_finance_trends
from super_tools.tools.entertainment import get_entertainment_trends

# Initialize the MCP server
mcp = FastMCP("super-tools-mcp-server")

# Register tools
mcp.add_tool(get_tech_trends)
mcp.add_tool(get_finance_trends)
mcp.add_tool(get_entertainment_trends)

def main():
    """Entry point for the application script"""
    mcp.run()

if __name__ == "__main__":
    main()
