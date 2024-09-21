# read_game_state.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the browser driver (Assuming Chrome)
def initialize_browser():
    driver = webdriver.Chrome(executable_path="./drivers/chrome_driver.exe")
    driver.maximize_window()
    return driver

# Function to wait for an element to appear and return it
def wait_for_element(driver, xpath, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        print(f"Timeout: Could not find element {xpath}")
        return None

# Function to read the player's hand cards
def get_player_hand(driver):
    try:
        hand_cards = []
        card_elements = driver.find_elements(By.XPATH, "//div[@class='player-hand-card']")
        for card in card_elements:
            hand_cards.append(card.text.strip())  # Assuming card text is in the inner text
        return hand_cards
    except NoSuchElementException:
        print("Error: Could not find player's hand cards")
        return []

# Function to read the community cards (flop, turn, river)
def get_community_cards(driver):
    try:
        community_cards = []
        card_elements = driver.find_elements(By.XPATH, "//div[@class='community-card']")
        for card in card_elements:
            community_cards.append(card.text.strip())  # Assuming card text is in the inner text
        return community_cards
    except NoSuchElementException:
        print("Error: Could not find community cards")
        return []

# Function to get the current pot size
def get_pot_size(driver):
    try:
        pot_element = wait_for_element(driver, "//div[@class='pot-size']")
        if pot_element:
            pot_size = pot_element.text.strip()
            return pot_size
        else:
            return None
    except NoSuchElementException:
        print("Error: Could not find pot size")
        return None

# Function to read opponent actions
def get_opponent_actions(driver):
    try:
        opponent_actions = {}
        opponent_elements = driver.find_elements(By.XPATH, "//div[@class='opponent-action']")
        for opponent in opponent_elements:
            opponent_name = opponent.get_attribute("data-player-name")  # Assuming there's a data attribute for player name
            opponent_action = opponent.text.strip()
            opponent_actions[opponent_name] = opponent_action
        return opponent_actions
    except NoSuchElementException:
        print("Error: Could not find opponent actions")
        return {}

# Function to scrape the current game state
def read_game_state(driver):
    print("Reading game state...")
    
    player_hand = get_player_hand(driver)
    print(f"Player's Hand: {player_hand}")
    
    community_cards = get_community_cards(driver)
    print(f"Community Cards: {community_cards}")
    
    pot_size = get_pot_size(driver)
    print(f"Pot Size: {pot_size}")
    
    opponent_actions = get_opponent_actions(driver)
    print(f"Opponent Actions: {opponent_actions}")
    
    game_state = {
        "player_hand": player_hand,
        "community_cards": community_cards,
        "pot_size": pot_size,
        "opponent_actions": opponent_actions,
    }
    
    return game_state

# Main function to run the script
def main():
    driver = initialize_browser()
    
    # Navigate to the poker game (replace URL with actual game URL)
    driver.get("https://example-poker-site.com/game")
    
    try:
        while True:
            # Continuously read game state every few seconds
            game_state = read_game_state(driver)
            print("Current Game State:", game_state)
            time.sleep(10)  # Adjust the sleep interval as needed
            
    except KeyboardInterrupt:
        print("Exiting...")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
