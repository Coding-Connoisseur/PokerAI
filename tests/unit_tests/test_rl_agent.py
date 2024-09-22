
# test_rl_agent.py

import unittest
import numpy as np
from rl_module.q_learning_agent import QLearningAgent
from rl_module.dqn_agent import DQNAgent

class TestRLAgent(unittest.TestCase):

    def setUp(self):
        """
        Initialize both the Q-Learning and DQN agents with dummy parameters for testing.
        """
        self.q_agent = QLearningAgent(state_size=10, action_size=5, learning_rate=0.1, gamma=0.9, epsilon=0.2)
        self.dqn_agent = DQNAgent(state_size=10, action_size=5, learning_rate=0.1, gamma=0.9, epsilon=0.2)

        # Example state and action spaces
        self.state = np.random.rand(10)
        self.action = 2
        self.reward = 10
        self.next_state = np.random.rand(10)
        self.done = False

    def test_q_learning_update(self):
        """
        Test that the Q-Learning agent updates the Q-table correctly.
        """
        initial_q_value = self.q_agent.q_table[0, self.action]
        
        # Perform update
        self.q_agent.learn(state=0, action=self.action, reward=self.reward, next_state=1, done=self.done)
        
        updated_q_value = self.q_agent.q_table[0, self.action]
        self.assertNotEqual(initial_q_value, updated_q_value, "Q-value should have been updated after learning step")

    def test_q_learning_policy(self):
        """
        Test that the Q-Learning agent selects an action based on the epsilon-greedy policy.
        """
        action = self.q_agent.choose_action(0)
        self.assertIn(action, range(self.q_agent.action_size), "Chosen action is outside the valid action space")

    def test_dqn_agent_prediction(self):
        """
        Test that the DQN agent predicts valid Q-values for a given state.
        """
        q_values = self.dqn_agent.model.predict(self.state.reshape(1, -1))
        self.assertEqual(q_values.shape, (1, self.dqn_agent.action_size), "DQN output shape mismatch")

    def test_dqn_agent_training_step(self):
        """
        Test that the DQN agent performs a valid training step.
        """
        # Initial prediction
        q_values_initial = self.dqn_agent.model.predict(self.state.reshape(1, -1))

        # Perform training step
        self.dqn_agent.remember(self.state, self.action, self.reward, self.next_state, self.done)
        self.dqn_agent.replay(batch_size=1)

        # Prediction after training
        q_values_post = self.dqn_agent.model.predict(self.state.reshape(1, -1))

        self.assertNotEqual(np.sum(q_values_initial), np.sum(q_values_post), "DQN should update weights during training")

    def test_dqn_epsilon_decay(self):
        """
        Test that the DQN agent's epsilon value decays as expected after each training episode.
        """
        initial_epsilon = self.dqn_agent.epsilon
        self.dqn_agent.epsilon_decay()
        self.assertLess(self.dqn_agent.epsilon, initial_epsilon, "Epsilon should decay after each episode")

if __name__ == "__main__":
    unittest.main()
