# Configuration Module

This directory contains all configuration files and settings that govern how PokerAI operates. These files control aspects like reinforcement learning (RL) parameters, browser automation preferences, strategy settings, opponent profiling, and environment-specific configurations.

## Cross-Referencing Modules

The configuration settings in this directory directly affect different components of PokerAI:

- **Reinforcement Learning Module**: The parameters defined here (e.g., learning rate, exploration strategies) influence how the RL agent learns from poker games. [Learn more in the RL Module README](../rl_module/README.md).
- **Browser Automation Module**: Settings such as browser type, retries, and timeouts help manage browser interactions during live poker sessions. [More details in the Browser Automation README](../browser_automation/README.md).
- **Strategy Engine**: Configuration files like `strategy_config.yaml` directly influence how the AI handles pre-flop and post-flop decisions, bluffing, and opponent profiling. [More details in the Strategy Engine README](../strategy_engine/README.md).
- **NLP Chat Module**: Chat settings in the `chat_config.yaml` define how the AI engages in conversations, bluffing, and natural language interactions during poker games. [More details in the NLP Chat README](../nlp_chat/README.md).

## Directory Structure

- **`env_config.yaml`**: Contains environment-specific settings such as browser configurations, platform URLs, and logging levels.
- **`rl_config.yaml`**: Defines the key hyperparameters for reinforcement learning, including learning rates, discount factors, and exploration/exploitation balances.
- **`strategy_config.yaml`**: Controls poker decision-making settings like bluff frequency, hand evaluation thresholds, and opponent behavior models.
- **`browser_automation_config.yaml`**: Holds parameters for browser automation, including retries, timeouts, and supported browsers.
- **`logging_config.yaml`**: Specifies logging levels and output directories for system logs.
- **`chat_config.yaml`**: Configures chat settings for the NLP module, determining how frequently and under what conditions the AI interacts with opponents using natural language.

## Key Configuration Files and Their Impact

### 1. **env_config.yaml**
This file defines key environment parameters, ensuring the system is properly configured for both local development and deployment on live platforms. The AI adapts its behavior depending on the environment setup.

### 2. **rl_config.yaml**
This file controls the learning process of the reinforcement learning agent. The exploration rate determines how often the AI tries new strategies, while the learning rate affects how quickly the AI adapts to game outcomes. Changes here directly affect how fast the AI learns and how effectively it performs in live games.

### 3. **strategy_config.yaml**
The strategy configuration defines high-level poker strategy rules, such as when to bluff or fold based on hand strength and pot odds. This is tightly integrated with the **Strategy Engine** module, meaning adjustments here influence how aggressive or conservative the AI plays. Small tweaks can lead to large changes in the AI's playing style.

### 4. **browser_automation_config.yaml**
This file configures the browser behavior used by Selenium, ensuring smooth interactions with poker platforms. By adjusting retry limits or timeouts, you can optimize the AI’s performance across various platforms without being detected as a bot.

### 5. **chat_config.yaml**
Configures the chat behavior for bluffing and conversational interactions with opponents. The settings here define how natural the AI's responses are, contributing to its psychological strategy in poker games. It is tightly integrated with the **NLP Chat Module**.

## Usage Examples

### Example 1: Modifying RL Agent Behavior

To modify the AI's learning behavior, you can adjust parameters in `rl_config.yaml`:

```yaml
learning_rate: 0.001
gamma: 0.9
exploration_rate: 0.2
```

This increases the learning rate, which makes the AI adapt faster to game outcomes, but also increases the risk of overfitting.

### Example 2: Customizing Bluff Frequency

In `strategy_config.yaml`, you can adjust the bluff frequency:

```yaml
bluffing_frequency: 0.25
```

Setting this to `0.25` means the AI will bluff 25% of the time, which can be further customized based on the opponent profile.

### Example 3: Adjusting Browser Timeouts

In `browser_automation_config.yaml`, you can set timeouts for specific elements:

```yaml
element_timeout: 10
```

This defines the amount of time the AI will wait for a browser element to load before retrying, ensuring smoother gameplay.

## Extended Documentation

### Essential Scripts

- **`train.py`**: This script handles the training of the RL agent. The configuration files in `config/` directly influence the training process, such as exploration strategies and reward calculations. 

    Example usage:
    ```bash
    python train.py --config config/rl_config.yaml
    ```

- **`ai_poker_player.py`**: The main execution script that ties the browser automation, strategy engine, and RL components together. The settings in `browser_automation_config.yaml`, `strategy_config.yaml`, and others dictate how the AI interacts with the poker platform and opponents.

    Example usage:
    ```bash
    python ai_poker_player.py --config config/browser_automation_config.yaml
    ```

## Future Enhancements

- **Improved Opponent Profiling**: The next step is to integrate dynamic opponent profiling based on real-time game outcomes, allowing the AI to adjust to new player styles on the fly. See the opponent profiles section in the [opponent_profiles README](opponent_profiles/README.md) for further details.
- **Cross-Platform Support**: We aim to expand browser support to include Safari and Edge, which will require updates to `browser_automation_config.yaml`.

---

This configuration module provides flexibility to tune the AI’s behavior, allowing developers to customize gameplay strategies, learning processes, and interaction mechanisms for a better-performing poker-playing AI.
