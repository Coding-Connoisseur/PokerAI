### Project Overview

**PokerAI** integrates several key components to create an autonomous poker-playing AI:
- **Reinforcement Learning (RL)**: Trains the AI to make optimal decisions using either Q-Learning or Deep Q-Networks (DQN), allowing it to improve with each game.
- **Strategy Engine**: Provides pre-flop, post-flop, and bluffing strategies based on poker theory and opponent profiling. This ensures the AI adapts to different opponents dynamically.
- **Browser Automation**: Uses Selenium to interact with real poker platforms by simulating clicks, bets, and navigation.
- **NLP Chat**: Employs GPT-based natural language processing to generate conversational chat responses, making the AI more human-like during play.

These components work together to allow the AI to play poker in real time, adapting strategies based on live data, opponent behavior, and learned experiences.

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Coding-Connoisseur/PokerAI.git
   cd PokerAI
   ```

2. Install dependencies by running the following script:
   ```bash
   bash install_dependencies.sh
   ```

3. Set up the environment by running:
   ```bash
   python setup_environment.py
   ```

4. Ensure you have the correct browser drivers (e.g., ChromeDriver) in the `/drivers` directory.

---

### Running PokerAI

1. **Training the RL Agent**:
   - Configure the RL hyperparameters in `config/rl_config.yaml`.
   - Train the agent by running:
     ```bash
     python rl_module/train_agent.py
     ```

2. **Simulating Poker Games**:
   - To run a poker game simulation and test the AI’s decision-making, execute:
     ```bash
     python run_simulation.py
     ```

3. **Real-Time Gameplay**:
   - Ensure browser automation is configured in `config/browser_automation_config.yaml`.
   - Run real-time poker using browser automation:
     ```bash
     python browser_automation/scripts/enter_game.py
     ```

4. **NLP Chat**:
   - Enable the NLP chat module by configuring `config/chat_config.yaml` and integrating it with the main poker game.

5. **Monitoring Performance**:
   - Use logging tools in `rl_module/metrics_logger.py` to track training and in-game performance.

