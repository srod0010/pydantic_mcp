from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
import asyncio
from dotenv import load_dotenv

load_dotenv()

server = MCPServerStdio(command='python', args=['server.py'])
agent = Agent('openai:gpt-4o', mcp_servers=[server])


async def main():
    async with agent.run_mcp_servers():
        result = await agent.run('Write a poem on robots.')
    print(result.output)

if __name__ == "__main__":
    asyncio.run(main())
