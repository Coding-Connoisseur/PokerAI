# Data Directory

This directory contains all data essential for training, testing, and evaluating the PokerAI model. These datasets include poker hand histories, game logs, opponent profiling data, and performance metrics. The data is used to enhance decision-making capabilities, providing a solid foundation for reinforcement learning and strategic optimization.

## Directory Structure

- **`/hand_history/`**: Stores both raw and processed hand history data from poker games. The data is used to train the AI and refine its strategy over time.
  - **`hand_history_samples.json`**: Sample hand history data for training and testing.
  
- **`/game_state_logs/`**: Logs in-game events such as player hands, pot size, and player actions. These logs are crucial for tracking real-time states during training and simulations.
  - **`game_state_log.csv`**: Records the AI’s decisions and game states during training for later analysis.
  
- **`/opponent_profiles/`**: Contains data on opponent behaviors, betting tendencies, and general statistics that allow the AI to adjust its strategy.
  - **`opponent_stats.csv`**: Aggregated statistics of opponent behavior (aggression, folding frequency, etc.).
  
- **`/training_metrics/`**: Stores metrics generated during reinforcement learning training, such as rewards, win rates, and Q-values.
  - **`training_performance.csv`**: Logs the agent's progress over episodes.

## Cross-Referencing

Each data submodule directly impacts components across the PokerAI system. Below are links to key related modules:
  
- **Reinforcement Learning Module (`rl_module/`)**: Utilizes the **`hand_history`** data and **`training_metrics`** for agent training. Learn more in the [RL Module README](../rl_module/README.md).
- **Strategy Engine (`strategy_engine/`)**: Uses **opponent profiling** and **game state logs** to refine strategic decision-making. See the [Strategy Engine README](../strategy_engine/README.md).
- **Browser Automation Module (`browser_automation/`)**: Reads real-time game state data for interaction with live poker platforms. Read the full description [here](../browser_automation/README.md).
- **NLP Chat Module (`nlp_chat/`)**: For bluffing or influencing opponents, the AI uses behavioral data from **opponent profiling**. Check the [NLP Chat README](../nlp_chat/README.md).

## Key Configurations and Their Impact

1. **Hand History Data**: Directly influences how the RL agent is trained. The accuracy and diversity of this dataset are critical for ensuring that the AI can handle a wide range of game situations.
2. **Opponent Profiles**: Real-time adjustment of AI strategy is driven by opponent tendencies, captured in this dataset. This profiling ensures that the AI can adapt to different types of opponents (aggressive, passive, etc.) during gameplay.
3. **Game State Logs**: Helps to identify trends in the AI’s decision-making, allowing developers to track its performance and optimize strategies in future updates.

## Usage Examples

1. **Training with Hand History Data**:
   To initiate training with a hand history dataset, use the following command:
   ```bash
   python rl_module/train.py --input data/hand_history/hand_history_samples.json
   ```

2. **Analyzing Opponent Profiles**:
   Run the following command to analyze opponent profiling and update strategies:
   ```bash
   python strategy_engine/analyze_opponents.py --input data/opponent_profiles/opponent_stats.csv
   ```

3. **Logging Game States**:
   The AI records in-game events in real-time, which can be viewed as follows:
   ```bash
   python rl_module/log_game_state.py --output data/game_state_logs/game_state_log.csv
   ```

## Future Enhancements

- **Data Augmentation**: Plan to generate synthetic hand histories to further train the RL agent on rare poker scenarios.
- **Advanced Opponent Profiling**: Machine learning will be integrated to create dynamic opponent profiles based on evolving behavioral patterns.
- **Multi-Platform Support**: Enable cross-platform game state logs to enhance data diversity.

---

This directory plays a foundational role in improving the PokerAI’s decision-making through structured datasets and logs that feed into the various learning and strategic components of the project.
