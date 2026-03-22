from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import service
from .const import DOMAIN
from .storage import VendorOverrideStorage
from .api import VendorOverrideAPI
from .websocket import async_register_websocket

async def async_setup(hass: HomeAssistant, config: ConfigType):
    storage = VendorOverrideStorage(hass)
    await storage.async_load()

    # Register REST API
    hass.http.register_view(VendorOverrideAPI(storage))

    # Register WebSocket API
    await async_register_websocket(hass, storage)

    # Register service
    async def handle_set_override(call):
        mac = call.data["mac"]
        vendor = call.data["vendor"]
        await storage.set_override(mac, vendor)

    hass.services.async_register(DOMAIN, "set_override", handle_set_override)

    hass.data[DOMAIN] = storage
    return True
