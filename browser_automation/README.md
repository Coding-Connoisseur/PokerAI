# Browser Automation Module

This module automates browser-based interactions on online poker platforms, allowing the PokerAI to simulate user input, read game states, and make real-time decisions. It works in tandem with the Reinforcement Learning (RL) agent, Strategy Engine, and NLP Chat module to deliver a seamless poker-playing experience.

## Directory Structure

- **`/actions`**: Defines atomic actions the AI can take, such as clicking buttons or entering text. Each action is reusable and modular.
  - **`click_button.py`**: Simulates button clicks within the browser.
  - **`enter_text.py`**: Automates typing into input fields, like poker chat or bet boxes.
  - **`navigate.py`**: Handles page transitions, such as moving from the lobby to a table.

- **`/drivers`**: Contains browser driver executables needed for Selenium to control the browser (ChromeDriver, GeckoDriver).
  - **Example**: For Chrome:
    ```bash
    python -m webdriver_manager.chrome
    ```
    Reference: [WebDriver Manager Documentation](https://github.com/SergeyPirogov/webdriver_manager)

- **`/scripts`**: Contains Selenium scripts that perform complex actions, such as joining games or placing bets.
  - **`enter_game.py`**: Automates table selection and joining.
  - **`place_bet.py`**: Reads AI’s decisions from the strategy engine and places corresponding bets.
  - **`read_game_state.py`**: Scrapes in-game data (cards, pot size, opponent actions) and passes it to the RL agent.

- **`/helpers`**: Contains utility scripts for error handling and logging.
  - **`wait_for_element.py`**: Pauses execution until a specific web element is visible.
  - **`handle_popups.py`**: Detects and dismisses popups to avoid interruptions during gameplay.

## Key Features and Enhancements

### 1. **Integration with Strategy Engine and RL Agent**
- **Strategy Engine**: Provides decision logic for actions (e.g., betting, folding) based on game state and opponent profiling. See [Strategy Engine README](../strategy_engine/README.md) for details.
- **Reinforcement Learning**: Ensures decisions made by the AI are data-driven and adaptive over time. Learn more in the [RL Module README](../rl_module/README.md).

### 2. **Error Handling and Recovery**
If an error occurs (e.g., browser crash), the module retries the action, reloads the page, or restarts the game session. This ensures robustness in real-time gameplay.

### 3. **Multi-Table Support**
New multi-table functionality allows PokerAI to handle several tables at once, with each session managed in a separate browser window.

### 4. **Automated Testing**
Automated tests verify browser interactions, from joining a game to handling complex in-game scenarios. See the [Tests README](../tests/README.md) for more information on test coverage.

### 5. **Real-Time Decision Making**
Interacts closely with the Strategy Engine and RL agent, ensuring decisions such as bluffing, folding, or raising are executed instantly based on the game state.

## Usage Examples

### Start a Poker Session:
To begin a poker session, where the AI automates table entry and decision-making, run the following:

```bash
python scripts/enter_game.py
```

### Place a Bet:
Once the AI has evaluated its hand strength and decided on a bet:

```bash
python scripts/place_bet.py
```

### Read Game State:
To capture and log the current poker game state (cards, pot size, player actions):

```bash
python scripts/read_game_state.py
```

## Cross-Referencing Other Modules
- **Reinforcement Learning Module**: For how the AI learns and adapts its strategy, refer to the [RL Module README](../rl_module/README.md).
- **NLP Chat Module**: Learn how the AI engages in human-like poker chat interactions in the [NLP Chat README](../nlp_chat/README.md).
- **Strategy Engine**: Detailed strategy logic, including bluffing and pot odds calculation, is covered in the [Strategy Engine README](../strategy_engine/README.md).

## Future Enhancements

- **Advanced Game State Detection**: Using machine learning for image recognition to improve element detection accuracy on dynamic poker platforms.
- **Cross-Browser Compatibility**: Expand to support more browsers like Edge or Safari to increase flexibility.
- **Mobile Browser Support**: Adding support for mobile poker platforms through browser emulation.

---

The **browser_automation** module is vital for enabling PokerAI to interact with live poker platforms, ensuring it functions autonomously in real-time environments while seamlessly integrating with other key components of the system.
