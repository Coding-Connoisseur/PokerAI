"""
test_gameplay.py

Contains unit tests for the GameSession module, verifying session management,
gameplay execution, and session termination.

Classes:
- TestGameSession: Defines test cases for gameplay functionality.
"""

import unittest
from core.game_session import GameSession

class TestGameSession(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test environment for GameSession tests.
        """
        self.game_session = GameSession()

    def test_start_session(self):
        """
        Tests if a game session starts successfully.
        """
        game_type = "Texas Hold'em"
        buy_in_amount = 50.0
        result = self.game_session.start_session(game_type, buy_in_amount)
        self.assertIsNone(result, "Session start should complete without errors.")

    def test_end_session(self):
        """
        Tests if a game session ends successfully, including cash out.
        """
        result = self.game_session.end_session()
        self.assertIsNone(result, "Session end should complete without errors.")

    def test_execute_turn(self):
        """
        Tests if a game turn executes an action successfully.
        """
        result = self.game_session.execute_turn()
        self.assertIsNone(result, "Turn execution should complete without errors.")
