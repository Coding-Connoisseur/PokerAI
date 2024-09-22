# test_nlp_with_gameplay.py

import unittest
from unittest.mock import patch, MagicMock
from rl_module.environment import PokerEnvironment
from nlp_chat.response_generator import generate_chat_response
from strategy_engine.decision_maker import DecisionMaker

class TestNLPWithGameplay(unittest.TestCase):
    
    def setUp(self):
        """
        Sets up the test environment for integrating NLP with the gameplay.
        Creates a mock PokerEnvironment and DecisionMaker.
        """
        self.mock_env = MagicMock(spec=PokerEnvironment)
        self.mock_decision_maker = MagicMock(spec=DecisionMaker)
        self.mock_env.reset.return_value = {"state": "pre-flop"}
        self.mock_env.step.return_value = ({"state": "post-flop"}, 0, False, {})
        
        # Example mock opponent profiles and chat responses
        self.mock_env.get_opponent_profiles.return_value = [
            {"name": "AggressivePlayer", "profile": "Aggressive"},
            {"name": "CautiousPlayer", "profile": "Passive"}
        ]

    @patch("nlp_chat.response_generator.generate_chat_response")
    def test_nlp_response_on_bluff(self, mock_generate_chat_response):
        """
        Tests whether the NLP module generates a bluff-related chat response when the AI decides to bluff.
        """
        # Mock the decision maker to simulate a bluff
        self.mock_decision_maker.make_decision.return_value = "bluff"
        
        # Simulate the gameplay where a bluff is made
        state = self.mock_env.reset()
        action = self.mock_decision_maker.make_decision(state)
        self.assertEqual(action, "bluff")
        
        # Call the NLP chat response generator after a bluff decision
        generate_chat_response(action)
        
        # Verify that the NLP module generates a bluff-related response
        mock_generate_chat_response.assert_called_with("bluff")
    
    @patch("nlp_chat.response_generator.generate_chat_response")
    def test_nlp_response_on_win(self, mock_generate_chat_response):
        """
        Tests if the NLP module generates a win-related chat response after the AI wins a hand.
        """
        # Simulate game environment reaching a "win" state
        self.mock_env.step.return_value = ({"state": "win"}, 1, True, {})

        # Simulate game interaction where the AI wins
        state, reward, done, _ = self.mock_env.step(self.mock_decision_maker.make_decision.return_value)
        self.assertEqual(state["state"], "win")
        self.assertTrue(done)

        # Generate NLP chat response after win
        generate_chat_response("win")
        
        # Verify the NLP module triggers a win-related response
        mock_generate_chat_response.assert_called_with("win")
    
    @patch("nlp_chat.response_generator.generate_chat_response")
    def test_nlp_response_on_loss(self, mock_generate_chat_response):
        """
        Tests if the NLP module generates a loss-related chat response after the AI loses a hand.
        """
        # Simulate game environment reaching a "loss" state
        self.mock_env.step.return_value = ({"state": "loss"}, -1, True, {})

        # Simulate game interaction where the AI loses
        state, reward, done, _ = self.mock_env.step(self.mock_decision_maker.make_decision.return_value)
        self.assertEqual(state["state"], "loss")
        self.assertTrue(done)

        # Generate NLP chat response after loss
        generate_chat_response("loss")
        
        # Verify the NLP module triggers a loss-related response
        mock_generate_chat_response.assert_called_with("loss")

    @patch("nlp_chat.response_generator.generate_chat_response")
    def test_nlp_chat_frequency(self, mock_generate_chat_response):
        """
        Tests the frequency of chat messages generated by the NLP module during gameplay.
        """
        # Simulate a sequence of game steps
        for _ in range(10):
            state, _, _, _ = self.mock_env.step(self.mock_decision_maker.make_decision.return_value)
            if state["state"] == "post-flop":
                generate_chat_response("comment")
        
        # Verify that chat responses are generated during the game
        self.assertEqual(mock_generate_chat_response.call_count, 10)

if __name__ == "__main__":
    unittest.main()
