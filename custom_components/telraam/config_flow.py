"""Config flow for Telraam integration."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp
import async_timeout
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from .const import (
    DOMAIN,
    CONF_SEGMENT_ID,
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    API_BASE_URL,
    API_ENDPOINT,
)

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_SEGMENT_ID): str,
    }
)


async def validate_segment_id(hass: HomeAssistant, segment_id: str) -> dict[str, Any]:
    """Validate the segment ID by making a test API call."""
    from datetime import date
    today = date.today().isoformat()
    
    url = f"{API_BASE_URL}/{API_ENDPOINT}/{segment_id}/{today}/{today}"
    
    try:
        async with async_timeout.timeout(10):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 404:
                        raise InvalidSegmentID
                    if response.status != 200:
                        raise CannotConnect
                    
                    data = await response.json()
                    
                    if "data" not in data:
                        raise InvalidSegmentID
                    
                    return {"title": f"Telraam {segment_id}"}
    except aiohttp.ClientError:
        raise CannotConnect
    except Exception:
        raise CannotConnect


class TelraamConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Telraam."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        
        if user_input is not None:
            segment_id = user_input[CONF_SEGMENT_ID]
            
            # Prüfe ob diese Segment ID bereits konfiguriert ist
            await self.async_set_unique_id(segment_id)
            self._abort_if_unique_id_configured()
            
            try:
                info = await validate_segment_id(self.hass, segment_id)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidSegmentID:
                errors["base"] = "invalid_segment_id"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> TelraamOptionsFlowHandler:
        """Get the options flow for this handler."""
        return TelraamOptionsFlowHandler(config_entry)


class TelraamOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle Telraam options."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_SCAN_INTERVAL,
                        default=self.config_entry.options.get(
                            CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=60, max=3600)),
                }
            ),
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidSegmentID(HomeAssistantError):
    """Error to indicate the segment ID is invalid."""
