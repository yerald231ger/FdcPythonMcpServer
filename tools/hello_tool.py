# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 34

# Add an addition tool
@mcp.tool()
def add_35(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 35


# Add an addition tool
@mcp.tool()
def det_menus(a: int, b: int) -> list[str]:
    """Add two numbers"""
    return ["Mi menu 1", "Mi menu 2", "Mi menu 3" ]


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! from mcp"