"""
test_ai_engine.py

Contains unit tests for AI-related modules, including strategy execution,
reinforcement learning, and hand analysis.

Classes:
- TestAIEngine: Defines test cases for AI components.
"""

import unittest
from ai_engine.strategy_engine import StrategyEngine
from ai_engine.reinforcement_learning import ReinforcementLearner
from ai_engine.hand_analysis import HandAnalyzer

class TestAIEngine(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test environment for AI Engine tests.
        """
        self.strategy_engine = StrategyEngine()
        self.learner = ReinforcementLearner()
        self.hand_analyzer = HandAnalyzer()

    def test_choose_strategy(self):
        """
        Tests if the AI can choose an appropriate strategy based on game state.
        """
        game_state = {"position": "early", "opponents": 3}
        strategy = self.strategy_engine.choose_strategy(game_state)
        self.assertIn(strategy, ["Aggressive", "Defensive"], "Strategy should be valid.")

    def test_update_strategy(self):
        """
        Tests if reinforcement learning updates the strategy correctly after a game result.
        """
        game_result = {"win": True, "reward": 100}
        result = self.learner.update_strategy(game_result)
        self.assertIsNone(result, "Strategy update should complete without errors.")

    def test_analyze_hand(self):
        """
        Tests if hand analysis correctly identifies mistakes.
        """
        hand_data = {"cards": ["As", "Kd"], "result": "loss"}
        analysis = self.hand_analyzer.analyze_hand(hand_data)
        self.assertIn("mistakes", analysis, "Analysis should include detected mistakes.")
