#!/bin/bash

# Move to the project directory
cd /home/admin_dollhouse/dollhouse-salma || {
  echo "Failed to change directory to /home/admin_dollhouse/dollhouse-salma"
  exit 1
}

# Run git pull and log output
echo "Running git pull..."
if git pull; then
  echo "Git pull successful."
else
  echo "Git pull failed."
  exit 1
fi

exit 0
