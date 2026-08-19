"""SF Spook Services."""

from homeassistant.const import ATTR_DEVICE_ID, ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import device_registry as dr, entity_registry as er


class SFSpookServices:
    """SF Spook Services."""

    hass: HomeAssistant

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the service."""
        self.hass = hass

    async def async_device_delete(self, call: ServiceCall):
        """Call to delete a device."""
        device_registry = dr.async_get(self.hass)
        device_id = call.data[ATTR_DEVICE_ID]
        device_registry.async_remove_device(device_id)

        return {"response": True}

    async def async_entity_delete(self, call: ServiceCall):
        """Call to delete a entity."""
        entity_registry = er.async_get(self.hass)
        entity_id = call.data[ATTR_ENTITY_ID]
        entity_registry.async_remove(entity_id)
        response = self.hass.states.async_remove(entity_id, call.context)

        return {"response": response}
