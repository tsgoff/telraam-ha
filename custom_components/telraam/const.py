"""Constants for the Telraam integration."""

DOMAIN = "telraam"
CONF_SEGMENT_ID = "segment_id"
CONF_SCAN_INTERVAL = "scan_interval"

DEFAULT_SCAN_INTERVAL = 300  # 5 Minuten

# API
API_BASE_URL = "https://telraam.net/api"
API_ENDPOINT = "measurements-day-barchart/segments"

# Sensor Types
SENSOR_TYPES = {
    "car": {
        "name": "Autos",
        "unit": "Fahrzeuge",
        "icon": "mdi:car",
        "key": "car"
    },
    "bike": {
        "name": "Fahrräder",
        "unit": "Fahrräder",
        "icon": "mdi:bike",
        "key": "bike"
    },
    "pedestrian": {
        "name": "Fußgänger",
        "unit": "Personen",
        "icon": "mdi:walk",
        "key": "pedestrian"
    },
    "heavy": {
        "name": "Schwere Fahrzeuge",
        "unit": "Fahrzeuge",
        "icon": "mdi:truck",
        "key": "heavy"
    }
}
