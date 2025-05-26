import asyncio
from tools.fdc_tool import FdcService, get_tanks_deliveries


# Test fdc service
async def main():
    fdc_service = FdcService()
    result = await fdc_service.get_tank_delivery(1)
    print(result)
    result = await get_tanks_deliveries()
    print(result)

# Run the async function
asyncio.run(main())
