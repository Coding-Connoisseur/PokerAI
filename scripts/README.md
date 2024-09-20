# Scripts Directory

The `scripts` directory contains utility scripts and automation tools to simplify the setup, execution, and maintenance of the PokerAI project. These scripts handle tasks such as installation, environment setup, data processing, and running simulations. The directory is structured to help users quickly get the AI up and running, train models, and automate repetitive tasks during the development and deployment process.

## Directory Structure

- **`install_dependencies.sh`**: A shell script for setting up the necessary dependencies for the PokerAI project. It automates the installation of required Python packages (via `pip`), system libraries, and other tools needed to run the project.
  - **Purpose**: This script ensures that all required software, libraries, and tools are installed with the correct versions, avoiding environment-related issues.
  - **How to Use**: Run `bash install_dependencies.sh` from the terminal to install all dependencies.

- **`setup_environment.py`**: A Python script that helps configure the environment needed to run PokerAI. This includes setting up directories, creating configuration files, and initializing default data files.
  - **Purpose**: To automate the process of preparing the environment for development or production use, making it easier to switch between environments.
  - **How to Use**: Run `python setup_environment.py` to automatically set up the environment.

- **`run_training.sh`**: A shell script designed to automate the process of training the reinforcement learning agents. It calls the necessary Python training scripts, passing along any relevant parameters like the agent type, number of episodes, or exploration strategies.
  - **Purpose**: To simplify the execution of RL training runs, allowing users to quickly start training their agents without having to manually configure each run.
  - **How to Use**: Run `bash run_training.sh` to initiate the training process with default or custom settings.

- **`process_hand_histories.py`**: A Python script for parsing and processing raw poker hand history files. It cleans, structures, and prepares the data for analysis or input into the RL training module.
  - **Purpose**: To transform raw hand history data into a format suitable for training the AI or performing statistical analysis.
  - **How to Use**: Run `python process_hand_histories.py --input <file_path>` to process hand history data.

- **`run_simulation.py`**: This script runs a simulation of poker games using the trained RL agents. It sets up simulated games between AI players (or against human opponents) and logs the outcomes for analysis.
  - **Purpose**: To test the performance of the AI agents in simulated poker games and evaluate their strategies under different conditions.
  - **How to Use**: Run `python run_simulation.py --agent <agent_type>` to start a poker simulation.

- **`backup_logs.sh`**: A utility script to backup the logs generated during training, evaluation, and simulations. It copies log files to a backup directory, compressing them if needed.
  - **Purpose**: To ensure that logs from critical training and evaluation phases are not lost, providing a history of the AI’s progress.
  - **How to Use**: Run `bash backup_logs.sh` to back up the logs.

- **`evaluate_model.py`**: A Python script that runs an evaluation of the trained models against a test dataset or in simulated games. It generates key performance metrics such as win rate, average reward, and decision accuracy.
  - **Purpose**: To assess the performance of trained models and ensure they meet desired criteria before deployment.
  - **How to Use**: Run `python evaluate_model.py --model <model_path>` to evaluate a model.

## Key Usage Scenarios

1. **Setup and Installation**: 
   - Run `install_dependencies.sh` to set up the environment.
   - Run `setup_environment.py` to configure the environment for development or deployment.

2. **Training AI Models**: 
   - Use `run_training.sh` to automate and customize training sessions for RL agents.
   
3. **Data Processing**: 
   - Run `process_hand_histories.py` to clean and prepare hand history data for training or analysis.

4. **Simulations and Testing**: 
   - Use `run_simulation.py` to simulate poker games with AI agents.
   - Run `evaluate_model.py` to assess model performance.

5. **Backup and Maintenance**: 
   - Use `backup_logs.sh` to regularly back up critical log data from training and simulation runs.

---

This directory provides essential scripts for automation, training, and evaluation, enabling smooth development and operational workflows for the PokerAI project.

