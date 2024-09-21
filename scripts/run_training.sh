#!/bin/bash

# Script to run reinforcement learning (RL) agent training for PokerAI

# Set the environment variables if needed
echo "Setting up environment..."
source ./venv/bin/activate  # Activate virtual environment (if applicable)

# Path to RL module configuration file
RL_CONFIG="./config/rl_config.yaml"

# Check if config file exists
if [[ ! -f $RL_CONFIG ]]; then
    echo "Error: RL configuration file ($RL_CONFIG) not found!"
    exit 1
fi

# Display training configuration
echo "Training configuration:"
cat $RL_CONFIG

# Start training
echo "Starting RL agent training..."
python3 rl_module/train_agent.py --config $RL_CONFIG

# Monitor training progress (logs or terminal output)
LOG_FILE="./logs/training_log.txt"
if [[ -f $LOG_FILE ]]; then
    echo "Monitoring training progress via log file ($LOG_FILE)..."
    tail -f $LOG_FILE
else
    echo "Training started, but log file not found. Check terminal output."
fi

# Completion message
echo "Training script completed."
