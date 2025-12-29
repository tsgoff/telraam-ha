# Telraam Home Assistant Integration

This custom integration allows you to integrate Telraam V2 traffic counter data directly into Home Assistant.

## Features

- ✅ Easy setup through Home Assistant UI
- ✅ Automatic detection and validation of segment ID
- ✅ 37 sensors per Telraam device:
  - 🚗 5 basic traffic counts (cars, bikes, pedestrians, heavy vehicles, night traffic)
  - 📊 8 speed distribution sensors (0-10, 10-20, 20-30, 30-40, 40-50, 50-60, 60-70, >70 km/h)
  - 🚦 10 detailed vehicle type sensors (bicycle, bus, car, light truck, motorcycle, pedestrian, stroller, tractor, trailer, truck)
  - 📈 4 average traffic sensors
  - 📊 4 typical traffic percentage sensors
- ✅ Customizable update interval (default: 5 minutes)
- ✅ Support for long-term statistics
- ✅ Multilingual (German & English)

## Installation

### HACS (recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right and select "Custom repositories"
4. Add this repository URL: `https://github.com/tsgoff/telraam-ha`
5. Category: "Integration"
6. Click "Add"
7. Search for "Telraam" and install it
8. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/telraam` folder to your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant

## Configuration

### Via UI (recommended)

1. Go to "Settings" → "Devices & Services"
2. Click "+ Add Integration"
3. Search for "Telraam"
4. Enter your Telraam segment ID (e.g., `9000008606`)
5. The integration will automatically create 4 sensors

### Finding Your Segment ID

You can find your Telraam segment ID:
- In your Telraam dashboard on the website
- In the URL when viewing your Telraam statistics
- The ID is a number like `9000008606`

### Customizing Options

1. Go to "Settings" → "Devices & Services"
2. Find your Telraam integration
3. Click "Options"
4. Adjust the update interval (60-3600 seconds)

## Usage

After installation, the following sensors will be available:

**Basic Traffic Count Sensors:**
- `sensor.telraam_autos` - Number of cars today
- `sensor.telraam_fahrrader` - Number of bicycles today
- `sensor.telraam_fussganger` - Number of pedestrians today
- `sensor.telraam_schwere_fahrzeuge` - Number of heavy vehicles today
- `sensor.telraam_nachtverkehr` - Number of vehicles at night

**Speed Distribution Sensors (in %):**
- `sensor.telraam_geschwindigkeit_0_10_km_h` - Traffic 0-10 km/h
- `sensor.telraam_geschwindigkeit_10_20_km_h` - Traffic 10-20 km/h
- `sensor.telraam_geschwindigkeit_20_30_km_h` - Traffic 20-30 km/h
- `sensor.telraam_geschwindigkeit_30_40_km_h` - Traffic 30-40 km/h
- `sensor.telraam_geschwindigkeit_40_50_km_h` - Traffic 40-50 km/h
- `sensor.telraam_geschwindigkeit_50_60_km_h` - Traffic 50-60 km/h
- `sensor.telraam_geschwindigkeit_60_70_km_h` - Traffic 60-70 km/h
- `sensor.telraam_geschwindigkeit_70_km_h` - Traffic >70 km/h

**Detailed Vehicle Type Sensors:**
- `sensor.telraam_fahrrader_modus` - Bicycles (mode detection)
- `sensor.telraam_busse` - Buses
- `sensor.telraam_pkw_modus` - Cars (mode detection)
- `sensor.telraam_leichte_lkw` - Light trucks
- `sensor.telraam_motorrader` - Motorcycles
- `sensor.telraam_fussganger_modus` - Pedestrians (mode detection)
- `sensor.telraam_kinderwagen` - Strollers
- `sensor.telraam_traktoren` - Tractors
- `sensor.telraam_anhanger` - Trailers
- `sensor.telraam_lkw` - Trucks

**Average Traffic Sensors:**
- `sensor.telraam_fussganger_durchschnitt` - Pedestrians average
- `sensor.telraam_fahrrader_durchschnitt` - Bicycles average
- `sensor.telraam_autos_durchschnitt` - Cars average
- `sensor.telraam_schwere_fahrzeuge_durchschnitt` - Heavy vehicles average

**Typical Traffic Percentage Sensors:**
- `sensor.telraam_fussganger_vom_durchschnitt` - Pedestrians % of typical
- `sensor.telraam_fahrrader_vom_durchschnitt` - Bicycles % of typical
- `sensor.telraam_autos_vom_durchschnitt` - Cars % of typical
- `sensor.telraam_schwere_fahrzeuge_vom_durchschnitt` - Heavy vehicles % of typical

### Example Automation

```yaml
automation:
  - alias: "High traffic notification"
    trigger:
      - platform: numeric_state
        entity_id: sensor.telraam_autos
        above: 1000
    action:
      - service: notify.mobile_app
        data:
          title: "High Traffic"
          message: "Already {{ states('sensor.telraam_autos') }} cars passed by today!"
```

### Example Lovelace Card

```yaml
type: entities
title: Traffic Count
entities:
  - entity: sensor.telraam_autos
    icon: mdi:car
  - entity: sensor.telraam_fahrrader
    icon: mdi:bike
  - entity: sensor.telraam_fussganger
    icon: mdi:walk
  - entity: sensor.telraam_schwere_fahrzeuge
    icon: mdi:truck
```

### Statistics Card

Since the sensors use `SensorStateClass.MEASUREMENT`, you can use long-term statistics:

```yaml
type: statistics-graph
entities:
  - sensor.telraam_autos
  - sensor.telraam_fahrrader
stat_types:
  - sum
  - mean
period: week
```

## Technical Details

### API

The integration uses the official Telraam API:
- Endpoint: `https://telraam.net/api/measurements-day-barchart/segments/{segment_id}/{date}/{date}`
- Method: GET
- No authentication required
- Data is retrieved for the current day

### Updates

- Default interval: 5 minutes (300 seconds)
- Configurable: 60 to 3600 seconds
- The integration always shows the last available value of the current day

### Error Handling

- Automatic retry on network errors
- Sensors show "Unavailable" on API issues
- Segment ID validation during setup

## Troubleshooting

### Sensors Show "Unknown"

- Check if your Telraam has sent data today
- Wait for the next update
- Check Home Assistant logs for errors

### "Invalid Segment ID" Error

- Make sure you're using the correct segment ID
- The ID should only contain numbers (e.g., `9000008606`)
- Verify the ID on the Telraam website

### API Connection Error

- Check your internet connection
- Ensure Home Assistant can access `telraam.net`
- Check if the Telraam API is available

### View Logs

To see detailed logs, add this to your `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.telraam: debug
```

## Support

For issues or questions:
- Open an issue on GitHub: https://github.com/tsgoff/telraam-ha/issues
- Describe the problem in detail
- Include relevant logs

## License

MIT License

## Credits

- Developed for the Telraam community
- Telraam API: https://telraam.net/
- Home Assistant: https://www.home-assistant.io/

## Changelog

### Version 1.0.0
- Initial release
- Support for all traffic types (cars, bikes, pedestrians, heavy vehicles, night traffic)
- Speed distribution sensors (8 speed ranges)
- Detailed vehicle type detection (10 types: bicycle, bus, car, light truck, motorcycle, pedestrian, stroller, tractor, trailer, truck)
- Average traffic sensors (4 types)
- Typical traffic percentage sensors (4 types)
- Config Flow integration
- German and English translations
- Total: 37 sensors
