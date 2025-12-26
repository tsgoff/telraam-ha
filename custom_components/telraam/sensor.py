"""Platform for Telraam sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import DOMAIN, SENSOR_TYPES, CONF_SEGMENT_ID


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Telraam sensors based on a config entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    segment_id = config_entry.data[CONF_SEGMENT_ID]

    entities = []
    for sensor_type, sensor_config in SENSOR_TYPES.items():
        entities.append(
            TelraamSensor(
                coordinator,
                segment_id,
                sensor_type,
                sensor_config,
            )
        )

    async_add_entities(entities)


class TelraamSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Telraam Sensor."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        segment_id: str,
        sensor_type: str,
        sensor_config: dict,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._segment_id = segment_id
        self._sensor_type = sensor_type
        self._sensor_config = sensor_config
        
        # Unique ID
        self._attr_unique_id = f"telraam_{segment_id}_{sensor_type}"
        
        # Name
        self._attr_name = f"Telraam {sensor_config['name']}"
        
        # Icon
        self._attr_icon = sensor_config["icon"]
        
        # Unit
        self._attr_native_unit_of_measurement = sensor_config["unit"]
        
        # State class für Statistiken
        self._attr_state_class = SensorStateClass.MEASUREMENT
        
        # Device info für Gruppierung
        self._attr_device_info = {
            "identifiers": {(DOMAIN, segment_id)},
            "name": f"Telraam {segment_id}",
            "manufacturer": "Telraam",
            "model": "Telraam V2",
            "entry_type": "service",
        }

    @property
    def native_value(self) -> int | None:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return None
        
        key = self._sensor_config["key"]
        value = self.coordinator.data.get(key)
        
        if value is None or value == "unbekannt":
            return None
        
        return value

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and self.coordinator.data is not None
