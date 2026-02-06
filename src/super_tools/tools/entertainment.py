import httpx

async def get_entertainment_trends() -> list[str]:
    """Returns the top 5 trending movies from iTunes."""
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://itunes.apple.com/us/rss/topmovies/limit=5/json")
        data = resp.json()
        entries = data["feed"]["entry"]
        # Handle case where entries might be a dict if limit=1, but here limit=5
        movies = [entry["im:name"]["label"] for entry in entries]
        return movies
