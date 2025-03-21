#!/bin/bash

# Remove any old version and re-clone
rm -rf relo_local
git clone https://github.com/ldott/relo.git relo_local

# Start the bot
exec python3 main.py