# Strategy Engine

The **Strategy Engine** is a critical component of PokerAI, responsible for implementing and executing poker strategies during gameplay. It combines poker theory, real-time game analysis, and learned experiences from the RL agent to make optimal decisions, such as when to bet, raise, fold, or bluff.

## Key Modules and How They Work Together

The **Strategy Engine** integrates seamlessly with other modules:
- **Reinforcement Learning Module**: Provides the AI with learned experiences. The strategy engine uses this information to enhance decision-making. (See [rl_module/README.md](../rl_module/README.md)).
- **Browser Automation**: Executes decisions made by the strategy engine on a live poker platform through Selenium. (See [browser_automation/README.md](../browser_automation/README.md)).
- **NLP Chat**: Adds conversational layers to the gameplay, allowing the AI to bluff or engage in casual conversation through chat. (See [nlp_chat/README.md](../nlp_chat/README.md)).

Each module works in tandem to help the AI adapt to real-time game states, ensuring that it plays optimally and interacts naturally with human players.

## Directory Structure

- **`/pre_flop_strategy/`**: Contains scripts and logic for decisions before the flop. This includes hand evaluation, position-based decisions, and initial aggression.
  - **Scripts**: 
    - `pre_flop_rules.py`: Evaluates pre-flop hand strength and recommends actions.
    - `pre_flop_simulations.py`: Uses simulations to determine pre-flop equity against a range of potential hands.
  
- **`/post_flop_strategy/`**: Strategies for the post-flop phase, where more information is available (e.g., community cards).
  - **Scripts**:
    - `hand_evaluation.py`: Evaluates the relative strength of the AI’s hand.
    - `pot_odds_calculator.py`: Assesses whether calling is mathematically correct based on pot odds.
  
- **`/opponent_modeling/`**: Profiles opponents based on their tendencies (e.g., aggressive, passive) and adjusts strategies accordingly.
  - **Script**: 
    - `opponent_profiling.py`: Tracks opponent tendencies and updates the AI's strategy in real time.
  
- **`/bluffing_engine/`**: Responsible for bluffing and deceptive plays to confuse opponents.
  - **Script**:
    - `bluff_probability.py`: Determines when the AI should bluff based on various factors such as hand strength and opponent tendencies.

## Detailed Documentation and Usage Examples

### Example: Using the Pre-Flop Strategy
To utilize the pre-flop strategy during gameplay, the AI evaluates its hand using **`pre_flop_rules.py`**. The hand strength and positional information are passed into the strategy engine, which returns a recommendation (e.g., raise, fold). This recommendation is sent to the **browser automation** system, which executes the decision on the poker platform.

**Command:**
```bash
python pre_flop_rules.py --hand 'AsKs' --position 'early'
```

### Example: Opponent Profiling in Action
The AI uses **`opponent_profiling.py`** to track opponents over time. Based on profiling data, the AI can adjust its strategy against specific players, such as calling more frequently against passive opponents or bluffing against aggressive ones.

**Command:**
```bash
python opponent_profiling.py --opponent_id 'player123'
```

## Real-Time Impact of Configurations

- **Hand Evaluation**: Adjusting the **`hand_evaluation.py`** parameters affects how aggressive the AI is when holding marginal hands.
- **Bluff Frequency**: Changes in **`bluff_probability.py`** influence how often the AI bluffs, adapting it to more aggressive or passive gameplay environments.
- **Opponent Modeling**: Modifying **`opponent_profiling.py`** alters the weight of past behavior when predicting future actions, making the AI more or less reactive to specific opponents.

## Future Enhancements

- **Multi-Table Strategy**: Support for multi-table gameplay where the AI must manage multiple poker tables simultaneously.
- **Advanced Opponent Profiling**: Use machine learning to dynamically classify opponents into more nuanced categories beyond just "aggressive" or "passive."
- **Strategy Evolution**: Implement a system where the AI's strategy evolves based on long-term opponent behavior across multiple sessions.

---

The **strategy_engine** module is crucial to PokerAI’s decision-making capabilities, tying together various strategic elements to allow the AI to adapt dynamically in real-time.
``` 

### Changes made:
1. **Cross-referencing**: Linked to other modules like RL, browser automation, and NLP chat in the README, showing how they all work together.
2. **Detailed Documentation**: Added examples showing how to use key scripts, such as `pre_flop_rules.py` and `opponent_profiling.py`.
3. **Extended Explanations**: Clarified the impact of configurations (like bluffing frequency and hand evaluation) on real-time gameplay.

This updated README ensures that users can understand how to use the **strategy engine** effectively, along with how it integrates into the larger PokerAI system.
