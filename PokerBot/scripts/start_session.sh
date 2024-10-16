#!/bin/bash
# start_session.sh
# Starts a new poker session using the bot

# Define default game parameters
GAME_TYPE="TexasHoldem"
BUY_IN_AMOUNT=50.0

# Allow overriding parameters from command line
if [ ! -z "$1" ]; then
  GAME_TYPE=$1
fi
if [ ! -z "$2" ]; then
  BUY_IN_AMOUNT=$2
fi

echo "Starting poker session with $GAME_TYPE and buy-in of $BUY_IN_AMOUNT..."

# Execute the main bot script with specified parameters
python3 main.py --game_type $GAME_TYPE --buy_in $BUY_IN_AMOUNT
