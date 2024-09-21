# q_learning_agent.py

import numpy as np
import random
import json
import os

class QLearningAgent:
    def __init__(self, state_size, action_size, config_path="config/rl_config.yaml"):
        """
        Initializes the Q-Learning agent with the given state and action sizes.
        
        Args:
            state_size (int): The size of the state space.
            action_size (int): The size of the action space.
            config_path (str): Path to the configuration file for RL parameters.
        """
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = np.zeros((state_size, action_size))

        # Load hyperparameters from config file
        self.load_config(config_path)

    def load_config(self, config_path):
        """
        Loads the Q-Learning hyperparameters from the configuration file.
        
        Args:
            config_path (str): Path to the configuration file.
        """
        import yaml
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        
        self.learning_rate = config['learning_rate']
        self.discount_rate = config['discount_rate']
        self.exploration_rate = config['exploration_rate']
        self.exploration_decay = config['exploration_decay']
        self.min_exploration_rate = config['min_exploration_rate']
        self.save_path = config.get('save_path', 'rl_module/models/q_table.json')

    def choose_action(self, state):
        """
        Chooses the next action for the agent to take based on the current state.
        
        Args:
            state (int): The current state of the agent.

        Returns:
            int: The action chosen by the agent.
        """
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(range(self.action_size))
        return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        """
        Updates the Q-value for the state-action pair based on the observed reward and the next state.
        
        Args:
            state (int): The current state of the agent.
            action (int): The action taken by the agent.
            reward (float): The reward received for taking the action.
            next_state (int): The resulting state after taking the action.
        """
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_rate * self.q_table[next_state, best_next_action]
        td_error = td_target - self.q_table[state, action]
        
        self.q_table[state, action] += self.learning_rate * td_error

    def decay_exploration(self):
        """
        Decays the exploration rate after each episode.
        """
        self.exploration_rate = max(self.min_exploration_rate, self.exploration_rate * self.exploration_decay)

    def save_q_table(self):
        """
        Saves the Q-table to a JSON file for later use or analysis.
        """
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        with open(self.save_path, 'w') as file:
            json.dump(self.q_table.tolist(), file)

    def load_q_table(self):
        """
        Loads a saved Q-table from a JSON file if available.
        """
        if os.path.exists(self.save_path):
            with open(self.save_path, 'r') as file:
                self.q_table = np.array(json.load(file))

    def reset(self):
        """
        Resets the Q-table and exploration rate to start a new training process.
        """
        self.q_table = np.zeros((self.state_size, self.action_size))
        self.exploration_rate = 1.0

# Example of usage
if __name__ == "__main__":
    state_size = 100  # Example state space size
    action_size = 4   # Example action space size
    agent = QLearningAgent(state_size, action_size)

    # Simulate a few episodes (this is for demonstration)
    for episode in range(100):
        state = random.randint(0, state_size - 1)
        action = agent.choose_action(state)
        reward = random.uniform(-1, 1)  # Simulated reward
        next_state = random.randint(0, state_size - 1)

        agent.update_q_table(state, action, reward, next_state)
        agent.decay_exploration()

    # Save the trained Q-table
    agent.save_q_table()
