"""Configuration flow for the skyq platform."""

# import logging
from typing import Self

from homeassistant.config_entries import CONN_CLASS_LOCAL_POLL, ConfigFlow

from .const import CONF_NAME, DOMAIN

# _LOGGER = logging.getLogger(__name__)


class SFSpookConfigFlow(ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    VERSION = 1
    CONNECTION_CLASS = CONN_CLASS_LOCAL_POLL

    # def __init__(self):
    #     """Initiliase the configuration flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        return self.async_create_entry(title=CONF_NAME, data={})

    def is_matching(self, other_flow: Self) -> bool:  # pragma: no cover
        """Return True if other_flow is matching this flow."""
        return False
