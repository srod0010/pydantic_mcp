from fastmcp import FastMCP, Context

mcp = FastMCP('Server with sampling')


@mcp.tool()
async def poet(ctx: Context, theme: str) -> str:
    """Poem generator"""
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
    result = response.text.strip()
    return f"{result}"


if __name__ == "__main__":
    mcp.run()   # stdio
