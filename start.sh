#!/bin/bash

echo "Starting the Super Advanced Telegram Music Bot..."

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Install dependencies
pip3 install -r requirements.txt

# Start the bot
python3 main.py