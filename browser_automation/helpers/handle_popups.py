from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def handle_popups(driver, timeout=5):
    """
    Detects and closes common popups or interruptions that may appear during a poker game.
    This function tries to identify elements that resemble popups and close them to prevent interruptions.

    Parameters:
    driver (WebDriver): The Selenium WebDriver instance controlling the browser.
    timeout (int): Time in seconds to wait for the popup elements to appear before assuming no popup exists.

    Returns:
    bool: Returns True if a popup was found and closed, False otherwise.
    """
    popup_selectors = [
        # Add common selectors for popups, modals, or ads that might appear on poker platforms.
        (By.XPATH, "//div[@class='popup-close-button']"),  # Generic close button for popups
        (By.XPATH, "//button[text()='Close']"),  # Button with text 'Close'
        (By.XPATH, "//button[text()='No Thanks']"),  # For dismissing optional offers
        (By.XPATH, "//div[@class='modal-close']"),  # Common modal close
        (By.CLASS_NAME, "ad-close"),  # Close button for ads
        (By.XPATH, "//button[@aria-label='Close']"),  # Buttons with ARIA labels
    ]
    
    for selector in popup_selectors:
        try:
            # Wait until the popup appears and is clickable, then close it
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector))
            element.click()
            print(f"Popup closed using selector: {selector}")
            return True
        except TimeoutException:
            # No popup found within the timeout for this selector
            continue
        except NoSuchElementException:
            # In case an element is expected but not found
            continue
        except Exception as e:
            # Catch-all for any unexpected exceptions and log them
            print(f"Error handling popup with selector {selector}: {e}")

    # No popups found if we reach this point
    print("No popups found.")
    return False

def handle_ads(driver, timeout=5):
    """
    Specifically handles ads that interrupt the poker platform. These ads often appear during game loading
    or between hands.

    Parameters:
    driver (WebDriver): The Selenium WebDriver instance controlling the browser.
    timeout (int): Time in seconds to wait for ad elements before assuming no ad exists.

    Returns:
    bool: Returns True if an ad was found and closed, False otherwise.
    """
    ad_selectors = [
        (By.ID, "ad-close-button"),  # Ad close button with specific ID
        (By.XPATH, "//button[text()='Skip Ad']"),  # Button to skip video or banner ads
        (By.CLASS_NAME, "advertisement-close"),  # Close button for general advertisements
    ]
    
    for selector in ad_selectors:
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector))
            element.click()
            print(f"Ad closed using selector: {selector}")
            return True
        except TimeoutException:
            continue
        except NoSuchElementException:
            continue
        except Exception as e:
            print(f"Error handling ad with selector {selector}: {e}")
    
    print("No ads found.")
    return False

def dismiss_all_popups(driver, timeout=5):
    """
    Attempts to dismiss all types of popups and ads that may interrupt the game.

    Parameters:
    driver (WebDriver): The Selenium WebDriver instance controlling the browser.
    timeout (int): Time in seconds to wait for popups or ads to appear.

    Returns:
    None
    """
    print("Checking for popups or ads...")
    popup_closed = handle_popups(driver, timeout)
    ad_closed = handle_ads(driver, timeout)
    
    if popup_closed or ad_closed:
        print("At least one popup or ad was successfully handled.")
    else:
        print("No popups or ads were detected.")

