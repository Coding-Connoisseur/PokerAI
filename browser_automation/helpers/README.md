# Helpers Module

The `helpers` directory contains utility functions that support browser automation tasks in the PokerAI system. These scripts ensure that key browser operations such as element detection, page navigation, and error handling are robust and efficient. The helpers provide essential functionality that is reused across the main automation scripts, improving reliability and scalability when interacting with online poker platforms.

## Directory Structure

- **`wait_for_element.py`**: Implements waiting mechanisms to ensure elements are fully loaded and interactable before actions are performed on them.
  - **Functionality**: This script is crucial for synchronizing actions with the dynamic loading of poker platform elements. It allows the browser automation to wait until specific HTML elements (e.g., buttons, text fields) are visible, clickable, or otherwise ready for interaction, avoiding premature actions that could lead to failures.
  - **Key Functions**:
    - `wait_until_visible(driver, selector, timeout)`: Waits for an element to become visible on the page before interacting.
    - `wait_until_clickable(driver, selector, timeout)`: Ensures that an element is clickable, preventing clicks on elements that are not fully interactive.

- **`take_screenshot.py`**: Captures screenshots at specific points during browser interactions for debugging and state tracking.
  - **Functionality**: The script captures screenshots when critical actions occur, such as placing a bet, reading game states, or handling unexpected errors. These screenshots are invaluable for debugging, performance monitoring, and auditing game flow.
  - **Key Functions**:
    - `capture_screenshot(driver, filepath)`: Takes a screenshot of the current browser window and saves it to the specified filepath.
    - `capture_on_error(driver, filepath)`: Automatically captures a screenshot when an error or unexpected condition occurs.

- **`handle_popups.py`**: Detects and handles popups that can interrupt gameplay, such as advertisements or confirmation dialogs.
  - **Functionality**: Poker platforms often trigger popups that can disrupt the flow of gameplay, such as promotional offers or login prompts. This script ensures that popups are detected and dismissed automatically to prevent interruptions.
  - **Key Functions**:
    - `detect_and_close_popup(driver)`: Searches for common popup elements (e.g., modal dialogs) and closes them if detected.
    - `detect_adblock_warning(driver)`: Specific handler for adblock warnings, dismissing them without affecting gameplay.

- **`element_exists.py`**: Verifies the existence of specific elements on the page.
  - **Functionality**: Used to confirm whether an important element (such as a betting button or a player’s card) is present on the poker platform. This helps avoid performing actions based on incomplete or outdated game state data.
  - **Key Functions**:
    - `element_present(driver, selector)`: Returns a boolean indicating whether the specified element exists on the page.
    - `element_visible(driver, selector)`: Verifies if an element is visible (not just present in the DOM but interactable).

- **`retry_logic.py`**: Implements retry logic for actions that may fail due to temporary issues, such as network latency or incomplete page loads.
  - **Functionality**: This script is designed to handle temporary failures in browser interactions, automatically retrying failed actions with increasing time intervals. This is especially useful when dealing with unreliable connections or slow-loading pages.
  - **Key Functions**:
    - `retry_action(action, retries, delay)`: Retries a given action a specified number of times, with a delay between each attempt.
    - `retry_on_exception(driver, action, retries, delay, exception)`: Retries an action only if a specified exception (such as `ElementNotInteractableException`) occurs.

## Usage

### 1. **Waiting for Elements**
To avoid interacting with elements before they are ready, use `wait_for_element.py` in your scripts. For example, before clicking a button:

```python
from helpers.wait_for_element import wait_until_clickable

wait_until_clickable(driver, 'button.submit', 10)
driver.find_element_by_css_selector('button.submit').click()
```

### 2. **Handling Popups**
Popups can disrupt the game flow, and handling them automatically ensures uninterrupted gameplay:

```python
from helpers.handle_popups import detect_and_close_popup

detect_and_close_popup(driver)
```

### 3. **Retrying Failed Actions**
If an action fails due to a temporary issue (e.g., network lag), use `retry_logic.py` to attempt the action again:

```python
from helpers.retry_logic import retry_action

retry_action(lambda: driver.find_element_by_id('bet_button').click(), retries=3, delay=2)
```

### 4. **Taking Screenshots for Debugging**
Use `take_screenshot.py` to capture screenshots when unexpected conditions occur or for auditing gameplay:

```python
from helpers.take_screenshot import capture_on_error

try:
    driver.find_element_by_id('bet_button').click()
except Exception as e:
    capture_on_error(driver, 'logs/screenshots/error.png')
```

## Future Enhancements

- **AI-Based Element Detection**: Improve element detection by using AI models to identify dynamic content more accurately, especially on platforms with frequently changing layouts.
- **Dynamic Retry Logic**: Implement dynamic backoff algorithms for retrying actions, adjusting retry intervals based on previous failures or network conditions.
- **Automated Browser Logs**: Integrate automated logging of browser console output, providing more detailed context for debugging complex issues.
- **Enhanced Popup Detection**: Expand the popup detection system to cover a wider range of popup formats, including complex JavaScript alerts or custom modals.
- **Smart Screenshot Triggers**: Develop intelligent screenshot triggers that activate based on unusual game conditions or performance anomalies, beyond just error states.

---

The `helpers` module is essential for ensuring smooth, reliable browser automation, particularly in the dynamic environment of online poker platforms. It provides reusable utilities that enhance error handling, improve robustness, and streamline gameplay interactions.
