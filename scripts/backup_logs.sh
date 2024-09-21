#!/bin/bash

# Directory where logs are stored
LOG_DIR="./logs"

# Directory to store backups
BACKUP_DIR="./backup_logs"

# Get the current timestamp for the backup folder name
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create a new backup directory with the current timestamp
NEW_BACKUP_DIR="$BACKUP_DIR/logs_backup_$TIMESTAMP"
mkdir -p "$NEW_BACKUP_DIR"

# Check if the log directory exists and has logs
if [ -d "$LOG_DIR" ]; then
  # Copy all log files to the backup directory
  cp -r "$LOG_DIR/"* "$NEW_BACKUP_DIR/"

  echo "Logs have been backed up to $NEW_BACKUP_DIR"

  # Optionally, you can compress the backup folder to save space
  tar -czf "$NEW_BACKUP_DIR.tar.gz" -C "$BACKUP_DIR" "logs_backup_$TIMESTAMP"
  echo "Logs compressed to $NEW_BACKUP_DIR.tar.gz"

else
  echo "No logs found to backup in $LOG_DIR"
fi
