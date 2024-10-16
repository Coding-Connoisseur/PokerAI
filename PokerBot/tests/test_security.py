"""
test_security.py

Contains unit tests for security components, including anti-detection,
account rotation, and VPN handling.

Classes:
- TestSecurity: Defines test cases for security functionalities.
"""

import unittest
from security.anti_detection import AntiDetection
from security.account_rotation import AccountRotation
from security.vpn_handler import VPNHandler

class TestSecurity(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test environment for Security tests.
        """
        self.anti_detection = AntiDetection()
        self.account_rotation = AccountRotation()
        self.vpn_handler = VPNHandler()

    def test_randomize_action_timing(self):
        """
        Tests if action timing is randomized correctly.
        """
        delay = self.anti_detection.randomize_action_timing()
        self.assertGreater(delay, 0, "Random delay should be positive.")

    def test_select_account(self):
        """
        Tests if the account rotation selects a valid account.
        """
        account = self.account_rotation.select_account()
        self.assertIsNotNone(account, "Account selection should return an account.")

    def test_connect_to_vpn(self):
        """
        Tests if the VPN handler can connect to a specified location.
        """
        result = self.vpn_handler.connect_to_vpn("USA")
        self.assertTrue(result, "VPN connection should be successful when given a valid location.")
