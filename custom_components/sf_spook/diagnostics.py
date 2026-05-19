"""Diagnostics support for SF Spook."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant,  # pylint: disable=unused-argument
    entry: ConfigEntry,
) -> dict:
    """Return diagnostics for a config entry."""
    return {
        "name": entry.title,
        "config_entry_data": dict(entry.data),
    }
