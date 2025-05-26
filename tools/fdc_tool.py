import json
from pydantic import BaseModel, Field
from typing import List
from decimal import Decimal
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests

class DeliveryData(BaseModel):
    starting_date_time: str = Field(alias="StartingDateTime")
    ending_date_time: str = Field(alias="EndingDateTime")
    starting_height: float = Field(alias="StartingHeight")
    starting_volume: float = Field(alias="StartingVolume")
    starting_volume_tc: float = Field(alias="StartingVolumeTC")
    ending_height: float = Field(alias="EndingHeight")
    ending_volume: float = Field(alias="EndingVolume")
    ending_volume_tc: float = Field(alias="EndingVolumeTC")
    delivered_volume: float = Field(alias="DeliveredVolume")
    delivered_volume_tc: float = Field(alias="DeliveredVolumeTC")
    starting_water_height: float = Field(alias="StartingWaterHeight")
    starting_water_volume: float = Field(alias="StartingWaterVolume")
    ending_water_height: float = Field(alias="EndingWaterHeight")
    ending_water_volume: float = Field(alias="EndingWaterVolume")
    starting_temperature: float = Field(alias="StartingTemperature")
    ending_temperature: float = Field(alias="EndingTemperature")
    sales_volume: Decimal = Field(alias="SalesVolume")


class DeviceClass(BaseModel):
    type: str = Field(alias="Type")
    device_id: int = Field(alias="DeviceID")
    delivery_data: DeliveryData = Field(alias="DeliveryData")
    error_code: str = Field(alias="ErrorCode")


class FdcData(BaseModel):
    fdc_time_stamp: str = Field(alias="FDCTimeStamp")
    device_classes: List[DeviceClass] = Field(alias="DeviceClasses")


class TankDeliveryResponse(BaseModel):
    request_type: str = Field(alias="RequestType")
    application_sender: str = Field(alias="ApplicationSender")
    workstation_id: str = Field(alias="WorkstationID")
    request_id: int = Field(alias="RequestID")
    overall_result: str = Field(alias="OverallResult")
    fdc_data: FdcData = Field(alias="FDCdata")

class FdcService:
    """Service for communicating with the FDC server."""

    def __init__(self):
        """Initialize the FDC service."""
        self._base_url = "http://192.168.100.187:5070"

    async def get_tank_delivery(self, device_id: Optional[int] = None) -> Optional[TankDeliveryResponse]:
        """
        Get tank delivery information.

        Args:
            device_id: Optional device ID to filter results

        Returns:
            TankDeliveryResponse object or None if the request fails
        """
        url = f"{self._base_url}/tank-delivery"
        if device_id is not None:
            url += f"?device_id={device_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return TankDeliveryResponse.parse_obj(response.json())
        except Exception as e:
            print(f"Error fetching tank delivery data: {e}")
            return None


# MCP Server Fdc Tool

mcp = FastMCP("FdcToolPython")
fdc_service = FdcService()

@mcp.tool()
async def get_tanks_deliveries() -> TankDeliveryResponse:
    """
    Get the latest tank delivery data for all tanks.

    Returns:
        JSON string containing the tank delivery data
    """
    print("Get latest tank delivery data")
    response = await fdc_service.get_tank_delivery(None)
    return response

@mcp.tool()
async def get_tank_delivery(device_id: int) -> TankDeliveryResponse:
    """
    Get the latest tank delivery data for a specific tank.

    Args:
        device_id: The tank id, also specified as device id

    Returns:
        JSON string containing the tank delivery data
    """
    print(f"Get latest tank delivery data for device {device_id}")
    response = await fdc_service.get_tank_delivery(device_id)
    return response
