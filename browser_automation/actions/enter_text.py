# enter_text.py

"""
This script automates the action of entering text into a specific web element on a poker website.
It uses Selenium to interact with the browser and the HTML DOM, finding the input element by various locators
and entering the provided text into it.

This can be used for sending messages in the chatbox during gameplay or for entering text into any input field.

Dependencies:
    - selenium
    - WebDriver (ChromeDriver, GeckoDriver, etc.) must be available in the browser_automation/drivers directory.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Configuration parameters
TIMEOUT = 10  # Maximum wait time for elements to become interactable

def initialize_driver(browser="chrome"):
    """
    Initializes the Selenium WebDriver based on the specified browser.
    
    Args:
        browser (str): The browser to use for automation (default is Chrome).
    
    Returns:
        driver (WebDriver): The initialized WebDriver instance.
    """
    driver_path = f"../drivers/{browser}_driver"
    
    if browser.lower() == "chrome":
        driver_path += ".exe"
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser.lower() == "firefox":
        driver_path += ".exe"
        driver = webdriver.Firefox(executable_path=driver_path)
    else:
        raise ValueError("Unsupported browser. Please use 'chrome' or 'firefox'.")
    
    return driver

def enter_text(driver, url, locator_type, locator_value, text_to_enter):
    """
    Automates entering text into a specified web element.

    Args:
        driver (WebDriver): The initialized Selenium WebDriver instance.
        url (str): The URL of the page where the input element is located.
        locator_type (str): The method to locate the element (e.g., 'id', 'name', 'css_selector', 'xpath').
        locator_value (str): The value used for locating the input element.
        text_to_enter (str): The text to be entered into the input field.
    
    Returns:
        bool: True if the text was successfully entered, False if any error occurred.
    """
    try:
        # Navigate to the page
        driver.get(url)
        print(f"Navigating to {url}...")

        # Wait for the element to be located and become interactable
        print(f"Waiting for element '{locator_value}' using {locator_type}...")
        element = WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable((getattr(By, locator_type.upper()), locator_value))
        )

        # Clear the existing text (if any) and enter the new text
        print(f"Clearing existing text in the field...")
        element.clear()

        print(f"Entering text: {text_to_enter}")
        element.send_keys(text_to_enter)
        
        # Optionally submit or press Enter if required
        # element.send_keys(Keys.RETURN)
        
        print("Text entry successful.")
        return True

    except TimeoutException:
        print(f"Error: Element '{locator_value}' not found within the timeout period.")
        return False
    except NoSuchElementException:
        print(f"Error: Unable to locate the element '{locator_value}'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

def main():
    """
    Main function to demonstrate the usage of the enter_text functionality.
    Modify the URL, locator type, locator value, and text as needed.
    """
    # Initialize the WebDriver (use Chrome by default)
    driver = initialize_driver("chrome")
    
    # Define the target page and input field
    url = "https://example.com/poker"
    locator_type = "id"  # Could be 'name', 'xpath', 'css_selector', etc.
    locator_value = "chat_input"  # Replace with the actual locator for the input field
    text_to_enter = "Hello, Poker World!"  # Replace with the text you want to enter
    
    # Call the enter_text function
    success = enter_text(driver, url, locator_type, locator_value, text_to_enter)
    
    # Pause for observation and close the browser
    if success:
        print("Waiting for 5 seconds before closing the browser...")
        time.sleep(5)
    
    driver.quit()
    print("Browser closed.")

if __name__ == "__main__":
    main()
