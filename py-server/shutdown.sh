#!/bin/bash

# Log start of shutdown
echo "SHUTDOWN SCRIPT TRIGGERED $(date)" >> /home/admin_dollhouse/dollhouse-salma/bridge-script/log.txt

# Stop Pure Data patch
pkill -f "pd.*main.pd"

# Stop lifx bridge script
pkill -f "venv/bin/python3.*main.py"

# Stop Flask service
sudo systemctl stop dollhouse-web.service

# Wait briefly to let processes terminate cleanly
sleep 2

# Shutdown the Pi safely
sudo shutdown -h now
