from mcp.server.fastmcp import FastMCP

mcp = FastMCP("super-tools-mcp-server")

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("super-tools-mcp-server")

@mcp.tool()
async def get_tech_trends() -> list[str]:
    """Returns the top 5 trending active stories from Hacker News."""
    async with httpx.AsyncClient() as client:
        # Get top stories
        resp = await client.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        story_ids = resp.json()[:5]
        
        stories = []
        for sid in story_ids:
            story_resp = await client.get(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
            stories.append(story_resp.json().get("title", "Unknown"))
        return stories

@mcp.tool()
async def get_finance_trends() -> list[str]:
    """Returns the top 5 trending coins from CoinGecko."""
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.coingecko.com/api/v3/search/trending")
        data = resp.json()
        # Extract coin names from the trending list
        coins = [item["item"]["name"] for item in data["coins"][:5]]
        return coins

@mcp.tool()
async def get_entertainment_trends() -> list[str]:
    """Returns the top 5 trending movies from iTunes."""
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://itunes.apple.com/us/rss/topmovies/limit=5/json")
        data = resp.json()
        entries = data["feed"]["entry"]
        # Handle case where entries might be a dict if limit=1, but here limit=5
        movies = [entry["im:name"]["label"] for entry in entries]
        return movies

if __name__ == "__main__":
    mcp.run()
