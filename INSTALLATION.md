# Quick Start Guide - Telraam Home Assistant Integration

## Installation

### Step 1: Install the Integration

**Manual Installation:**
1. Copy the complete folder `custom_components/telraam` to your Home Assistant configuration directory under `config/custom_components/`
2. The structure should look like this:
   ```
   config/
   └── custom_components/
       └── telraam/
           ├── __init__.py
           ├── config_flow.py
           ├── const.py
           ├── manifest.json
           ├── sensor.py
           └── translations/
               ├── de.json
               └── en.json
   ```

### Step 2: Restart Home Assistant

Restart Home Assistant so the integration is recognized.

### Step 3: Add the Integration

1. Open Home Assistant
2. Go to **Settings** → **Devices & Services**
3. Click **+ Add Integration** in the bottom right
4. Search for **"Telraam"**
5. Enter your **Segment ID** (e.g., `9000008606`)
6. Click **Submit**

### Step 4: Done!

The integration automatically creates 4 sensors:
- Telraam Cars (Autos)
- Telraam Bicycles (Fahrräder)
- Telraam Pedestrians (Fußgänger)
- Telraam Heavy Vehicles (Schwere Fahrzeuge)

## Where to Find Your Segment ID?

You can find your Telraam segment ID:
- On https://telraam.net in your dashboard
- In the URL when viewing your statistics
- Example: `9000008606`

## Customize Options

You can adjust the update interval:

1. Go to **Settings** → **Devices & Services**
2. Find **Telraam** in the list
3. Click **Options**
4. Change the interval (60-3600 seconds, default: 300)

## Getting Started After Installation

### Create a Dashboard Card

Add a new card to your dashboard:

```yaml
type: entities
title: Traffic Count Today
entities:
  - sensor.telraam_autos
  - sensor.telraam_fahrrader
  - sensor.telraam_fussganger
  - sensor.telraam_schwere_fahrzeuge
```

### Notification for High Traffic

```yaml
automation:
  - alias: "Traffic Warning"
    trigger:
      platform: numeric_state
      entity_id: sensor.telraam_autos
      above: 1000
    action:
      service: notify.persistent_notification
      data:
        title: "High Traffic"
        message: "Already {{ states('sensor.telraam_autos') }} cars passed by today!"
```

## Problems?

### Sensors Show "Unavailable"
- Wait 5 minutes for the first update
- Check the logs under **Settings** → **System** → **Logs**

### "Integration Not Found"
- Make sure the folder `custom_components/telraam` was created correctly
- Verify the folder structure
- Restart Home Assistant

### "Invalid Segment ID"
- Check if the segment ID is correct (numbers only)
- Test the URL manually: `https://telraam.net/api/measurements-day-barchart/segments/YOUR_ID/2025-12-26/2025-12-26`

## Support

For further questions, please open an issue on GitHub or check the detailed README.md.
