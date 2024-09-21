# navigate.py
"""
This script handles navigation across different pages of the poker platform using Selenium.
It ensures that PokerAI can automatically move between critical areas, such as the game lobby,
individual poker tables, and other sections. It handles errors, waits for elements to load,
and retries navigation if necessary.
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Timeout settings for navigation
DEFAULT_TIMEOUT = 10

class Navigator:
    def __init__(self, driver: webdriver):
        """
        Initializes the Navigator with a Selenium WebDriver instance.
        
        :param driver: The Selenium WebDriver controlling the browser.
        """
        self.driver = driver

    def wait_for_element(self, by, value, timeout=DEFAULT_TIMEOUT):
        """
        Waits for an element to appear on the page before proceeding.

        :param by: The method to search by (e.g., By.ID, By.CSS_SELECTOR).
        :param value: The value to search for (e.g., the ID or CSS selector of the element).
        :param timeout: The maximum number of seconds to wait for the element.
        :return: The located WebElement, or raises TimeoutException.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element with {by} = {value} not found within {timeout} seconds.")

    def navigate_to_url(self, url):
        """
        Directs the browser to a specific URL.

        :param url: The URL to navigate to.
        """
        try:
            self.driver.get(url)
            print(f"Navigated to {url}")
        except Exception as e:
            print(f"Failed to navigate to {url}: {e}")
            raise

    def navigate_to_lobby(self):
        """
        Navigates to the main poker lobby where tables can be selected.
        Assumes the lobby is accessible via a button or link.
        """
        try:
            lobby_button = self.wait_for_element(By.CSS_SELECTOR, "button.lobby-btn")
            lobby_button.click()
            print("Navigated to the poker lobby.")
        except NoSuchElementException:
            print("Lobby button not found!")
        except TimeoutException:
            print("Lobby button took too long to appear.")

    def navigate_to_table(self, table_id):
        """
        Navigates to a specific poker table using a table identifier.

        :param table_id: The ID or unique identifier of the table.
        """
        try:
            table_selector = f"div.table[data-id='{table_id}']"
            table_element = self.wait_for_element(By.CSS_SELECTOR, table_selector)
            table_element.click()
            print(f"Navigated to poker table {table_id}.")
        except TimeoutException:
            print(f"Poker table with ID {table_id} not found.")
        except NoSuchElementException:
            print(f"Poker table with ID {table_id} does not exist.")

    def navigate_back(self):
        """
        Navigates back to the previous page.
        """
        try:
            self.driver.back()
            print("Navigated back to the previous page.")
        except Exception as e:
            print(f"Failed to navigate back: {e}")

    def retry_navigation(self, target_function, max_retries=3):
        """
        Retries a navigation action if it fails.

        :param target_function: The function to retry (e.g., navigate_to_table).
        :param max_retries: The maximum number of times to retry.
        :return: True if the navigation succeeds, False otherwise.
        """
        attempts = 0
        while attempts < max_retries:
            try:
                target_function()
                return True
            except Exception as e:
                attempts += 1
                print(f"Navigation attempt {attempts} failed: {e}. Retrying...")
                time.sleep(2)
        print("Max retries reached. Navigation failed.")
        return False

if __name__ == "__main__":
    # Example usage of the Navigator class
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
    
    navigator = Navigator(driver)
    
    # Example: Navigate to the poker site, then to the lobby, and a specific table.
    try:
        navigator.navigate_to_url("https://example-poker-site.com")
        navigator.navigate_to_lobby()
        navigator.navigate_to_table("table12345")
    except Exception as e:
        print(f"Error during navigation: {e}")
    finally:
        driver.quit()
