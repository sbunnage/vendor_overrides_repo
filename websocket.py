from homeassistant.components.http import HomeAssistantView
from .const import DOMAIN

class VendorOverrideAPI(HomeAssistantView):
    url = "/api/vendor_overrides/table"
    name = "api:vendor_overrides"
    requires_auth = True

    def __init__(self, storage):
        self.storage = storage

    async def get(self, request):
        return self.json(self.storage.get_table())
