#!/bin/bash

# Stop Pure Data patch
pkill -f "pd.*main.pd"

# Stop lifx bridge script
pkill -f "venv/bin/python3.*main.py"