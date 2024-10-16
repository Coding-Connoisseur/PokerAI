"""
test_ui_interaction.py

Contains unit tests for UI interaction components, verifying screen scraping,
click handling, and web automation functionalities.

Classes:
- TestUIInteraction: Defines test cases for UI interaction modules.
"""

import unittest
from ui_interaction.screen_scraper import ScreenScraper
from ui_interaction.click_handler import ClickHandler
from ui_interaction.web_automation import WebAutomation

class TestUIInteraction(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test environment for UI Interaction tests.
        """
        self.screen_scraper = ScreenScraper()
        self.click_handler = ClickHandler()
        self.web_automation = WebAutomation()

    def test_capture_screen(self):
        """
        Tests if the screen scraper can capture and return an image.
        """
        image = self.screen_scraper.capture_screen()
        self.assertIsNotNone(image, "Screen capture should return image data.")

    def test_click_button(self):
        """
        Tests if the click handler can perform a click action successfully.
        """
        button_label = "Fold"
        result = self.click_handler.click_button(button_label)
        self.assertTrue(result, "Button click should be successful.")

    def test_fill_form(self):
        """
        Tests if the web automation can fill a form with given data.
        """
        form_data = {"username": "test_user", "password": "test_pass"}
        result = self.web_automation.fill_form(form_data)
        self.assertIsNone(result, "Form fill should complete without errors.")
