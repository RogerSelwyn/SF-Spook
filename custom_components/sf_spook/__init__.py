"""Main initialisation code."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, SupportsResponse

from .const import (
    DOMAIN,
)
from .schema import DEVICE_DELETE_SCHEMA, ENTITY_DELETE_SCHEMA
from .services import SFSpookServices

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):  # pylint: disable=unused-argument
    """Set up a config entry."""
    await async_do_service_setup(hass)

    return True


async def async_do_service_setup(hass: HomeAssistant):
    """Run the service setup."""

    services = SFSpookServices(hass)

    hass.services.async_register(
        DOMAIN,
        "device_delete",
        services.async_device_delete,
        DEVICE_DELETE_SCHEMA,
        SupportsResponse.ONLY,
    )
    hass.services.async_register(
        DOMAIN,
        "entity_delete",
        services.async_entity_delete,
        ENTITY_DELETE_SCHEMA,
        SupportsResponse.ONLY,
    )
