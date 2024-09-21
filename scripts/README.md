# Scripts Directory

This directory contains essential utility scripts for setting up, training, and running the PokerAI. The scripts streamline tasks such as installation, environment setup, reinforcement learning training, and simulation execution. Additionally, it provides integration across the various modules of the project, including the **Strategy Engine**, **Reinforcement Learning (RL) Module**, **Browser Automation**, and **NLP Chat**.

## Directory Structure

- **`install_dependencies.sh`**: Installs required Python libraries and system dependencies.
  - **Usage**: Run `bash install_dependencies.sh` to install all required dependencies listed in `requirements.txt`.
  - **Components Used**: This script sets up everything from **Reinforcement Learning** to **NLP** and **Browser Automation**, linking the various systems.

- **`setup_environment.py`**: Prepares the necessary environment for the PokerAI, creating configuration files and directories needed by various components.
  - **Usage**: Run `python setup_environment.py` to set up all required directories and configurations.
  - **Submodule Interaction**: Links to configuration files under the **`config`** folder, especially important for configuring **opponent profiling**.

- **`run_training.sh`**: Automates the training process for the RL agent by interacting with the **RL module** and running episodes in a simulated environment.
  - **Usage**: Run `bash run_training.sh` to start training the agent using the configuration specified in `rl_config.yaml`.
  - **Integration**: Utilizes **`rl_module`** and **`strategy_engine`**. Reference the **`rl_module/README.md`** for RL configuration details.

- **`process_hand_histories.py`**: Parses poker hand histories for analysis and training.
  - **Usage**: Run `python process_hand_histories.py --input <file_path>` to process raw hand histories into a usable format for analysis and training.
  - **Impact**: Provides essential data to both the **strategy engine** and **RL module** for refining strategies and improving decision-making based on past performance.

- **`run_simulation.py`**: Executes a simulated poker game using the RL agent and strategy engine, providing real-time decision-making and interaction with a poker environment.
  - **Usage**: Run `python run_simulation.py --agent <agent_type>` to simulate poker games and assess the agent's performance.
  - **Key Interactions**: Pulls decision-making logic from the **strategy engine** and uses the trained RL agent to simulate real-time poker play.

- **`backup_logs.sh`**: Backs up training and gameplay logs to ensure critical data is not lost.
  - **Usage**: Run `bash backup_logs.sh` to copy and archive log files.
  - **Real-Time Impact**: Critical for tracking the performance of various submodules (e.g., RL training logs, game outcomes).

- **`evaluate_model.py`**: Evaluates the performance of trained RL models in a simulated or real environment by running test cases.
  - **Usage**: Run `python evaluate_model.py --model <model_path>` to assess a trained model’s performance.
  - **Submodule Interactions**: References the **`rl_module`** for evaluation configurations and metrics logging. This script can also be tied to **`strategy_engine`** for testing strategic refinements.

## Cross-Module Functionality

Each script interacts with one or more submodules. Below are key references for how these scripts integrate into the larger project:
- **Reinforcement Learning**: The **`run_training.sh`**, **`evaluate_model.py`**, and **`run_simulation.py`** scripts directly engage with the **RL module** for training and evaluation. Refer to [rl_module/README.md](../rl_module/README.md) for more details.
- **Strategy Engine**: Decision-making relies on the **Strategy Engine**, which processes data from **hand histories** and applies strategies during simulations. Learn more from [strategy_engine/README.md](../strategy_engine/README.md).
- **Browser Automation**: If you're running the AI on a live platform, scripts like **`run_simulation.py`** will also interface with the **browser_automation** module to perform real-time actions. See [browser_automation/README.md](../browser_automation/README.md).
- **NLP Chat**: When simulating interactions that require human-like communication, the **NLP Chat** engine is used in conjunction with **run_simulation.py**. Refer to [nlp_chat/README.md](../nlp_chat/README.md).

## Usage Examples

1. **Installing Dependencies**:
   ```bash
   bash install_dependencies.sh
   ```

2. **Setting Up the Environment**:
   ```bash
   python setup_environment.py
   ```

3. **Training the RL Agent**:
   ```bash
   bash run_training.sh
   ```

4. **Running a Simulation**:
   ```bash
   python run_simulation.py --agent DQN
   ```

5. **Evaluating a Trained Model**:
   ```bash
   python evaluate_model.py --model models/dqn_model.pth
   ```

## Future Enhancements

- **Automatic Multi-Agent Support**: Modify `run_simulation.py` to support multiple agents, simulating multiplayer poker games.
- **Extended Profiling and Testing**: Integrate automated profiling scripts that measure model performance against specific opponent types from the **opponent_profiles** module.

---

This directory provides the core scripts required to integrate and automate various components of the PokerAI project, allowing seamless training, simulation, and deployment.
```

### Key Changes:
1. **Cross-Referencing**:
   - Added clear links to other modules like **RL**, **Strategy Engine**, **NLP Chat**, and **Browser Automation**.
   - Provided direct references to related README files for more context.
   
2. **Detailed Documentation**:
   - Explained each script in more detail, including how they interact with the submodules and where to find more configuration information.

3. **Extended Explanations**:
   - Provided more information about configurations, particularly for scripts like `run_training.sh`, `process_hand_histories.py`, and `evaluate_model.py`, which are critical for the system's performance.

These improvements should make the `scripts` directory much clearer and better integrated with the rest of the project.
