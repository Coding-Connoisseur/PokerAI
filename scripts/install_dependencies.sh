#!/bin/bash

# install_dependencies.sh

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

echo "Starting installation of dependencies for PokerAI..."

# Update package lists for system libraries (for Ubuntu/Debian-based systems)
echo "Updating system packages..."
sudo apt-get update -y

# Install Python 3 and pip (if not already installed)
if command_exists python3; then
    echo "Python 3 is already installed."
else
    echo "Installing Python 3..."
    sudo apt-get install python3 -y
fi

if command_exists pip3; then
    echo "Pip3 is already installed."
else
    echo "Installing Pip3..."
    sudo apt-get install python3-pip -y
fi

# Install virtualenv to manage project dependencies
if command_exists virtualenv; then
    echo "Virtualenv is already installed."
else
    echo "Installing virtualenv..."
    pip3 install virtualenv
fi

# Create a virtual environment
echo "Creating virtual environment..."
virtualenv venv
source venv/bin/activate

# Install Python packages from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing Python dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found."
    exit 1
fi

# Install Selenium and browser drivers (e.g., ChromeDriver)
echo "Installing Selenium..."
pip install selenium

# Check if ChromeDriver is installed
if [ ! -f "./drivers/chromedriver" ]; then
    echo "Downloading ChromeDriver..."
    CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+')
    wget -N https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip -P ./drivers/
    unzip ./drivers/chromedriver_linux64.zip -d ./drivers/
    rm ./drivers/chromedriver_linux64.zip
    chmod +x ./drivers/chromedriver
else
    echo "ChromeDriver is already installed."
fi

# Ensure other drivers (e.g., GeckoDriver for Firefox) can be added similarly

# Final message
echo "All dependencies have been installed successfully!"
