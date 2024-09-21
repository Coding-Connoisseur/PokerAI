# dqn_agent.py

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque

class DQNAgent:
    def __init__(self, state_size, action_size, gamma=0.99, epsilon=1.0, epsilon_min=0.01, epsilon_decay=0.995, learning_rate=0.001, batch_size=64, memory_size=10000):
        self.state_size = state_size
        self.action_size = action_size
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.memory = deque(maxlen=memory_size)
        
        # Build the model
        self.model = self._build_model()

    def _build_model(self):
        """
        Creates a simple neural network for approximating Q-values.
        """
        model = nn.Sequential(
            nn.Linear(self.state_size, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, self.action_size)
        )
        return model

    def remember(self, state, action, reward, next_state, done):
        """
        Store a transition in memory for experience replay.
        """
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        """
        Choose an action using epsilon-greedy strategy.
        """
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state = torch.FloatTensor(state).unsqueeze(0)
        q_values = self.model(state)
        return torch.argmax(q_values).item()

    def replay(self):
        """
        Train the model using randomly sampled experiences from memory.
        """
        if len(self.memory) < self.batch_size:
            return

        minibatch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                next_state = torch.FloatTensor(next_state).unsqueeze(0)
                target += self.gamma * torch.max(self.model(next_state)).item()

            state = torch.FloatTensor(state).unsqueeze(0)
            q_values = self.model(state)
            target_f = q_values.clone().detach()
            target_f[0][action] = target

            criterion = nn.MSELoss()
            optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
            optimizer.zero_grad()
            loss = criterion(q_values, target_f)
            loss.backward()
            optimizer.step()

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        """
        Load a pre-trained model.
        """
        self.model.load_state_dict(torch.load(name))

    def save(self, name):
        """
        Save the current model.
        """
        torch.save(self.model.state_dict(), name)
