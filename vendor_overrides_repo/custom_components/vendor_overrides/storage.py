from homeassistant.helpers.storage import Store
from .const import DOMAIN, STORAGE_KEY, STORAGE_VERSION

class VendorOverrideStorage:
    def __init__(self, hass):
        self.hass = hass
        self.store = Store(hass, STORAGE_VERSION, f"{DOMAIN}/{STORAGE_KEY}")
        self.data = {}

    async def async_load(self):
        stored = await self.store.async_load()
        if stored:
            self.data = stored
        else:
            self.data = {}

    async def async_save(self):
        await self.store.async_save(self.data)

    def get_table(self):
        return self.data

    async def set_override(self, mac, vendor):
        mac = mac.upper()
        self.data[mac] = vendor
        await self.async_save()

    def resolve_vendor(self, mac, auto_vendor=None):
        mac = mac.upper()
        # Manual override always wins
        if mac in self.data:
            return self.data[mac]
        return auto_vendor
