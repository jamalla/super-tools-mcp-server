import httpx

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
