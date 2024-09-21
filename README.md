# PokerAI

## Project Overview

PokerAI is an advanced system designed to autonomously play poker using a combination of components that work together to optimize decision-making:

- **Reinforcement Learning (RL)**: The RL agent trains by playing simulated poker games, learning the best strategies through rewards and penalties.
- **Strategy Engine**: This engine integrates game theory and real-time game state evaluations (e.g., hand strength, pot odds) to guide decision-making.
- **Browser Automation**: Uses Selenium to interact with live poker platforms, allowing the AI to play online games in real-time.
- **NLP Chat**: An optional feature powered by GPT to engage in human-like conversations, adding psychological tactics such as bluffing via chat.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Coding-Connoisseur/PokerAI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PokerAI
   ```
3. Run the setup script to install necessary dependencies:
   ```bash
   bash install_dependencies.sh
   ```
4. Configure the environment:
   ```bash
   python setup_environment.py
   ```
5. Ensure the correct browser drivers (e.g., ChromeDriver, GeckoDriver) are in place under `browser_automation/drivers`.

## Running PokerAI

1. **RL Training**: Train the reinforcement learning agent by running:
   ```bash
   python rl_module/train_agent.py
   ```
   - Configure training parameters in `config/rl_config.yaml`.

2. **Simulating Games**: To simulate games and evaluate agent performance:
   ```bash
   python rl_module/run_simulation.py --agent <agent_type>
   ```

3. **Real-Time Play (Browser Automation)**: Start the AI playing on a live poker platform:
   ```bash
   python browser_automation/start_game.py
   ```
   - The AI will interact with the platform, making moves based on the strategy engine.

4. **NLP Chat (Optional)**: Enable AI chat interactions:
   ```bash
   python nlp_chat/engage_chat.py
   ```

