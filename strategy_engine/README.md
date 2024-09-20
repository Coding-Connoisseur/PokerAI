# Strategy Engine

The `strategy_engine` directory is the core decision-making component of the PokerAI system. This module is responsible for implementing and executing poker strategies during gameplay. The strategies are based on poker theory, real-time game analysis, and the AI's learned experiences. The strategy engine interacts with the reinforcement learning module and game environment to make optimal decisions, such as when to bet, raise, fold, or bluff.

## Directory Structure

- **`/pre_flop_strategy/`**: Contains strategies specifically designed for the pre-flop phase of poker. Pre-flop decisions are based on hand strength, position, and opponent behavior. 
  - **`pre_flop_rules.py`**: Implements a rules-based system that evaluates hand strength in relation to position and recommends an action (e.g., raise, fold, or call).
  - **`pre_flop_simulations.py`**: Uses Monte Carlo simulations to evaluate the equity of the AI's hand versus potential ranges of opponent hands.

- **`/post_flop_strategy/`**: This folder holds strategies for decisions after the flop. The post-flop phase is more complex as more information (community cards) is available.
  - **`hand_evaluation.py`**: A script that assesses the relative strength of the AI's hand based on the community cards, current pot odds, and opponents' actions.
  - **`pot_odds_calculator.py`**: Calculates pot odds to help the AI decide whether to continue in the hand based on the bet size and the potential reward.
  - **`bluff_detection.py`**: A component that analyzes opponents’ actions to detect potential bluffs and adjust the strategy accordingly.

- **`/opponent_modeling/`**: This folder holds scripts that allow the AI to build models of its opponents. It uses historical data and real-time observations to adjust strategies based on opponent tendencies.
  - **`opponent_profiling.py`**: Assigns profiles to opponents (e.g., aggressive, passive) based on their actions over time.
  - **`exploitative_strategy.py`**: Adapts the AI’s strategy to exploit specific weaknesses in opponent play styles.

- **`/bluffing_engine/`**: This component handles the bluffing logic of the AI. Bluffing is a key strategic element in poker, and this module ensures that the AI executes bluffs at optimal moments to confuse opponents.
  - **`bluff_probability.py`**: Determines the likelihood that the AI should bluff, based on factors such as hand strength, opponent behavior, and pot size.
  - **`deceptive_play.py`**: Adds deceptive actions to the AI’s gameplay, such as slow-playing a strong hand to induce a bluff from opponents.

- **`/equity_calculators/`**: This folder contains various calculators used to determine hand equity in real-time.
  - **`equity_vs_range.py`**: Computes the equity of the AI’s hand versus a range of potential hands held by opponents, helping to guide decision-making.
  - **`run_out_simulations.py`**: Simulates possible outcomes based on remaining community cards to assess the chance of winning the hand.

- **`/decision_logic/`**: The heart of the strategy engine, this contains scripts that make final decisions based on all available inputs (hand strength, pot odds, opponent modeling, etc.).
  - **`decision_maker.py`**: Integrates all data points and selects the optimal action for the current game state.
  - **`adaptive_strategy.py`**: Continuously updates the AI’s decision-making strategy in real-time based on feedback from game results and opponent actions.

## Key Components

### 1. **Pre-Flop and Post-Flop Strategies**
The engine separates pre-flop and post-flop strategies to tailor decision-making to the specific stage of the game. Pre-flop decisions focus on initial hand strength, while post-flop strategy evaluates the AI’s hand strength relative to community cards and betting patterns.

### 2. **Opponent Profiling**
Opponent modeling is a vital component that allows the AI to adjust its strategy based on the behavior of other players at the table. This includes profiling their tendencies (e.g., aggressive vs. passive) and making exploitative decisions based on their weaknesses.

### 3. **Bluffing Engine**
Bluffing is a key aspect of poker strategy. The bluffing engine helps the AI balance when to bluff and when to play straightforwardly. It also uses deceptive strategies like slow-playing strong hands.

### 4. **Equity Calculators**
Hand equity, which represents the likelihood of winning a hand at a given point, is constantly calculated using real-time data. The AI uses this to make mathematically sound decisions.

### 5. **Adaptive Decision Logic**
The decision logic combines all strategic inputs (hand strength, opponent models, pot odds, etc.) to make real-time decisions during a poker game. This logic continuously adapts as the game evolves and new information is available.

## Usage

1. **Configure Strategy Settings**: Use the available scripts in the pre-flop and post-flop strategy directories to fine-tune the AI's decisions based on your preferences or testing results.
2. **Opponent Modeling**: Enhance the AI’s ability to predict opponent actions by improving the profiling system in `opponent_modeling/`.
3. **Run Equity Calculations**: Use the `equity_calculators/` scripts to continuously compute hand equity and adjust decisions dynamically during gameplay.
4. **Bluffing**: Enable the bluffing engine by setting parameters in `bluffing_engine/` to control the frequency and conditions under which the AI bluffs.

## Future Enhancements

- **Advanced Opponent Modeling**: Introduce more complex machine learning models for opponent behavior prediction, beyond rule-based profiling.
- **Multi-Agent Strategy**: Expand the strategy engine to handle multi-agent scenarios, where multiple AI opponents play against each other, creating a more competitive learning environment.
- **Dynamic Bluffing**: Implement more sophisticated bluffing algorithms that learn from opponents’ reactions to the AI’s bluffs over time.

---

The strategy engine is a dynamic and adaptable system that enables the AI to make optimal decisions during poker gameplay, combining mathematical calculations with psychological tactics like bluffing and opponent exploitation.

