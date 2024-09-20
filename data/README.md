# Data Directory

This directory contains all the data required for training, testing, and evaluating the PokerAI model. It holds datasets related to poker hand histories, RL agent performance metrics, opponent profiling information, and game state logs. The data stored here plays a crucial role in improving the AI's decision-making capabilities and provides the foundation for reinforcement learning and strategy optimization.

## Directory Structure

- **`/hand_history/`**: This folder stores raw and processed hand history data from various poker games. Hand histories contain detailed information about past games, including cards dealt, player actions, pot sizes, and outcomes. This data is used for:
  - **Training the RL Agent**: By feeding historical data to the RL model, the AI can learn from real-world scenarios.
  - **Strategy Refinement**: Hand history data is analyzed to adjust the AI's betting strategies and opponent profiling.
  - **Opponent Insights**: Historical games are used to develop opponent models that predict behaviors based on past actions.

- **`/game_state_logs/`**: Logs of in-game events captured in real-time during the AI's interactions with poker platforms. These files are critical for tracking the current state of the game and include information such as:
  - **Player Hands**: The cards each player holds at any given time.
  - **Pot Size**: The total amount of chips in play.
  - **Action Logs**: A sequence of actions taken by all players in the game (betting, folding, raising, etc.).
  - **Outcomes**: The final results of the hand, including winners, hand rankings, and chip distributions.
  - **Training Feedback**: Captures the reward feedback that informs the reinforcement learning model to improve its decision-making.

- **`/opponent_profiles/`**: This folder contains data that profiles the playing styles and tendencies of various opponents. Based on previous games, the AI builds predictive models to categorize opponents as aggressive, passive, or neutral. Key files include:
  - **Player Statistics**: Aggregated data on opponents' betting patterns, frequency of raises, bluffs, and folds.
  - **Profile Summaries**: High-level summaries of different opponent types, which are used by the AI to adjust its strategies in real-time.

- **`/training_metrics/`**: Contains logs and performance metrics from the training of the RL agent. These files track the agent’s progress over time, helping to fine-tune learning rates and exploration strategies. Metrics include:
  - **Win Rates**: Tracks how often the AI wins based on different strategies and game conditions.
  - **Q-Values**: Records the Q-values learned by the agent during training, which guide decision-making.
  - **Cumulative Rewards**: Measures the total rewards accumulated by the RL agent over time, which is a key performance indicator for the AI’s learning efficiency.

- **`/datasets/`**: This folder holds any external datasets used for training or testing purposes. It might include:
  - **Synthetic Data**: Simulated poker games used to pre-train the RL agent before deploying it on live games.
  - **Test Cases**: Specific hand scenarios or poker situations used to evaluate the AI's decision-making accuracy.

## Usage

1. **Hand History Analysis**: Load hand history data to feed into the AI’s training process and strategy refinement.
2. **Game State Tracking**: Use real-time game logs to monitor and update the AI's knowledge of the current game state.
3. **Opponent Profiling**: Extract and analyze opponent tendencies from the profiling data to enhance real-time decision-making.
4. **Training Monitoring**: Access training metrics to evaluate and adjust the RL agent’s performance.

## Data Flow

1. **Hand histories and game logs** feed directly into the RL model for training.
2. **Opponent profiles** are updated continuously based on real-time game events, informing strategy.
3. **Training metrics** guide iterative adjustments to the AI’s parameters, helping optimize performance.

---

This directory forms the backbone of data-driven decision-making and learning for the PokerAI.
