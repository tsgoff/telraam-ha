"""The Telraam integration."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
import aiohttp
import async_timeout

from .const import (
    DOMAIN,
    CONF_SEGMENT_ID,
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    API_BASE_URL,
    API_ENDPOINT,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Telraam from a config entry."""
    segment_id = entry.data[CONF_SEGMENT_ID]
    scan_interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    coordinator = TelraamDataUpdateCoordinator(
        hass,
        segment_id=segment_id,
        scan_interval=scan_interval,
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)


class TelraamDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Telraam data."""

    def __init__(
        self,
        hass: HomeAssistant,
        segment_id: str,
        scan_interval: int,
    ) -> None:
        """Initialize."""
        self.segment_id = segment_id
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=scan_interval),
        )

    async def _async_update_data(self):
        """Fetch data from Telraam API."""
        from datetime import date
        today = date.today().isoformat()
        
        url = f"{API_BASE_URL}/{API_ENDPOINT}/{self.segment_id}/{today}/{today}"
        
        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status != 200:
                            raise UpdateFailed(
                                f"Error fetching data: {response.status}"
                            )
                        data = await response.json()
                        
                        # Extrahiere die aktuellen Werte (letzter Eintrag des Tages)
                        if "data" not in data:
                            raise UpdateFailed("Invalid data format from API")
                        
                        traffic_data = data["data"]
                        result = {}
                        
                        # Verkehrszählungen
                        for key in ["car", "bike", "pedestrian", "heavy", "night"]:
                            if key in traffic_data and traffic_data[key]:
                                # Nimm den letzten (aktuellsten) Wert
                                result[key] = traffic_data[key][-1]
                            else:
                                result[key] = 0
                        
                        # Geschwindigkeitsverteilungen
                        for key in ["speedZero", "speedTen", "speedTwenty", "speedThirty", 
                                    "speedFourty", "speedFifty", "speedSixty", "speedSeventy"]:
                            if key in traffic_data and traffic_data[key]:
                                # Nimm den letzten (aktuellsten) Wert
                                result[key] = traffic_data[key][-1]
                            else:
                                result[key] = 0
                        
                        # Fahrzeugtypen (Mode)
                        for key in ["mode_bicycle", "mode_bus", "mode_car", "mode_lighttruck",
                                    "mode_motorcycle", "mode_pedestrian", "mode_stroller",
                                    "mode_tractor", "mode_trailer", "mode_truck"]:
                            if key in traffic_data and traffic_data[key]:
                                result[key] = traffic_data[key][-1]
                            else:
                                result[key] = 0
                        
                        # Durchschnittswerte
                        for key in ["pedestrianAvg", "bikeAvg", "carAvg", "heavyAvg"]:
                            if key in traffic_data and traffic_data[key]:
                                result[key] = traffic_data[key][-1]
                            else:
                                result[key] = 0
                        
                        # Prozent des typischen Verkehrs
                        for key in ["pedestrianPctOfTypical", "bikePctOfTypical", 
                                    "carPctOfTypical", "heavyPctOfTypical"]:
                            if key in traffic_data and traffic_data[key]:
                                result[key] = traffic_data[key][-1]
                            else:
                                result[key] = 0
                        
                        return result
                        
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
        except Exception as err:
            raise UpdateFailed(f"Unexpected error: {err}")
