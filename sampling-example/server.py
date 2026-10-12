import sys
from fastmcp import FastMCP, Context

mcp = FastMCP('Server with sampling')


# NOTE: This server uses the *stdio* transport, which means it talks to the client
# over stdout. Any debug print MUST go to stderr (file=sys.stderr) — printing to
# stdout here would corrupt the MCP protocol messages flowing to the client.
def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


@mcp.tool()
async def poet(ctx: Context, theme: str) -> str:
    """Poem generator"""
    # [3] The agent (running in the client) decided to call this tool with a theme.
    log(f"[SERVER] poet() tool called with theme={theme!r}")

    # [4] SAMPLING: instead of generating the poem itself, the server asks the
    #     *client* to run an LLM completion on its behalf. ctx.sample(...) sends a
    #     "sampling/createMessage" request back over the connection to the client,
    #     which fulfils it using ITS model, then returns the text here.
    log("[SERVER] -> asking the CLIENT to generate a sample (ctx.sample)...")
    response = await ctx.sample(
        messages=f'''write a short poem (10 lines) about:
                    {theme}
                    IMPORTANT:
                    1. Give a suggested title.
                    2. Write the author name: Roboman II
                    3. Write publisher as: Morning Star''',
        system_prompt="You are an expert poem writer",
        temperature=0.7
    )
    # [6] The client sent the generated completion back to us.
    log("[SERVER] <- received sampled completion from the client")

    result = response.text.strip()
    # [7] Return the poem to the agent as this tool's result.
    return f"{result}"


if __name__ == "__main__":
    log("[SERVER] starting (stdio transport), waiting for the client...")
    mcp.run()   # stdio
