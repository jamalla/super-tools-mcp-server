import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "super-tools"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print(f"Found {len(tools.tools)} tools")

            print("\n--- Tech Trends (Hacker News) ---")
            tech = await session.call_tool("get_tech_trends")
            print(tech.content[0].text)

            print("\n--- Finance Trends (CoinGecko) ---")
            finance = await session.call_tool("get_finance_trends")
            print(finance.content[0].text)

            print("\n--- Entertainment Trends (iTunes) ---")
            ent = await session.call_tool("get_entertainment_trends")
            print(ent.content[0].text)

if __name__ == "__main__":
    asyncio.run(run())
