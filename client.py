import asyncio
from dotenv import load_dotenv
from pydantic_ai.mcp import MCPServerStreamableHTTP
from pydantic_ai import Agent

load_dotenv()

server = MCPServerStreamableHTTP(url='http://127.0.0.1:8000/mcp')

agent = Agent('openai:gpt-4o', mcp_servers=[server])


async def main():

    async with agent.run_mcp_servers():
        result = await agent.run(
            'What is the weather at Delhi?'
        )

    print(result.output)

if __name__ == "__main__":
    asyncio.run(main())
