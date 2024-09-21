# setup_environment.py

import os
import shutil
import yaml
import subprocess

# Paths to important directories
CONFIG_DIR = "./config"
DATA_DIR = "./data"
LOG_DIR = "./logs"
MODELS_DIR = "./models"
DRIVERS_DIR = "./drivers"

# Path to environment configuration file
ENV_CONFIG_FILE = os.path.join(CONFIG_DIR, "env_config.yaml")


def create_directories():
    """
    Create necessary directories for data storage, logs, and models.
    """
    for directory in [DATA_DIR, LOG_DIR, MODELS_DIR, DRIVERS_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")


def check_browser_drivers():
    """
    Ensure that the required browser drivers (e.g., ChromeDriver, GeckoDriver) are present in the drivers directory.
    If drivers are missing, guide the user to install them.
    """
    chrome_driver = os.path.join(DRIVERS_DIR, "chrome_driver.exe")
    firefox_driver = os.path.join(DRIVERS_DIR, "firefox_driver.exe")

    if not os.path.exists(chrome_driver):
        print(f"ChromeDriver not found at {chrome_driver}. Please download it from https://sites.google.com/a/chromium.org/chromedriver/downloads")
    else:
        print("ChromeDriver is present.")

    if not os.path.exists(firefox_driver):
        print(f"GeckoDriver (Firefox) not found at {firefox_driver}. Please download it from https://github.com/mozilla/geckodriver/releases")
    else:
        print("GeckoDriver (Firefox) is present.")


def load_environment_config():
    """
    Load environment configuration from YAML file (env_config.yaml).
    """
    if os.path.exists(ENV_CONFIG_FILE):
        with open(ENV_CONFIG_FILE, 'r') as file:
            config = yaml.safe_load(file)
            print("Environment configuration loaded.")
            return config
    else:
        print(f"Error: {ENV_CONFIG_FILE} not found.")
        return None


def setup_python_environment():
    """
    Ensures the Python environment is set up by installing dependencies via `requirements.txt`.
    """
    print("Installing Python dependencies from requirements.txt...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    print("Dependencies installed successfully.")


def initialize_data_files():
    """
    Copy or initialize necessary data files and datasets.
    For example, you can seed opponent profiles or game logs.
    """
    sample_data_file = os.path.join(DATA_DIR, "sample_data.json")
    
    if not os.path.exists(sample_data_file):
        # Create a sample data file if none exists
        with open(sample_data_file, 'w') as f:
            f.write("{}")
        print(f"Sample data file created: {sample_data_file}")
    else:
        print(f"Sample data file already exists: {sample_data_file}")


def configure_logging():
    """
    Ensure that logging configurations are set up properly.
    Create a default log file or folder if necessary.
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        print(f"Created log directory: {LOG_DIR}")

    log_file = os.path.join(LOG_DIR, "poker_ai.log")
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write("Poker AI log initialized.\n")
        print(f"Log file created: {log_file}")
    else:
        print(f"Log file already exists: {log_file}")


def setup_environment():
    """
    The main function that ties together the environment setup steps.
    """
    print("Setting up PokerAI environment...")
    create_directories()
    check_browser_drivers()
    config = load_environment_config()
    setup_python_environment()
    initialize_data_files()
    configure_logging()
    print("Environment setup complete.")


if __name__ == "__main__":
    setup_environment()
