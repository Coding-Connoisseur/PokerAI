# Browser Automation Module

This directory contains scripts and tools used to automate browser interactions for online poker platforms. The browser automation is built to allow the AI to autonomously play poker on live platforms by simulating user input, tracking game states, and performing decision-making based on game events.

## Directory Structure

- **`/actions`**: This folder contains predefined browser actions, such as clicking buttons, entering values, or navigating between different screens. Actions are modular and reusable across various poker platforms.
  - **`click_button.py`**: Script to simulate a button click event. 
  - **`enter_text.py`**: Automates text input for chat boxes or form fields.
  - **`navigate.py`**: Handles navigation between different screens (e.g., game lobby to the table).

- **`/drivers`**: Browser drivers, typically for Chrome or Firefox, used by Selenium to control the browser.
  - **`chrome_driver.exe`**: The Chrome browser driver executable.
  - **`firefox_driver.exe`**: The Firefox browser driver executable.
  
- **`/scripts`**: Contains Selenium scripts used to perform specific poker-related tasks, such as entering a game or placing a bet.
  - **`enter_game.py`**: Automates the process of joining a poker table, selecting stakes, and confirming participation.
  - **`place_bet.py`**: Script that simulates placing a bet based on the AI's decision-making.
  - **`read_game_state.py`**: Tracks the state of the poker game (e.g., player hands, pot size) by reading elements on the screen.

- **`/helpers`**: Utility functions to assist with common browser automation tasks like waiting for page loads, taking screenshots, and handling browser popups.
  - **`wait_for_element.py`**: Contains functions to wait until a specific element (e.g., a button) is clickable or visible.
  - **`take_screenshot.py`**: Captures screenshots of the game for debugging or state tracking purposes.
  - **`handle_popups.py`**: Detects and dismisses popups or ads that might interrupt the gameplay.

## Main Components

### 1. **Game Automation**
The core of this module automates the poker game. It performs tasks such as joining games, placing bets, folding, and leaving tables. It reads game states and passes information to the AI for decision-making.

- **Join Table**: Automates the process of navigating to the poker site, selecting a game, and sitting at a table.
- **Place Bet**: Based on the decision from the strategy engine, it triggers actions like checking, raising, or folding in the game.
- **Read Game State**: Uses Selenium to scrape on-screen data, such as the cards dealt, the pot size, and player actions. This data is passed to the AI for processing.

### 2. **Error Handling and Recovery**
Automated poker requires robust error handling, as websites may not always load correctly, or unexpected popups may occur. The `helpers` module contains recovery mechanisms, such as reloading the page or dismissing popups when they appear, to ensure smooth gameplay.

### 3. **Compatibility**
The module is built to work with a variety of browsers, primarily Chrome and Firefox, but can be extended to other browsers by adding relevant drivers in the `drivers` folder.

### 4. **Testing and Debugging**
The directory includes tools to test and debug browser automation. For instance, `take_screenshot.py` is used to capture snapshots of the browser to verify if elements are detected correctly. Logs are generated during gameplay to record actions and errors for troubleshooting.

### Future Improvements

- **Multi-Table Support**: In future versions, the automation module will allow AI to play on multiple tables simultaneously by handling multiple browser windows.
- **Enhanced Detection**: Improve game state reading by using advanced image recognition or OCR (Optical Character Recognition) for better accuracy in identifying cards and player actions.
- **Cross-Browser Compatibility**: Extend support to other browsers like Safari and Edge for greater flexibility in deployment.

## Usage

1. Ensure you have installed all dependencies from the project root using `pip install -r requirements.txt`.
2. Place the required browser driver executables (e.g., ChromeDriver, GeckoDriver) in the `/drivers` directory.
3. Run the desired script (e.g., `place_bet.py`) to perform browser actions.
4. Monitor logs and screenshots for debugging purposes.

