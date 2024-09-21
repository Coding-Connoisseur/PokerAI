# enter_game.py
"""
This script automates the process of entering a poker game on a live poker platform using Selenium.
It includes logic for navigating to the game, selecting the correct table, and ensuring that the AI
is seated and ready to play.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuration settings
POKER_URL = "https://www.example-poker-site.com"
LOGIN_URL = POKER_URL + "/login"
USERNAME = "your_username"
PASSWORD = "your_password"
GAME_LOBBY_URL = POKER_URL + "/game-lobby"
TABLE_NAME = "High Stakes Table"  # Example table name; adjust accordingly
BROWSER_DRIVER_PATH = "./drivers/chrome_driver.exe"  # Ensure this path is correct

# Initialize the browser driver
def init_browser():
    """
    Initializes the Selenium WebDriver with the appropriate configurations.
    """
    driver = webdriver.Chrome(executable_path=BROWSER_DRIVER_PATH)
    driver.maximize_window()
    return driver

# Login function
def login(driver):
    """
    Logs into the poker site using stored credentials.
    """
    driver.get(LOGIN_URL)
    try:
        # Wait for login form to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        
        # Enter login credentials
        driver.find_element(By.NAME, "username").send_keys(USERNAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        
        # Wait for login to complete
        WebDriverWait(driver, 10).until(EC.url_changes(LOGIN_URL))
        print("Logged in successfully.")
    except TimeoutException:
        print("Login process timed out.")
        driver.quit()
        raise

# Navigate to game lobby
def navigate_to_lobby(driver):
    """
    Navigates to the game lobby where poker tables are listed.
    """
    try:
        driver.get(GAME_LOBBY_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "game-table-list")))
        print("Navigated to game lobby.")
    except TimeoutException:
        print("Failed to load the game lobby.")
        driver.quit()
        raise

# Select and join a poker table
def select_table(driver, table_name):
    """
    Selects a poker table by its name and joins the game.
    """
    try:
        # Look for the table by name
        tables = driver.find_elements(By.CLASS_NAME, "table-name")
        for table in tables:
            if table.text == table_name:
                table.click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "game-screen")))
                print(f"Joined table: {table_name}")
                return True
        print(f"Table {table_name} not found.")
        return False
    except NoSuchElementException:
        print(f"Table {table_name} not found.")
        return False
    except TimeoutException:
        print("Failed to join the game.")
        return False

# Ready up for the game
def ready_up(driver):
    """
    Ensures the AI is seated at the table and ready to play.
    """
    try:
        ready_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "readyButton")))
        ready_button.click()
        print("AI is ready to play.")
    except (TimeoutException, NoSuchElementException):
        print("Failed to ready up for the game.")
        driver.quit()
        raise

# Main function to execute the automation
def main():
    """
    Main function to run the entire process of logging in, navigating to the game lobby,
    selecting a poker table, and preparing the AI to play.
    """
    driver = init_browser()
    try:
        login(driver)
        navigate_to_lobby(driver)
        if select_table(driver, TABLE_NAME):
            ready_up(driver)
        else:
            print("Exiting due to table not found.")
            driver.quit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        driver.quit()
    finally:
        time.sleep(3)  # Pause for a short while before closing
        driver.quit()

if __name__ == "__main__":
    main()
