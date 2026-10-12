from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
import asyncio
from dotenv import load_dotenv

load_dotenv()

# [1] The client launches server.py as a subprocess and talks to it over stdio.
#     Because transport is stdio, the server's protocol messages come over its
#     stdout; its debug logs come over stderr (see server.py).
server = MCPServerStdio(command='python', args=['server.py'])
agent = Agent('openai:gpt-4o', mcp_servers=[server])


async def main():
    # Control flow of the sampling round-trip:
    #   [1] client starts the server subprocess (above)
    #   [2] client's agent sends the prompt to its model (gpt-4o)
    #   [3] the model calls the server's `poet` tool  ........... (server.py)
    #   [4] the server calls ctx.sample(...) -> asks THIS client to generate  (server.py)
    #   [5] this client runs the sampling request on its model and returns the text  <-- here
    #   [6] the server receives the sampled text  ............... (server.py)
    #   [7] the server returns the poem as the tool result  ..... (server.py)
    #   [8] the agent produces the final answer, printed below
    async with agent.run_mcp_servers():
        print("[CLIENT] connected to server; sending prompt to the agent...", flush=True)
        # [2] Send the user prompt. The client will also [5] serve the server's
        #     sampling request transparently using the agent's model.
        result = await agent.run('Write a poem on robots.')
        print("[CLIENT] agent run finished.", flush=True)

    # [8] Final output assembled by the agent.
    print("\n[CLIENT] final output:\n")
    print(result.output)

if __name__ == "__main__":
    asyncio.run(main())
