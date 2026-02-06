from mcp.server.fastmcp import FastMCP

mcp = FastMCP("super-tools-mcp-server")

@mcp.tool()
def get_tech_trends() -> list[str]:
    """Returns the top 5 trending technology keywords."""
    return ["AI Agents", "Quantum Computing", "Rust", "WebAssembly", "Edge Computing"]

@mcp.tool()
def get_finance_trends() -> list[str]:
    """Returns the top 5 trending finance keywords."""
    return ["Crypto ETFs", "Decentralized Finance", "Green Bonds", "Algorithmic Trading", "Micro-investing"]

@mcp.tool()
def get_entertainment_trends() -> list[str]:
    """Returns the top 5 trending entertainment keywords."""
    return ["Immersive VR", "Interactive Streaming", "Short-form Video", "Indie Game Revival", "Virtual Concerts"]

if __name__ == "__main__":
    mcp.run()
