# click_button.py

"""
This script is responsible for simulating a button click on an online poker platform using Selenium.
It identifies the button by a specified locator (ID, name, class, etc.) and performs the click action.
This is used by PokerAI to interact with the poker platform, such as placing bets or folding hands.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def setup_browser(driver_path, browser="chrome"):
    """
    Sets up the browser driver for Selenium based on the specified browser type.

    Parameters:
    - driver_path: str, Path to the browser driver (e.g., ChromeDriver or GeckoDriver).
    - browser: str, Optional. Specify the browser ("chrome", "firefox"). Defaults to "chrome".
    
    Returns:
    - driver: WebDriver, The Selenium WebDriver instance for the specified browser.
    """
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=driver_path)
    else:
        raise ValueError("Unsupported browser! Use 'chrome' or 'firefox'.")
    
    driver.maximize_window()
    return driver

def click_button(driver, locator_type, locator_value, timeout=10):
    """
    Simulates a button click action on the webpage using Selenium.

    Parameters:
    - driver: WebDriver, The WebDriver instance controlling the browser.
    - locator_type: str, The type of locator (e.g., "id", "name", "class", "xpath").
    - locator_value: str, The value for identifying the button (e.g., button's ID or class).
    - timeout: int, Optional. The time to wait for the element to appear. Default is 10 seconds.
    
    Returns:
    - bool: True if the button was clicked successfully, False if the button was not found or there was an error.
    """
    try:
        # Define how to find the button based on locator type
        if locator_type.lower() == "id":
            button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, locator_value)))
        elif locator_type.lower() == "name":
            button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.NAME, locator_value)))
        elif locator_type.lower() == "class":
            button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, locator_value)))
        elif locator_type.lower() == "xpath":
            button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        else:
            raise ValueError(f"Unsupported locator type '{locator_type}'. Use 'id', 'name', 'class', or 'xpath'.")
        
        # Perform the click action
        button.click()
        print(f"Successfully clicked the button with {locator_type} = '{locator_value}'")
        return True
    except TimeoutException:
        print(f"Timeout: Could not find the button with {locator_type} = '{locator_value}' within {timeout} seconds.")
        return False
    except NoSuchElementException:
        print(f"Error: No element found with {locator_type} = '{locator_value}'")
        return False
    except Exception as e:
        print(f"An error occurred while trying to click the button: {e}")
        return False

def close_browser(driver):
    """
    Closes the browser session and quits the driver.

    Parameters:
    - driver: WebDriver, The WebDriver instance controlling the browser.
    """
    driver.quit()

if __name__ == "__main__":
    # Example usage:
    
    # Path to the ChromeDriver or GeckoDriver
    driver_path = "path/to/chromedriver"
    
    # Setup the browser (Chrome in this case)
    driver = setup_browser(driver_path, browser="chrome")
    
    # Navigate to the poker platform URL
    poker_url = "https://example-poker-platform.com"
    driver.get(poker_url)
    
    # Wait for the page to load and click a button by its ID
    button_clicked = click_button(driver, "id", "bet-button-id", timeout=10)
    
    if button_clicked:
        print("Button click successful!")
    else:
        print("Button click failed.")
    
    # Close the browser session
    close_browser(driver)
