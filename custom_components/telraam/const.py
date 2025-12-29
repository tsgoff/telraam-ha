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
    },
    "night": {
        "name": "Nachtverkehr",
        "unit": "Fahrzeuge",
        "icon": "mdi:weather-night",
        "key": "night"
    },
    "speed_zero": {
        "name": "Geschwindigkeit 0-10 km/h",
        "unit": "%",
        "icon": "mdi:speedometer-slow",
        "key": "speedZero"
    },
    "speed_ten": {
        "name": "Geschwindigkeit 10-20 km/h",
        "unit": "%",
        "icon": "mdi:speedometer",
        "key": "speedTen"
    },
    "speed_twenty": {
        "name": "Geschwindigkeit 20-30 km/h",
        "unit": "%",
        "icon": "mdi:speedometer",
        "key": "speedTwenty"
    },
    "speed_thirty": {
        "name": "Geschwindigkeit 30-40 km/h",
        "unit": "%",
        "icon": "mdi:speedometer",
        "key": "speedThirty"
    },
    "speed_fourty": {
        "name": "Geschwindigkeit 40-50 km/h",
        "unit": "%",
        "icon": "mdi:speedometer",
        "key": "speedFourty"
    },
    "speed_fifty": {
        "name": "Geschwindigkeit 50-60 km/h",
        "unit": "%",
        "icon": "mdi:speedometer",
        "key": "speedFifty"
    },
    "speed_sixty": {
        "name": "Geschwindigkeit 60-70 km/h",
        "unit": "%",
        "icon": "mdi:speedometer-medium",
        "key": "speedSixty"
    },
    "speed_seventy": {
        "name": "Geschwindigkeit >70 km/h",
        "unit": "%",
        "icon": "mdi:speedometer",
        "key": "speedSeventy"
    },
    # Fahrzeugtypen (Mode)
    "mode_bicycle": {
        "name": "Fahrräder (Modus)",
        "unit": "Fahrzeuge",
        "icon": "mdi:bike",
        "key": "mode_bicycle"
    },
    "mode_bus": {
        "name": "Busse",
        "unit": "Fahrzeuge",
        "icon": "mdi:bus",
        "key": "mode_bus"
    },
    "mode_car": {
        "name": "PKW (Modus)",
        "unit": "Fahrzeuge",
        "icon": "mdi:car",
        "key": "mode_car"
    },
    "mode_lighttruck": {
        "name": "Leichte LKW",
        "unit": "Fahrzeuge",
        "icon": "mdi:truck-delivery",
        "key": "mode_lighttruck"
    },
    "mode_motorcycle": {
        "name": "Motorräder",
        "unit": "Fahrzeuge",
        "icon": "mdi:motorbike",
        "key": "mode_motorcycle"
    },
    "mode_pedestrian": {
        "name": "Fußgänger (Modus)",
        "unit": "Personen",
        "icon": "mdi:walk",
        "key": "mode_pedestrian"
    },
    "mode_stroller": {
        "name": "Kinderwagen",
        "unit": "Fahrzeuge",
        "icon": "mdi:baby-carriage",
        "key": "mode_stroller"
    },
    "mode_tractor": {
        "name": "Traktoren",
        "unit": "Fahrzeuge",
        "icon": "mdi:tractor",
        "key": "mode_tractor"
    },
    "mode_trailer": {
        "name": "Anhänger",
        "unit": "Fahrzeuge",
        "icon": "mdi:truck-trailer",
        "key": "mode_trailer"
    },
    "mode_truck": {
        "name": "LKW",
        "unit": "Fahrzeuge",
        "icon": "mdi:truck",
        "key": "mode_truck"
    },
    # Durchschnittswerte
    "pedestrian_avg": {
        "name": "Fußgänger Durchschnitt",
        "unit": "Personen",
        "icon": "mdi:walk",
        "key": "pedestrianAvg"
    },
    "bike_avg": {
        "name": "Fahrräder Durchschnitt",
        "unit": "Fahrräder",
        "icon": "mdi:bike",
        "key": "bikeAvg"
    },
    "car_avg": {
        "name": "Autos Durchschnitt",
        "unit": "Fahrzeuge",
        "icon": "mdi:car",
        "key": "carAvg"
    },
    "heavy_avg": {
        "name": "Schwere Fahrzeuge Durchschnitt",
        "unit": "Fahrzeuge",
        "icon": "mdi:truck",
        "key": "heavyAvg"
    },
    # Prozent des typischen Verkehrs
    "pedestrian_pct": {
        "name": "Fußgänger % vom Durchschnitt",
        "unit": "%",
        "icon": "mdi:walk",
        "key": "pedestrianPctOfTypical"
    },
    "bike_pct": {
        "name": "Fahrräder % vom Durchschnitt",
        "unit": "%",
        "icon": "mdi:bike",
        "key": "bikePctOfTypical"
    },
    "car_pct": {
        "name": "Autos % vom Durchschnitt",
        "unit": "%",
        "icon": "mdi:car",
        "key": "carPctOfTypical"
    },
    "heavy_pct": {
        "name": "Schwere Fahrzeuge % vom Durchschnitt",
        "unit": "%",
        "icon": "mdi:truck",
        "key": "heavyPctOfTypical"
    }
}
