#!/bin/bash

# Start in bridge script directory (Python lifx bridge)
cd /home/admin_dollhouse/dollhouse-salma/bridge-script || exit 1

# Start the lifx bridge
venv/bin/python3 main.py &

# Start the Pure Data patch
cd /home/admin_dollhouse/dollhouse-salma/pd || exit 1
pd -nogui -noadc -alsa -audiooutdev 4 main.pd &

# Log
echo "START SCRIPT TRIGGERED DOLL $(date)" >> /home/admin_dollhouse/dollhouse-salma/bridge-script/log.txt
