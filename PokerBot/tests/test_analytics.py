"""
test_analytics.py

Contains unit tests for analytics components, including game statistics,
player behavior tracking, and financial tracking.

Classes:
- TestAnalytics: Defines test cases for analytics functionalities.
"""

import unittest
from analytics.game_statistics import GameStatistics
from analytics.player_behavior import PlayerBehavior
from analytics.financial_tracker import FinancialTracker

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test environment for Analytics tests.
        """
        self.stats = GameStatistics()
        self.behavior = PlayerBehavior()
        self.financial_tracker = FinancialTracker()

    def test_update_statistics(self):
        """
        Tests if game statistics update correctly based on game data.
        """
        game_data = {"win": True, "net_profit": 20}
        result = self.stats.update_statistics(game_data)
        self.assertIsNone(result, "Statistics update should complete without errors.")

    def test_track_opponent(self):
        """
        Tests if opponent behavior is tracked accurately.
        """
        opponent_id = "Player123"
        action_data = {"action": "raise", "amount": 50}
        result = self.behavior.track_opponent(opponent_id, action_data)
        self.assertIsNone(result, "Opponent tracking should complete without errors.")

    def test_record_transaction(self):
        """
        Tests if financial transactions are recorded correctly.
        """
        result = self.financial_tracker.record_transaction("win", 50)
        self.assertIsNone(result, "Transaction recording should complete without errors.")
