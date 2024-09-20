# Browser Automation Module

This directory contains scripts and tools used to automate browser interactions for online poker platforms. The browser automation enables the AI to autonomously participate in poker games by simulating user input, detecting game states, and performing real-time decision-making.

## Directory Structure

- **`/actions`**: Contains reusable browser actions such as clicking buttons, entering text, and navigating screens.
- **`/drivers`**: Browser drivers (e.g., Chrome, Firefox) used by Selenium to control the browser.
- **`/scripts`**: Selenium scripts for specific poker tasks (e.g., entering a game, placing bets, reading game states).
- **`/helpers`**: Utility functions for page element detection, waiting, and handling popups.

## Key Enhancements

### 1. **Robust Game State Detection**
Improved mechanisms for detecting on-screen elements, including fallback selectors and platform-specific optimizations, ensure accurate and reliable reading of key poker elements like cards, bets, and player actions.

### 2. **Error Handling and Recovery**
The module includes robust error handling, including retry logic and page reloads for dealing with browser crashes, disconnections, or unexpected changes in site layouts. This ensures smoother and uninterrupted gameplay.

### 3. **Multi-Table Support**
The module is scalable to allow the AI to participate in multiple poker tables simultaneously. This requires handling multiple browser windows or tabs, with each one being monitored independently.

### 4. **Real-Time Decision Making**
The browser automation communicates efficiently with the strategy engine, ensuring that decisions made by the AI (e.g., bet, raise, fold) are executed with minimal delay. This allows the AI to react promptly to fast-paced poker games.

### 5. **Automated Testing**
Integration of testing scripts to ensure that the browser automation behaves reliably across different platforms and scenarios. Automated tests cover typical interactions, edge cases, and fail-safe mechanisms.

## Usage

1. **Install Dependencies**: Install Selenium and the required browser drivers (e.g., ChromeDriver) from the project root using `pip install -r requirements.txt`.
2. **Run Scripts**: Use the provided scripts to interact with the poker platform. For example, run `python scripts/place_bet.py` to place a bet based on the AI's decision.
3. **Monitor Logs**: Review logs and screenshots generated during gameplay for debugging and performance monitoring.

---

This enhanced version improves the robustness, flexibility, and scalability of the browser automation system, making it ready for real-world poker platforms.
