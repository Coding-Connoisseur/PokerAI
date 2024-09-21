# policy_gradient_agent.py

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
import gym
import random

class PolicyGradientAgent:
    def __init__(self, state_size, action_size, learning_rate=0.001, gamma=0.99):
        """
        Initialize the Policy Gradient agent.

        Args:
            state_size (int): Dimension of the state space.
            action_size (int): Dimension of the action space.
            learning_rate (float): Learning rate for the neural network optimizer.
            gamma (float): Discount factor for reward calculation.
        """
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma
        
        # Memory to store experiences
        self.states = []
        self.actions = []
        self.rewards = []
        
        # Build policy network
        self.model = self.build_model()

    def build_model(self):
        """
        Builds the policy network using a simple neural network architecture.
        
        Returns:
            keras.Model: A compiled Keras model.
        """
        model = tf.keras.Sequential()
        model.add(layers.Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(layers.Dense(24, activation='relu'))
        model.add(layers.Dense(self.action_size, activation='softmax'))  # Output probabilities for each action

        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate), loss='categorical_crossentropy')
        return model

    def remember(self, state, action, reward):
        """
        Store experiences in memory for training.

        Args:
            state (array): The observed state.
            action (int): The action taken.
            reward (float): The reward received.
        """
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)

    def act(self, state):
        """
        Select an action based on the current policy (probabilistic).

        Args:
            state (array): The current state.

        Returns:
            int: The action chosen based on policy.
        """
        state = np.reshape(state, [1, self.state_size])
        action_probs = self.model.predict(state, verbose=0)
        return np.random.choice(self.action_size, p=action_probs[0])

    def discount_rewards(self, rewards):
        """
        Apply discount to the rewards for each time step.

        Args:
            rewards (list): The rewards received during an episode.

        Returns:
            list: The discounted rewards.
        """
        discounted_rewards = np.zeros_like(rewards, dtype=np.float32)
        cumulative_sum = 0.0
        for t in reversed(range(len(rewards))):
            cumulative_sum = cumulative_sum * self.gamma + rewards[t]
            discounted_rewards[t] = cumulative_sum
        return discounted_rewards

    def train(self):
        """
        Train the policy network using the experiences stored in memory.
        """
        # Prepare data for training
        states = np.vstack(self.states)
        actions = np.array(self.actions)
        rewards = self.discount_rewards(self.rewards)
        
        # Normalize rewards
        rewards = (rewards - np.mean(rewards)) / (np.std(rewards) + 1e-7)
        
        # Convert actions to one-hot encoding
        actions_one_hot = np.zeros([len(actions), self.action_size])
        actions_one_hot[np.arange(len(actions)), actions] = 1
        
        # Train the policy network
        self.model.train_on_batch(states, actions_one_hot, sample_weight=rewards)
        
        # Clear the memory after training
        self.states, self.actions, self.rewards = [], [], []

def train_policy_gradient_agent(env_name="CartPole-v1", episodes=1000, render=False):
    """
    Trains a policy gradient agent on a given environment.

    Args:
        env_name (str): The OpenAI gym environment.
        episodes (int): Number of training episodes.
        render (bool): If True, renders the environment during training.
    """
    env = gym.make(env_name)
    agent = PolicyGradientAgent(state_size=env.observation_space.shape[0], action_size=env.action_space.n)

    for episode in range(episodes):
        state = env.reset()
        episode_reward = 0

        while True:
            if render:
                env.render()

            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)

            agent.remember(state, action, reward)
            state = next_state
            episode_reward += reward

            if done:
                agent.train()
                print(f"Episode {episode + 1}/{episodes} - Reward: {episode_reward}")
                break

    env.close()

if __name__ == "__main__":
    train_policy_gradient_agent(episodes=500, render=False)
