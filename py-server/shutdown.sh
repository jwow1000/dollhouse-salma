#!/bin/bash

# Stop Pure Data patch
pkill -f "pd.*main.pd"

# Stop lifx bridge script
pkill -f "venv/bin/python3.*main.py"

# Stop Flask service (started by systemd)
sudo systemctl stop dollhouse-web.service

# Log shutdown
echo "SHUTDOWN SCRIPT TRIGGERED $(date)" >> /home/admin_dollhouse/dollhouse-salma/bridge-script/log.txt

# Shutdown the Pi safely
sudo shutdown -h now
