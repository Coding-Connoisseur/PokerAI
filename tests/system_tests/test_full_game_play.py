import unittest
from rl_module.train_agent import PokerAgent
from strategy_engine.decision_maker import DecisionMaker
from browser_automation.scripts.enter_game import start_game
from browser_automation.scripts.read_game_state import get_game_state
from browser_automation.scripts.place_bet import place_bet
from nlp_chat.response_generator import generate_chat_response

class TestFullGamePlay(unittest.TestCase):
    def setUp(self):
        """
        Initialize components before each test.
        This includes setting up the RL agent, strategy engine, and browser automation.
        """
        # Set up a new poker agent using the RL module
        self.agent = PokerAgent()
        self.agent.load_pretrained_model()

        # Set up the strategy engine
        self.decision_maker = DecisionMaker()

        # Start the game using browser automation
        start_game()

    def test_full_gameplay(self):
        """
        Simulates a full poker game, ensuring the agent interacts with all components correctly.
        This test evaluates the integration of decision-making, browser interaction, and chat responses.
        """
        # Simulate several game rounds
        for _ in range(10):  # Simulate 10 rounds
            # Read the current game state from the poker platform
            game_state = get_game_state()

            # Ensure the game state was successfully captured
            self.assertIsNotNone(game_state, "Failed to capture game state.")

            # Agent makes a decision based on the current state
            decision = self.decision_maker.make_decision(game_state)

            # Verify the decision is valid (e.g., raise, call, fold)
            self.assertIn(decision['action'], ['raise', 'call', 'fold'], "Invalid decision made by the strategy engine.")

            # Place a bet using browser automation based on the agent's decision
            bet_result = place_bet(decision['action'], decision.get('amount', 0))
            self.assertTrue(bet_result, "Failed to place a bet.")

            # Generate a chat response using the NLP chat system
            chat_message = generate_chat_response(game_state, decision)
            self.assertIsNotNone(chat_message, "Failed to generate a chat response.")

        # Ensure the agent performed as expected
        final_results = self.agent.evaluate_performance()
        self.assertGreaterEqual(final_results['win_rate'], 0.4, "Win rate too low.")

    def tearDown(self):
        """
        Clean up after each test by closing browser sessions or other resources.
        """
        # Placeholder for cleaning up (close browsers, save logs, etc.)
        print("Cleaning up after test...")

if __name__ == "__main__":
    unittest.main()
