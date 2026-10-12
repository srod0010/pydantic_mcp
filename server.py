from fastmcp import FastMCP

mcp = FastMCP("Sample")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def weather(loc: str) -> str:
    """Return weather for a given location"""
    return f"The weather in {loc} is sunny. 48 degrees Celsius."


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
