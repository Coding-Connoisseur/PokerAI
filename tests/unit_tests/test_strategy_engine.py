import unittest
from strategy_engine.pre_flop_strategy import pre_flop_rules
from strategy_engine.post_flop_strategy import hand_evaluation, pot_odds_calculator
from strategy_engine.bluffing_engine import bluff_probability
from strategy_engine.opponent_modeling import opponent_profiling

class TestStrategyEngine(unittest.TestCase):

    def setUp(self):
        """
        This method sets up common variables or mock data used for the tests.
        """
        # Example setup data, modify based on actual function requirements
        self.hand = ['Ah', 'Kh']
        self.community_cards = ['2d', '7c', '5h']
        self.opponent_stats = {
            'aggressiveness': 0.8,
            'bluff_frequency': 0.2,
            'fold_percentage': 0.6
        }
        self.pot_size = 100
        self.bet_size = 20

    def test_pre_flop_rules(self):
        """
        Test the pre-flop strategy logic to ensure correct decisions are made based on the starting hand.
        """
        decision = pre_flop_rules(self.hand, position='early')
        self.assertIn(decision, ['raise', 'call', 'fold'], "Pre-flop decision should be one of 'raise', 'call', or 'fold'.")
    
    def test_hand_evaluation(self):
        """
        Test the hand evaluation logic after the flop.
        """
        hand_strength = hand_evaluation(self.hand, self.community_cards)
        self.assertGreaterEqual(hand_strength, 0, "Hand strength should be a non-negative value.")
        self.assertLessEqual(hand_strength, 1, "Hand strength should be between 0 and 1.")

    def test_pot_odds_calculator(self):
        """
        Test the pot odds calculation to ensure the correct evaluation of whether to call a bet.
        """
        pot_odds = pot_odds_calculator(self.pot_size, self.bet_size)
        self.assertGreaterEqual(pot_odds, 0, "Pot odds should be a non-negative value.")
        self.assertLessEqual(pot_odds, 1, "Pot odds should be between 0 and 1.")

    def test_bluff_probability(self):
        """
        Test the bluffing engine to check if the bluff probability is calculated correctly based on opponent behavior.
        """
        bluff_prob = bluff_probability(self.opponent_stats)
        self.assertGreaterEqual(bluff_prob, 0, "Bluff probability should be a non-negative value.")
        self.assertLessEqual(bluff_prob, 1, "Bluff probability should be between 0 and 1.")

    def test_opponent_profiling(self):
        """
        Test opponent profiling to ensure correct opponent categorization.
        """
        profile = opponent_profiling(self.opponent_stats)
        self.assertIn(profile, ['aggressive', 'passive', 'neutral'], "Profile should classify the opponent into 'aggressive', 'passive', or 'neutral'.")

if __name__ == "__main__":
    unittest.main()
