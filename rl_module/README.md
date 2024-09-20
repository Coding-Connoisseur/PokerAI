# Reinforcement Learning (RL) Module

The `rl_module` directory contains all the components required to train and evaluate the PokerAI using reinforcement learning techniques. The primary goal of this module is to help the AI learn optimal poker strategies by interacting with the environment and receiving feedback in the form of rewards. This directory supports both traditional Q-Learning as well as more advanced deep reinforcement learning methods such as Deep Q-Networks (DQN).

## Directory Structure

- **`/agents/`**: This folder contains the RL agents responsible for decision-making during poker games. Each agent is an implementation of a specific RL algorithm, which learns how to make optimal betting, folding, or raising decisions.
  - **`q_learning_agent.py`**: Implements the traditional Q-Learning algorithm, which updates the Q-values for each game state based on rewards.
  - **`dqn_agent.py`**: Implements a Deep Q-Network (DQN) agent, where a neural network approximates the Q-values for more complex decision-making.
  - **`policy_gradient_agent.py`**: Implements a Policy Gradient agent, an alternative RL method where the agent learns directly by optimizing the policy that dictates actions.

- **`/training/`**: Contains scripts and configurations for training the RL agents.
  - **`train_agent.py`**: Main script for training the selected agent. It runs episodes where the agent plays poker hands and learns from the outcomes.
  - **`rewards.py`**: Defines the reward structure for the training process. For example, winning a hand may give a high positive reward, while losing a hand results in a negative reward.
  - **`exploration_strategies.py`**: Implements different exploration strategies, such as epsilon-greedy, which balances the trade-off between exploring new strategies and exploiting known ones.
  
- **`/environment/`**: This folder includes the environment class, which simulates the poker game. The RL agent interacts with this environment, which sends back observations and rewards.
  - **`poker_environment.py`**: Defines the poker environment where the game is simulated. It sends the game state (e.g., cards, pot size, opponent actions) to the RL agent and returns rewards based on the agent's actions.
  - **`state_representation.py`**: Converts the game state into a format that the RL agent can understand and process. This may involve encoding the cards, player actions, and pot size into numerical vectors.
  
- **`/evaluation/`**: Contains tools for evaluating the performance of the RL agents after training.
  - **`evaluate_agent.py`**: Evaluates the agent’s performance by running test games and calculating metrics such as win rate, total rewards, and decision accuracy.
  - **`metrics_logger.py`**: Logs key metrics such as average rewards, number of wins, and learning progress over time, helping visualize and monitor the training process.
  - **`visualization_tools.py`**: Scripts to generate visualizations (e.g., reward curves, Q-value heatmaps) to analyze how the agent is learning and improving.

## Key Components

### 1. **Q-Learning Agent**
The `q_learning_agent.py` script implements a traditional Q-Learning agent that learns by updating a table of Q-values based on rewards received from specific actions. This agent is suitable for simpler environments with smaller state spaces.

### 2. **Deep Q-Network (DQN) Agent**
The `dqn_agent.py` script implements a Deep Q-Network agent, which uses a neural network to approximate the Q-values. This is ideal for complex environments like poker, where the state space is too large for traditional Q-Learning.

### 3. **Environment Simulation**
The `poker_environment.py` script simulates the poker game, providing observations (current game state) to the agent and calculating rewards based on the agent's actions (e.g., betting, folding, raising).

### 4. **Training and Exploration**
The training scripts (`train_agent.py`) run episodes where the agent plays poker hands, learns from rewards, and refines its strategy. The exploration strategies (`exploration_strategies.py`) define how the agent balances between trying new actions and exploiting known successful ones.

### 5. **Evaluation and Metrics**
After training, the agent is evaluated using `evaluate_agent.py`. Performance metrics are logged, and visualizations are generated to analyze how the agent improves over time.

## Usage

1. **Configure Training**: Modify the `train_agent.py` script to select the desired RL agent (Q-Learning, DQN, etc.), and adjust hyperparameters (e.g., learning rate, exploration strategy).
2. **Train the Agent**: Run the `train_agent.py` script to start the training process. The agent will play poker hands, receive rewards, and improve its strategy over time.
3. **Monitor Training**: Use `metrics_logger.py` and `visualization_tools.py` to track the agent’s progress and visualize performance improvements.
4. **Evaluate the Agent**: Once training is complete, run the `evaluate_agent.py` script to test the agent's performance in various poker scenarios and log key metrics.

## Future Improvements

- **Multi-Agent Training**: Implement multi-agent reinforcement learning, where multiple AI agents play against each other to improve their strategies.
- **Transfer Learning**: Add transfer learning capabilities, allowing the agent to adapt to new poker platforms or game formats with minimal retraining.
- **Custom Reward Structures**: Expand the `rewards.py` to support more complex reward structures, such as accounting for long-term strategic decisions.

---

This directory forms the core of the PokerAI's learning process, allowing it to continually improve its poker-playing abilities through reinforcement learning.
