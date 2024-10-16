#!/bin/bash
# deploy_bot.sh
# Deploys the poker bot to a remote server

# Define variables for server connection
SERVER_USER="username"
SERVER_HOST="your.server.com"
SERVER_PATH="/path/to/deploy"

# Define local paths
LOCAL_PATH="path/to/your/bot"

echo "Starting deployment..."

# Upload bot files to the server
scp -r $LOCAL_PATH $SERVER_USER@$SERVER_HOST:$SERVER_PATH

# Log in to the server and start the bot setup
ssh $SERVER_USER@$SERVER_HOST << EOF
  cd $SERVER_PATH
  echo "Installing dependencies..."
  pip install -r requirements.txt
  echo "Starting bot..."
  python3 main.py
EOF

echo "Deployment complete."
