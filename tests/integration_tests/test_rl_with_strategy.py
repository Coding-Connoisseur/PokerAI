
# test_rl_with_strategy.py

import unittest
from rl_module.q_learning_agent import QLearningAgent
from rl_module.dqn_agent import DQNAgent
from strategy_engine.decision_maker import DecisionMaker
from poker_environment import PokerEnvironment

class TestRLWithStrategy(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment, RL agents, and the strategy engine.
        Initializes both Q-learning and DQN agents, as well as the poker environment.
        """
        self.env = PokerEnvironment()
        self.q_learning_agent = QLearningAgent(self.env)
        self.dqn_agent = DQNAgent(self.env)
        self.strategy_engine = DecisionMaker()

    def test_q_learning_with_strategy(self):
        """
        Test the integration of the Q-learning agent with the strategy engine.
        Ensures the agent makes decisions based on learned Q-values and strategy logic.
        """
        state = self.env.reset()  # Initialize a new poker game state
        action = self.q_learning_agent.choose_action(state)  # Q-learning agent chooses an action
        
        # Pass action through strategy engine to evaluate if it's optimal
        strategy_action = self.strategy_engine.apply_strategy(state, action)
        
        # Assert that a valid action is chosen after applying strategy
        self.assertIn(strategy_action, ['fold', 'check', 'call', 'raise', 'bet'], 
                      "Invalid action chosen by Q-learning with strategy engine")

    def test_dqn_with_strategy(self):
        """
        Test the integration of the DQN agent with the strategy engine.
        Ensures the DQN agent makes decisions based on its neural network outputs and strategy logic.
        """
        state = self.env.reset()  # Initialize a new poker game state
        action = self.dqn_agent.choose_action(state)  # DQN agent chooses an action
        
        # Pass action through strategy engine to evaluate if it's optimal
        strategy_action = self.strategy_engine.apply_strategy(state, action)
        
        # Assert that a valid action is chosen after applying strategy
        self.assertIn(strategy_action, ['fold', 'check', 'call', 'raise', 'bet'], 
                      "Invalid action chosen by DQN with strategy engine")

    def test_rl_agents_consistency(self):
        """
        Test both agents to ensure that, given the same state, they provide consistent 
        and logical decisions after applying the strategy engine.
        """
        state = self.env.reset()  # Initialize a new poker game state
        
        # Get actions from both RL agents
        q_learning_action = self.q_learning_agent.choose_action(state)
        dqn_action = self.dqn_agent.choose_action(state)
        
        # Apply strategy engine to both actions
        strategy_q_action = self.strategy_engine.apply_strategy(state, q_learning_action)
        strategy_dqn_action = self.strategy_engine.apply_strategy(state, dqn_action)
        
        # Both actions should be valid after strategy adjustment
        self.assertIn(strategy_q_action, ['fold', 'check', 'call', 'raise', 'bet'], 
                      "Invalid Q-learning action after strategy adjustment")
        self.assertIn(strategy_dqn_action, ['fold', 'check', 'call', 'raise', 'bet'], 
                      "Invalid DQN action after strategy adjustment")
        
        # Test for consistency between agents (optional, since strategies could diverge)
        self.assertNotEqual(strategy_q_action, strategy_dqn_action, 
                            "Both agents should not always take the same action, but both actions should be valid")

if __name__ == '__main__':
    unittest.main()
