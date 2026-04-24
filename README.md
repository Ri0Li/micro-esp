# Micro-ESP

Bridge a micro:bit display and buttons to Home Assistant through an ESP32-C3 running ESPHome.

## What It Does

- Sends commands from ESPHome to micro:bit over UART:
  - draw/clear pixels on the 5x5 LED matrix
  - show numbers
  - scroll text
  - trigger a simple connection test icon
- Reports micro:bit button A/B state back to ESPHome as binary sensors.
- Exposes an ESPHome API service to send raw command strings from Home Assistant automations/scripts.

## Wiring

- ESP32 `GPIO21` (TX) -> micro:bit `P1`
- ESP32 `GPIO20` (RX) -> micro:bit `P0`
- GND -> GND

## Setup

### 1) Configure secrets

Create/update your ESPHome secrets file with Wi-Fi credentials.

#### secrets.yaml:

```
yaml
wifi_ssid: "your-ssid"
wifi_password: "your-password"
```

Change fallback AP password in micro-esp.yaml.

#### micro-esp.yaml:

```
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  fast_connect: true 
  power_save_mode: none
  ap:
    ssid: "micro-esp"
    password: "CHANGE_ME"
```

### 2) Flash micro:bit code

Flash `main.py` to your micro:bit using [Makecode](https://makecode.microbit.org/).

### 3) Flash ESPHome firmware

Use `micro-esp.yaml` in ESPHome to install onto the ESP32-C3.

## Command Protocol

All commands are newline-terminated (`\n`).

- `PX:x,y,v`  
  Set pixel `(x,y)` where `v=1` plots and `v=0` unplots.

- `CLR`  
  Clear the display.

- `DISP:n`  
  Show number/text via `show_string`.

- `MSG:text`  
  Scroll text.

- `INC`  
  Show a YES icon (used as a quick UART test).

## Using the YAML Builder

Use [mirocesp.rioli.app](https://mirocesp.rioli.app) to generate Home Assistant action YAML:
- Draw pixels on a 5x5 grid
- Toggle between single command and sequence mode
- Generate `MSG:` and `DISP:` payloads
- Copy YAML to clipboard
