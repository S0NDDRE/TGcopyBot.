#!/bin/bash

# Telegram Copy Bot Setup Script for Mac
# This script checks for Python3, installs dependencies, and prepares the project.

echo "Checking for Python3..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install Python3 from https://www.python.org/downloads/"
    echo "After installation, run this script again."
    exit 1
fi

echo "Python3 found. Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully!"
    echo "Next steps:"
    echo "1. Copy .env.example to .env"
    echo "2. Edit .env with your API credentials (API_ID, API_HASH, PHONE, SOURCE_GROUP_ID, CHANNEL_ID)"
    echo "3. Run: python3 tg_copy_bot.py"
    echo "4. Follow the prompts for login."
else
    echo "Failed to install dependencies. Check your internet connection and try again."
    exit 1
fi