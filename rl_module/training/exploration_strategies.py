# exploration_strategies.py

import random
import numpy as np

class ExplorationStrategy:
    """
    Base class for defining exploration strategies in RL.
    Each strategy must implement the get_action method, which chooses
    an action based on the current state of the agent and environment.
    """
    def __init__(self):
        pass
    
    def get_action(self, state, q_values, available_actions):
        raise NotImplementedError("This method should be overridden by subclasses.")


class EpsilonGreedyStrategy(ExplorationStrategy):
    """
    Epsilon-Greedy exploration strategy:
    With probability epsilon, the agent will explore by taking a random action.
    With probability 1 - epsilon, the agent will exploit by choosing the action with the highest Q-value.
    """
    def __init__(self, epsilon_start=1.0, epsilon_end=0.1, decay_rate=0.99):
        super().__init__()
        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.decay_rate = decay_rate

    def get_action(self, state, q_values, available_actions):
        # Exploration: With probability epsilon, take a random action
        if random.random() < self.epsilon:
            return random.choice(available_actions)
        # Exploitation: With probability 1 - epsilon, take the best action
        else:
            return np.argmax(q_values)
    
    def decay_epsilon(self):
        """
        Decays epsilon to gradually reduce exploration over time.
        """
        self.epsilon = max(self.epsilon_end, self.epsilon * self.decay_rate)


class SoftmaxExplorationStrategy(ExplorationStrategy):
    """
    Softmax exploration strategy:
    Assigns a probability to each action based on its Q-value using a softmax function, encouraging exploration of higher-reward actions.
    """
    def __init__(self, temperature=1.0):
        super().__init__()
        self.temperature = temperature

    def get_action(self, state, q_values, available_actions):
        # Apply softmax to the Q-values
        exp_q = np.exp(q_values / self.temperature)
        probabilities = exp_q / np.sum(exp_q)
        # Choose an action based on the softmax probabilities
        return np.random.choice(available_actions, p=probabilities)


class UCBExplorationStrategy(ExplorationStrategy):
    """
    Upper Confidence Bound (UCB) exploration strategy:
    Chooses actions based on the confidence interval around the Q-values. 
    This encourages actions with high uncertainty, balancing exploration and exploitation.
    """
    def __init__(self, c=2):
        super().__init__()
        self.c = c
        self.action_counts = None

    def get_action(self, state, q_values, available_actions, total_steps):
        if self.action_counts is None:
            self.action_counts = np.zeros(len(available_actions))

        ucb_values = q_values + self.c * np.sqrt(np.log(total_steps + 1) / (self.action_counts + 1))
        action = np.argmax(ucb_values)
        self.action_counts[action] += 1
        return action


class DecayingEpsilonGreedyStrategy(EpsilonGreedyStrategy):
    """
    Decaying epsilon-greedy exploration strategy:
    Epsilon starts high and decays over time to encourage exploration early in training and more exploitation later.
    """
    def __init__(self, epsilon_start=1.0, epsilon_end=0.05, decay_rate=0.995):
        super().__init__(epsilon_start, epsilon_end, decay_rate)

    def get_action(self, state, q_values, available_actions):
        action = super().get_action(state, q_values, available_actions)
        self.decay_epsilon()
        return action


# Example usage
if __name__ == "__main__":
    # Example Q-values and actions
    q_values = np.array([0.2, 0.5, 0.1, 0.7])
    available_actions = [0, 1, 2, 3]

    # Epsilon-Greedy Strategy
    epsilon_greedy = EpsilonGreedyStrategy()
    action = epsilon_greedy.get_action(None, q_values, available_actions)
    print(f"Epsilon-Greedy selected action: {action}")

    # Softmax Exploration Strategy
    softmax_strategy = SoftmaxExplorationStrategy(temperature=1.0)
    action = softmax_strategy.get_action(None, q_values, available_actions)
    print(f"Softmax selected action: {action}")

    # Upper Confidence Bound Strategy
    ucb_strategy = UCBExplorationStrategy(c=2)
    action = ucb_strategy.get_action(None, q_values, available_actions, total_steps=10)
    print(f"UCB selected action: {action}")
