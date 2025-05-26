import json
import asyncio
from mcp.server.fastmcp import FastMCP
from services.fdc_service import FdcService

mcp = FastMCP("FdcTool")
fdc_service = FdcService()

@mcp.tool()
async def get_tanks_deliveries() -> str:
    """
    Get the latest tank delivery data for all tanks.

    Returns:
        JSON string containing the tank delivery data
    """
    print("Get latest tank delivery data")
    response = await fdc_service.get_tank_delivery(None)
    if response:
        return json.dumps(response.model_dump(by_alias=True))
    return json.dumps({"error": "Failed to retrieve tank delivery data"})

@mcp.tool()
async def get_tank_delivery(device_id: int) -> str:
    """
    Get the latest tank delivery data for a specific tank.
    
    Args:
        device_id: The tank id, also specified as device id
        
    Returns:
        JSON string containing the tank delivery data
    """
    print(f"Get latest tank delivery data for device {device_id}")
    response = await fdc_service.get_tank_delivery(device_id)
    if response:
        return json.dumps(response.model_dump(by_alias=True))
    return json.dumps({"error": f"Failed to retrieve tank delivery data for device {device_id}"})

if __name__ == "__main__":
    mcp.run()
