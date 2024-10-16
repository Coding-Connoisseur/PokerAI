"""
test_account_manager.py

Contains unit tests for the AccountManager module, verifying account creation,
login, and validation.

Classes:
- TestAccountManager: Defines test cases for account management functionalities.
"""

import unittest
from core.account_manager import AccountManager

class TestAccountManager(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test environment for AccountManager tests.
        """
        self.account_manager = AccountManager()

    def test_create_account(self):
        """
        Tests if an account is successfully created on a platform.
        """
        platform_name = "TestPlatform"
        result = self.account_manager.create_account(platform_name)
        self.assertIsNotNone(result, "Account creation should return account details.")
        
    def test_login(self):
        """
        Tests if the bot can log into an existing account.
        """
        platform_name = "TestPlatform"
        credentials = {"username": "test_user", "password": "test_pass"}
        result = self.account_manager.login(platform_name, credentials)
        self.assertTrue(result, "Login should return True if successful.")

    def test_validate_account(self):
        """
        Tests if the account validation correctly identifies an active account.
        """
        account_info = {"username": "test_user", "status": "active"}
        result = self.account_manager.validate_account(account_info)
        self.assertTrue(result, "Account validation should return True for active accounts.")
