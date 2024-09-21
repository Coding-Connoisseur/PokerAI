# place_bet.py
"""
This script is responsible for automating the process of placing a bet on the poker platform. It uses Selenium 
to interact with the web elements, simulating a user placing a bet based on the AI's decision-making process.
The AI's decision (bet, raise, fold) is assumed to be provided by the strategy engine.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import yaml

# Load browser automation configurations from config file
def load_config():
    """Load browser automation configurations such as timeout and retries."""
    with open('../config/browser_automation_config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_ai_decision():
    """
    Simulate the AI decision-making process. This is a placeholder function where, in a real-world scenario,
    you'd connect to the strategy engine to get the decision (bet, fold, check, raise, etc.).
    """
    # Example decisions could be 'bet', 'fold', 'raise', etc. This is mocked for now.
    return "bet", 100  # (action, amount)

def wait_for_game_state(driver, config):
    """
    Wait for the game state to be loaded (e.g., player's turn to act).
    This ensures the system only tries to place a bet when the game is ready.
    """
    try:
        # Wait until the element indicating it's the player's turn is visible (e.g., a 'Your Turn' button)
        WebDriverWait(driver, config['timeout']).until(
            EC.visibility_of_element_located((By.ID, "your-turn-indicator"))
        )
        print("Detected player's turn.")
        return True
    except Exception as e:
        print(f"Error: Game state could not be detected. {e}")
        return False

def place_bet(driver, amount, config):
    """
    Place a bet by interacting with the web elements on the poker platform.
    The bet size is determined by the AI, and the driver sends the interaction to the page.
    """
    try:
        # Wait for the bet amount field to become clickable
        bet_input = WebDriverWait(driver, config['timeout']).until(
            EC.element_to_be_clickable((By.ID, "bet-amount-input"))
        )
        bet_input.clear()
        bet_input.send_keys(str(amount))  # Input the bet amount
        
        # Find and click the 'Bet' button
        bet_button = WebDriverWait(driver, config['timeout']).until(
            EC.element_to_be_clickable((By.ID, "bet-button"))
        )
        bet_button.click()
        print(f"Placed a bet of {amount}.")
        return True
    except Exception as e:
        print(f"Error while placing the bet: {e}")
        return False

def fold_hand(driver, config):
    """
    Fold the hand by clicking the 'Fold' button.
    """
    try:
        fold_button = WebDriverWait(driver, config['timeout']).until(
            EC.element_to_be_clickable((By.ID, "fold-button"))
        )
        fold_button.click()
        print("Folded the hand.")
        return True
    except Exception as e:
        print(f"Error while folding: {e}")
        return False

def raise_bet(driver, amount, config):
    """
    Raise the bet amount. Similar to the place_bet function but specifically for raises.
    """
    try:
        raise_input = WebDriverWait(driver, config['timeout']).until(
            EC.element_to_be_clickable((By.ID, "raise-amount-input"))
        )
        raise_input.clear()
        raise_input.send_keys(str(amount))  # Input the raise amount

        raise_button = WebDriverWait(driver, config['timeout']).until(
            EC.element_to_be_clickable((By.ID, "raise-button"))
        )
        raise_button.click()
        print(f"Raised the bet to {amount}.")
        return True
    except Exception as e:
        print(f"Error while raising the bet: {e}")
        return False

def execute_action(driver, action, amount, config):
    """
    Execute the AI's action (bet, fold, raise) based on the decision provided by the strategy engine.
    """
    if action == "bet":
        return place_bet(driver, amount, config)
    elif action == "fold":
        return fold_hand(driver, config)
    elif action == "raise":
        return raise_bet(driver, amount, config)
    else:
        print(f"Unknown action: {action}")
        return False

def main():
    """
    Main function to run the script. It initializes the web driver, waits for the player's turn, retrieves
    the AI's decision, and executes the corresponding action on the poker platform.
    """
    config = load_config()

    # Initialize WebDriver (assuming ChromeDriver is used here)
    driver = webdriver.Chrome(executable_path=config['chrome_driver_path'])
    driver.get(config['poker_url'])  # Navigate to the poker platform

    # Wait for the game state to be ready
    if wait_for_game_state(driver, config):
        # Retrieve AI's decision from the strategy engine
        action, amount = get_ai_decision()

        # Execute the AI's action
        if not execute_action(driver, action, amount, config):
            print("Failed to execute the action. Retrying...")
        else:
            print(f"Action {action} of amount {amount} executed successfully.")
    else:
        print("Game state not ready, exiting.")

    # Clean up and close the driver
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()
