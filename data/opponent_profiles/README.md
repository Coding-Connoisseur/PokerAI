### Opponent Profiles Configuration

The **`config/opponent_profiles/`** directory is designed to store data and configuration files that help PokerAI profile and predict the behavior of opponents. Opponent profiling plays a critical role in determining the AI’s strategy by analyzing patterns in how players behave over time. The AI uses this information to adapt its play, exploiting weaknesses and adjusting its strategies to different playstyles.

## Directory Structure

- **`profiles.yaml`**: The main configuration file that defines opponent categories and the corresponding actions the AI should take. This file stores predefined profiles based on historical data and categorizes players into types such as "Aggressive," "Passive," "Tight," and "Loose."
  
- **`historical_data/`**: This folder contains datasets and logs of past hands played by opponents. The AI uses this data to build accurate models of each opponent's tendencies.
  - **`opponent_hand_history.json`**: Stores a log of previous hands played by each opponent. It includes information like bet sizes, frequencies of bluffs, and fold percentages.
  - **`opponent_stats.csv`**: Aggregates statistical information such as win rates, average bet sizes, and aggression frequency for each opponent.

- **`behavioral_patterns/`**: Contains behavior models that predict how an opponent will act in different situations.
  - **`bluff_detection_model.py`**: A machine learning model that predicts the likelihood of an opponent bluffing based on observed game data.
  - **`betting_pattern_analyzer.py`**: Analyzes patterns in opponent betting behaviors to classify them as aggressive, defensive, etc.

- **`adaptive_strategy.yaml`**: A configuration file that defines how the AI should adjust its strategy based on opponent profiling data. For example, it specifies how the AI should behave against an "Aggressive" player by tightening its own play or calling more bluffs.

## Key Components and Usage

### 1. **Opponent Categorization (`profiles.yaml`)**
This file contains high-level profiles of common poker player types, which guide the AI in its decisions. Profiles include:
- **Aggressive**: Players who frequently raise and bluff. The AI counters by calling more often and avoiding traps.
- **Passive**: Players who rarely raise and often fold. The AI can exploit this by betting aggressively and taking control of the hand.
- **Loose**: Players who play many hands regardless of strength. The AI focuses on making stronger hands before engaging.
- **Tight**: Players who fold frequently and only play strong hands. The AI adapts by bluffing more and calling with weaker hands.

Each category in the `profiles.yaml` file includes actions the AI should take, such as bluffing more or tightening its play based on the opponent's tendencies.

### 2. **Historical Data Collection (`historical_data/`)**
Historical data is essential for profiling opponents accurately. This folder contains logs of previous hands played by each opponent, including:
- **Hand History**: Each hand’s context, including cards dealt, bets made, and final outcomes.
- **Aggregate Statistics**: Opponent-specific data, such as how often they bluff, fold, or bet big. This data is updated in real-time during gameplay.

The AI uses this information to continuously improve its opponent models and refine its strategies.

### 3. **Behavioral Pattern Recognition (`behavioral_patterns/`)**
This folder contains the core logic for detecting and analyzing opponent behavior patterns.
- **Bluff Detection**: A machine learning model predicts bluffing patterns by looking at historical bluff frequencies, bet sizes, and other contextual factors.
- **Betting Patterns**: Analyzes an opponent’s betting style over time, categorizing them into patterns like aggressive, defensive, or erratic.

These models help the AI anticipate an opponent’s future actions based on previous behavior, allowing it to adjust its strategy dynamically.

### 4. **Adaptive Strategy (`adaptive_strategy.yaml`)**
This file defines how the AI should adjust its overall strategy based on opponent profiles. For each type of opponent (Aggressive, Passive, etc.), it contains rules for adjusting:
- **Bluffing Frequency**: How often the AI should bluff against a particular type of opponent.
- **Bet Sizing**: Adjusting bet sizes to maximize value or induce folds, depending on the opponent’s tendencies.
- **Defensive Plays**: Adapting defensive strategies such as folding more frequently against tight players or calling more often against aggressive bluffs.

### 5. **Real-Time Updates and Adaptation**
During gameplay, the AI continuously updates its opponent models based on real-time observations. For example:
- If an opponent deviates from their usual style (e.g., a passive player suddenly becomes aggressive), the AI recalibrates its profile to reflect this change.
- Data is logged after every hand, ensuring the AI stays up to date with the latest behavior patterns.

## How to Use

1. **Initialization**: Ensure the opponent profiling system is activated by including references to `profiles.yaml` and `adaptive_strategy.yaml` in the main PokerAI configuration files.
2. **Profile Update**: As the AI encounters new opponents, it updates `historical_data/` with fresh hand history logs and recalculates key stats in real time.
3. **Behavior Analysis**: The AI actively analyzes betting patterns using scripts in `behavioral_patterns/`, helping it recognize when an opponent is likely bluffing or playing conservatively.
4. **Dynamic Adaptation**: During gameplay, the AI continuously adapts its strategy based on `adaptive_strategy.yaml` and the latest opponent profiling data.

## Future Enhancements

- **Deeper Learning Models**: Introduce deep learning-based models to detect more subtle patterns in opponent behavior, such as timing and bet sizing tells.
- **Opponent Collaboration Detection**: Develop algorithms to detect potential collaboration between multiple opponents in the game (collusion detection).
- **Automated Data Labeling**: Automatically label historical hands with relevant patterns (e.g., bluffs, tight plays) to improve machine learning model training.
- **Cross-Platform Profiles**: Implement features that allow the AI to carry over opponent profiles between different poker platforms.

---

The **opponent_profiles** module is a key component in helping the PokerAI adapt dynamically to its opponents, improving its long-term win rate by learning and exploiting behavioral tendencies over time.
