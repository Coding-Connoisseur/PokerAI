# Browser Automation Scripts

This directory contains higher-level browser automation scripts designed to handle complex interactions with online poker platforms. These scripts automate key poker actions such as joining a game, placing bets, reading game states, and more. The automation leverages the actions and helpers from other directories and ties them into real-world poker gameplay scenarios. These scripts ensure seamless interaction between the PokerAI and the poker platform, enabling fully autonomous gameplay.

## Directory Structure

- **`enter_game.py`**: Automates the process of selecting and joining a poker table. The script navigates to the game lobby, selects the appropriate game type (e.g., cash game, tournament), and confirms participation.
  - **Features**:
    - Navigates to the poker game lobby.
    - Selects a game based on predefined parameters (e.g., stakes, number of players).
    - Automates the confirmation process to join the selected table.
    - Handles errors related to table availability and retries if necessary.

- **`place_bet.py`**: Simulates the placement of a bet, taking inputs from the AI’s decision-making module. It interacts with the platform’s bet buttons or manually enters the bet size when needed.
  - **Features**:
    - Detects the current game state (e.g., bet size, pot size).
    - Places a bet, calls, raises, or folds based on input from the strategy engine.
    - Supports customizable bet sizes for more precise control.
    - Monitors successful bet placements and verifies game state updates.

- **`read_game_state.py`**: Scrapes the poker platform to extract the current game state, including the AI’s hand, community cards, opponent actions, pot size, and player positions. This data is used by the strategy engine to make decisions.
  - **Features**:
    - Reads player hand information.
    - Extracts community cards from the game interface.
    - Tracks opponent actions and bet sizes.
    - Calculates the current pot size and other game variables.

- **`handle_timeout.py`**: Manages time-sensitive actions, ensuring the AI makes decisions and completes actions within the platform’s time constraints. It monitors the countdown timer for each action and ensures the AI submits its action before the timer expires.
  - **Features**:
    - Monitors the action timer and warns if the time is about to expire.
    - Forces quick decision-making when time is running out.
    - Optionally triggers emergency actions (e.g., folding) if time runs out.

- **`multi_table_support.py`**: A specialized script that allows the AI to play on multiple tables simultaneously. This script opens and manages multiple browser tabs or windows, ensuring that the AI tracks and interacts with each table independently.
  - **Features**:
    - Opens multiple browser tabs/windows for each poker table.
    - Tracks the game state of each table in real-time.
    - Executes the AI’s decisions on each table independently.
    - Manages focus switching between active tables to ensure smooth gameplay.

## Key Features

### 1. **Real-Time Interaction**
The scripts are designed to automate real-time poker actions. They ensure that the AI makes decisions within the platform's time limits and interacts with the game just like a human player would.

### 2. **Seamless Integration with Strategy Engine**
These scripts communicate directly with the strategy engine, executing actions based on the AI’s decisions. Whether it’s betting, folding, or joining a table, every action is driven by the AI’s game logic.

### 3. **Error Handling and Recovery**
Each script has built-in error handling mechanisms to ensure robustness. For example, if the AI encounters an error while joining a table, it will retry the process, ensuring that the game progresses without human intervention.

### 4. **Multi-Table Play**
The `multi_table_support.py` script adds the ability to play multiple poker games simultaneously. It ensures that each game is tracked and managed independently, maximizing the AI’s efficiency and increasing the complexity of the gameplay.

### 5. **Cross-Browser Compatibility**
These scripts are designed to work across multiple browsers (Chrome, Firefox, etc.) and support headless mode for efficient performance in server-based deployments.

## Usage

1. **Setup**: Ensure that all browser drivers are installed and located in the `/drivers` directory. Configure the browser settings in `browser_automation_config.yaml` to specify which browser to use.
   
2. **Running Scripts**:
   - To join a game:
     ```bash
     python enter_game.py
     ```
   - To place a bet:
     ```bash
     python place_bet.py --bet_size 100
     ```
   - To read the current game state:
     ```bash
     python read_game_state.py
     ```

3. **Multi-Table Play**:
   - To enable multi-table play, configure the script to open multiple tabs:
     ```bash
     python multi_table_support.py --tables 3
     ```

4. **Monitor and Debug**:
   - Use the logs and screenshots generated by the helper scripts to monitor and debug browser automation issues.

## Future Enhancements

- **AI-Based UI Detection**: Introducing AI-based element detection to further improve the robustness of detecting complex or dynamically changing UI elements.
- **Advanced Game Flow Control**: Adding more advanced game flow control mechanisms to anticipate and handle rare or complex situations, such as unexpected disconnections.
- **Adaptive Multi-Table Management**: Enhancing multi-table support to dynamically adjust focus and prioritize tables where the AI’s action is needed urgently.
- **Voice Command Integration**: Exploring the possibility of voice command integration to allow more interactive control of the browser automation.

---

This directory is essential for translating the PokerAI’s decisions into real-time interactions with online poker platforms. The scripts are designed for high performance, flexibility, and robustness, ensuring a smooth experience in real-world gameplay scenarios.
