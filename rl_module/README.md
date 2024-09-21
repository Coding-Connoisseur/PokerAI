# Reinforcement Learning (RL) Module

The RL module in PokerAI handles training and decision-making using Reinforcement Learning algorithms like Q-Learning and Deep Q-Networks (DQN). This module is the heart of the AI’s learning capabilities and integrates with other components like the strategy engine and browser automation.

## Directory Structure

- **`/agents/`**: Contains implementations for different RL agents (e.g., Q-Learning, DQN).
  - **`q_learning_agent.py`**: Traditional Q-Learning agent.
  - **`dqn_agent.py`**: Agent using a neural network to approximate Q-values.
  - **`policy_gradient_agent.py`**: Alternative agent using policy gradient methods.

- **`/training/`**: Scripts and utilities to train the RL agents.
  - **`train_agent.py`**: Core script for training an agent, running episodes, collecting rewards, and updating policies.
  - **`rewards.py`**: Defines how rewards are distributed to reinforce correct actions.
  - **`exploration_strategies.py`**: Implements exploration strategies (e.g., epsilon-greedy) to balance exploration and exploitation.

- **`/environment/`**: Defines the poker environment and game state representations.
  - **`poker_environment.py`**: Simulates the poker environment for RL agents to interact with.
  - **`state_representation.py`**: Converts game states (e.g., cards, pot size) into numerical formats that RL agents can process.

- **`/evaluation/`**: Scripts to evaluate the performance of trained RL agents.
  - **`evaluate_agent.py`**: Evaluates trained agents in simulated games, logging performance metrics like win rates and cumulative rewards.
  - **`metrics_logger.py`**: Logs training metrics, helping track performance improvements over time.

### Cross-Referencing to Other Modules

This module works closely with several other components of PokerAI:

- **Strategy Engine**: The RL module receives input from the strategy engine, such as pre-flop and post-flop strategies, and uses these inputs to guide decision-making.
  - For more details, check the [strategy_engine/README.md](../strategy_engine/README.md).
  
- **Browser Automation**: Once the RL agent makes decisions, the browser automation module executes these decisions in live poker environments.
  - More details in the [browser_automation/README.md](../browser_automation/README.md).

- **NLP Chat**: The RL module can also signal strategic moments for using the GPT-based chat system, like bluffing or banter during gameplay.
  - More info in the [nlp_chat/README.md](../nlp_chat/README.md).

### Detailed Documentation: Usage Examples

#### Training an RL Agent

To train an RL agent using the `train_agent.py` script:

```bash
python train_agent.py --agent dqn --episodes 1000 --learning_rate 0.001
```

- **`--agent`**: Specifies the RL agent to train (`q_learning` or `dqn`).
- **`--episodes`**: Number of training episodes.
- **`--learning_rate`**: Learning rate for the agent’s policy updates.

Training will simulate poker games and log performance metrics, updating the agent’s Q-values or neural network weights accordingly.

#### Evaluating a Trained Agent

After training, use `evaluate_agent.py` to test the agent's performance:

```bash
python evaluate_agent.py --model path/to/model --num_games 100
```

This evaluates the model in 100 simulated games, logging key metrics like win rates, hand outcomes, and decision accuracy.

### Extended Explanations: Key Configurations

1. **Exploration Strategies**: The `exploration_strategies.py` script plays a crucial role in balancing exploration and exploitation during training. By setting the epsilon value (for epsilon-greedy strategies), the agent decides when to explore new actions versus exploiting known successful strategies.

2. **Reward Structures**: The `rewards.py` script is vital in shaping the agent’s learning behavior. Customizing the reward system (e.g., larger rewards for successful bluffs) significantly impacts the agent’s decision-making and long-term strategy optimization.

3. **State Representation**: In `state_representation.py`, game states (cards, pot size, etc.) are converted into vectors, enabling the agent to process game information efficiently. Tuning this can drastically affect the quality of the agent's decision-making.

### Future Enhancements

- **Multi-Agent Learning**: Implement multi-agent systems to simulate games where multiple AI agents play against each other, creating a more competitive training environment.
  
- **Advanced Exploration Methods**: Integrate more sophisticated exploration strategies like Upper Confidence Bound (UCB) to optimize long-term agent performance.
  
- **Real-Time Adaptation**: Add mechanisms that allow the RL agent to adapt dynamically to new poker environments or changing opponent behaviors in real-time.

---

This module provides the core learning engine for PokerAI, driving the decision-making process during gameplay by continuously improving through training.
