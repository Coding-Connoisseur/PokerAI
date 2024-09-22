import unittest
from unittest.mock import patch, MagicMock
from browser_automation.actions.click_button import click_button
from browser_automation.actions.enter_text import enter_text
from browser_automation.actions.navigate import navigate

class TestBrowserAutomation(unittest.TestCase):
    
    @patch('browser_automation.actions.click_button.webdriver')
    def test_click_button_success(self, mock_webdriver):
        """
        Test if the click_button function correctly clicks a button.
        """
        # Mock WebDriver and button element
        mock_driver = MagicMock()
        mock_webdriver.Chrome.return_value = mock_driver
        mock_element = MagicMock()
        mock_driver.find_element.return_value = mock_element

        # Call the function
        click_button("some_button_selector")
        
        # Check if WebDriver was used correctly
        mock_webdriver.Chrome.assert_called_once()
        mock_driver.find_element.assert_called_once_with("css selector", "some_button_selector")
        mock_element.click.assert_called_once()

    @patch('browser_automation.actions.enter_text.webdriver')
    def test_enter_text_success(self, mock_webdriver):
        """
        Test if the enter_text function correctly inputs text into a field.
        """
        # Mock WebDriver and text field element
        mock_driver = MagicMock()
        mock_webdriver.Chrome.return_value = mock_driver
        mock_element = MagicMock()
        mock_driver.find_element.return_value = mock_element

        # Call the function
        enter_text("some_input_selector", "Test message")
        
        # Check if WebDriver was used correctly
        mock_webdriver.Chrome.assert_called_once()
        mock_driver.find_element.assert_called_once_with("css selector", "some_input_selector")
        mock_element.send_keys.assert_called_once_with("Test message")

    @patch('browser_automation.actions.navigate.webdriver')
    def test_navigate_success(self, mock_webdriver):
        """
        Test if the navigate function correctly navigates to a URL.
        """
        # Mock WebDriver
        mock_driver = MagicMock()
        mock_webdriver.Chrome.return_value = mock_driver

        # Call the function
        navigate("https://pokerplatform.com")
        
        # Check if WebDriver navigated to the correct URL
        mock_webdriver.Chrome.assert_called_once()
        mock_driver.get.assert_called_once_with("https://pokerplatform.com")

    @patch('browser_automation.actions.click_button.webdriver')
    def test_click_button_failure(self, mock_webdriver):
        """
        Test if click_button handles failure when the button is not found.
        """
        # Mock WebDriver and simulate an exception
        mock_driver = MagicMock()
        mock_webdriver.Chrome.return_value = mock_driver
        mock_driver.find_element.side_effect = Exception("Element not found")

        # Call the function and verify the exception handling
        with self.assertRaises(Exception):
            click_button("non_existent_selector")
        
        mock_webdriver.Chrome.assert_called_once()
        mock_driver.find_element.assert_called_once_with("css selector", "non_existent_selector")

if __name__ == "__main__":
    unittest.main()
