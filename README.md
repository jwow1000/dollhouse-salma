# 💡 LIFX Light Controller with Pure Data + Python on Raspberry Pi

This project connects [Pure Data (Pd)](https://puredata.info/) with [LIFX](https://www.lifx.com/) smart lights using a Python bridge on a Raspberry Pi. It's designed for gallery installations and performance setups where sound or MIDI triggers light behavior over a local network.

## 🛠️ Project Overview

- **Platform**: Raspberry Pi (tested on Pi 4)
- **Audio engine**: Pure Data (Pd) sends OSC messages
- **Bridge**: Python script using [`lifxlan`](https://github.com/mclarkk/lifxlan)
- **Lighting**: WiFi-connected LIFX bulbs with static IPs
- **Service manager**: `systemd` for running everything on boot

## 🧩 Components

```bash
/project-root
├── bridge-script
    ├── main.py   # Python script that receives OSC and controls LIFX lights

├── pd
    ├── main.pd # Pure Data Patch that runs light changes and plays the audio over HIFIberry

├── py-server
    ├── app.py # simple flask server for webpage control
    ├── shutdown.sh # shutdown script
    ├── start.sh # start script

```
