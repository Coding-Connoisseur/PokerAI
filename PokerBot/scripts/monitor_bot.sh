#!/bin/bash
# monitor_bot.sh
# Monitors the bot's performance and restarts it if necessary

# Define log file path and bot start command
LOG_FILE="logs/poker_bot.log"
START_CMD="python3 main.py"

# Function to check bot health
check_bot_health() {
  # Check if the bot is running by looking for its process
  pgrep -f "python3 main.py" > /dev/null
  if [ $? -ne 0 ]; then
    echo "$(date) - Bot is not running. Restarting..." >> $LOG_FILE
    start_bot
  else
    echo "$(date) - Bot is running smoothly." >> $LOG_FILE
  fi
}

# Function to start the bot
start_bot() {
  echo "Starting bot..."
  $START_CMD &
}

# Monitor bot health every 60 seconds
while true; do
  check_bot_health
  sleep 60
done
