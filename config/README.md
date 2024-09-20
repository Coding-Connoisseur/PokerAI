# Configuration Module

This directory contains all configuration files and settings required for running the PokerAI project. These files define parameters for reinforcement learning, browser automation, poker strategy settings, and other environment-specific configurations. The structure ensures that the PokerAI can easily be customized, extended, and deployed in different environments or for different poker platforms.

## Directory Structure

- **`env_config.yaml`**: This is the primary environment configuration file. It contains settings related to the environment in which the PokerAI operates, such as the browser choice, platform URLs, and file paths. It also holds general system parameters, such as logging preferences.
  
- **`rl_config.yaml`**: This file defines the hyperparameters for the reinforcement learning (RL) agent. Key parameters include:
  - **Learning Rate**: Controls how much the agent learns from new experiences.
  - **Discount Factor (Gamma)**: Determines how much future rewards are prioritized over immediate rewards.
  - **Exploration Rate**: Governs the balance between exploration and exploitation during training.
  - **Episode Length**: Sets the number of steps per game episode during training.
  - **Reward Structure**: Describes how rewards are distributed based on game outcomes.

- **`strategy_config.yaml`**: This configuration file specifies parameters for the poker strategy engine. It includes:
  - **Pre-flop Strategy**: Parameters for the decisions made before the flop (e.g., raising or folding with certain hands).
  - **Bluffing Frequency**: Defines how often the AI is allowed to bluff.
  - **Opponent Profiling**: Contains thresholds for categorizing opponents as aggressive, passive, or neutral, based on their playing patterns.
  - **Pot Odds Calculation**: Settings that control how the AI evaluates whether to continue in a hand based on the current pot odds.

- **`browser_automation_config.yaml`**: This file contains settings that control browser automation:
  - **Browser Type**: Defines which browser (e.g., Chrome, Firefox) is used for automation.
  - **Max Retries**: Specifies how many times an action should be retried if an error occurs during browser interaction.
  - **Timeout Settings**: Timeout thresholds for waiting for elements or actions on the poker platform.

- **`logging_config.yaml`**: This configuration file handles the logging behavior of the entire project. It defines:
  - **Log Levels**: Sets different logging levels (DEBUG, INFO, ERROR) for various components (e.g., RL agent, browser automation).
  - **Log File Paths**: Specifies where the log files should be stored.
  - **Rotation Policy**: Determines how logs are rotated and archived (e.g., daily, weekly).

- **`chat_config.yaml`**: Defines settings for the NLP-based chat functionality, including:
  - **Conversation Templates**: A list of pre-defined chat responses that the AI can use for bluffing or friendly banter.
  - **Response Delay**: The time delay between AI responses, to mimic human interaction.
  - **Language Model Settings**: Parameters for tuning the GPT model used for generating chat responses, such as temperature and max tokens.

## How to Use the Configurations

1. **Modify Parameters**: Update any of the YAML files to fine-tune the behavior of the AI, reinforcement learning, or browser automation to suit specific requirements.
2. **Environment-Specific Config**: `env_config.yaml` should be tailored for the specific poker platform or local environment where the AI will run.
3. **RL Tuning**: Adjust `rl_config.yaml` based on the results from training sessions to improve the AI’s decision-making process.
4. **Logging**: Use `logging_config.yaml` to control the level of verbosity for debugging and monitoring.

---

Each configuration file provides flexibility in controlling and customizing the PokerAI’s behavior for both development and deployment scenarios.
```
