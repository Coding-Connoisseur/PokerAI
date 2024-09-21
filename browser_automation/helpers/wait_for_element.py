# wait_for_element.py
"""
This module contains helper functions to wait for specific elements to become
visible, clickable, or present on the web page. These functions are useful for
browser automation to ensure that interactions occur only when elements are ready,
preventing errors due to timing issues.

Requirements:
- selenium
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

def wait_for_element_visible(driver, by, locator, timeout=10):
    """
    Waits for an element to be visible on the page before proceeding.

    Args:
        driver (WebDriver): The Selenium WebDriver instance controlling the browser.
        by (By): The method to locate the element (e.g., By.ID, By.XPATH).
        locator (str): The locator of the element (e.g., the element's ID or XPath).
        timeout (int): The maximum time (in seconds) to wait for the element to become visible.

    Returns:
        WebElement: The located WebElement if it becomes visible within the timeout.
    
    Raises:
        TimeoutException: If the element is not visible within the given time.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
        return element
    except TimeoutException:
        print(f"Element not visible within {timeout} seconds using locator: {locator}")
        raise


def wait_for_element_clickable(driver, by, locator, timeout=10):
    """
    Waits for an element to be clickable on the page before proceeding.

    Args:
        driver (WebDriver): The Selenium WebDriver instance controlling the browser.
        by (By): The method to locate the element (e.g., By.ID, By.XPATH).
        locator (str): The locator of the element (e.g., the element's ID or XPath).
        timeout (int): The maximum time (in seconds) to wait for the element to become clickable.

    Returns:
        WebElement: The located WebElement if it becomes clickable within the timeout.
    
    Raises:
        TimeoutException: If the element is not clickable within the given time.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        return element
    except TimeoutException:
        print(f"Element not clickable within {timeout} seconds using locator: {locator}")
        raise


def wait_for_element_present(driver, by, locator, timeout=10):
    """
    Waits for an element to be present in the DOM (but not necessarily visible) before proceeding.

    Args:
        driver (WebDriver): The Selenium WebDriver instance controlling the browser.
        by (By): The method to locate the element (e.g., By.ID, By.XPATH).
        locator (str): The locator of the element (e.g., the element's ID or XPath).
        timeout (int): The maximum time (in seconds) to wait for the element to be present in the DOM.

    Returns:
        WebElement: The located WebElement if it becomes present within the timeout.
    
    Raises:
        TimeoutException: If the element is not present within the given time.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return element
    except TimeoutException:
        print(f"Element not present in the DOM within {timeout} seconds using locator: {locator}")
        raise


def is_element_present(driver, by, locator):
    """
    Checks if an element is present in the DOM without waiting.

    Args:
        driver (WebDriver): The Selenium WebDriver instance controlling the browser.
        by (By): The method to locate the element (e.g., By.ID, By.XPATH).
        locator (str): The locator of the element (e.g., the element's ID or XPath).

    Returns:
        bool: True if the element is found, False otherwise.
    """
    try:
        driver.find_element(by, locator)
        return True
    except NoSuchElementException:
        return False


def wait_for_element_disappear(driver, by, locator, timeout=10):
    """
    Waits for an element to disappear from the DOM (or become invisible) before proceeding.

    Args:
        driver (WebDriver): The Selenium WebDriver instance controlling the browser.
        by (By): The method to locate the element (e.g., By.ID, By.XPATH).
        locator (str): The locator of the element (e.g., the element's ID or XPath).
        timeout (int): The maximum time (in seconds) to wait for the element to disappear.

    Returns:
        bool: True if the element disappears within the timeout, False otherwise.
    
    Raises:
        TimeoutException: If the element does not disappear within the given time.
    """
    try:
        WebDriverWait(driver, timeout).until_not(
            EC.presence_of_element_located((by, locator))
        )
        return True
    except TimeoutException:
        print(f"Element did not disappear within {timeout} seconds using locator: {locator}")
        return False


# Example Usage (This would be removed in production):
if __name__ == "__main__":
    from selenium import webdriver

    # Set up the WebDriver instance (using Chrome as an example)
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')

    # Navigate to a sample website
    driver.get("https://example.com")

    # Example usage of the wait_for_element_visible function
    try:
        element = wait_for_element_visible(driver, By.ID, "sampleElementID", timeout=15)
        print("Element is visible and ready for interaction.")
    except TimeoutException:
        print("Failed to find the visible element.")

    # Quit the browser
    driver.quit()
