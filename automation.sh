#!/bin/bash

# Navigate to your project directory
#cd /path/to/your/project

# Activate your virtual environment if needed
# source /path/to/venv/bin/activate

# Log file location
LOG_FILE="automation.log"

# Execute your Python script for weather data
echo "Fetching weather data..." >> $LOG_FILE
python3 main.py --weather >> $LOG_FILE 2>&1
echo "Weather data fetched successfully!" >> $LOG_FILE

# Execute your Python script for flight data
echo "Fetching flight data..." >> $LOG_FILE
python3 main.py --flights >> $LOG_FILE 2>&1
echo "Flight data fetched successfully!" >> $LOG_FILE

# Send a desktop notification (optional, for Linux)
notify-send "Automation Complete" "Weather and Flight data fetching completed."

# Optionally, send an email notification if required
