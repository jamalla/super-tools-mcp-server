import httpx

async def get_finance_trends() -> list[str]:
    """Returns the top 5 trending coins from CoinGecko."""
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.coingecko.com/api/v3/search/trending")
        data = resp.json()
        # Extract coin names from the trending list
        coins = [item["item"]["name"] for item in data["coins"][:5]]
        return coins
