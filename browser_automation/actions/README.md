# Browser Automation - Actions Directory

This directory contains scripts for automating individual browser actions used in the PokerAI system. Each script executes a specific action needed for interacting with the online poker platform, forming the foundation for more complex workflows. These actions are reusable and customizable, enabling the AI to navigate, interact, and respond to dynamic web elements during gameplay.

## Directory Structure

- **`click_button.py`**: Automates button click events on specific elements.
  - **Functionality**:
    - Locates the button using element selectors (e.g., ID, XPath, CSS).
    - Waits for the button to become clickable.
    - Simulates a button click and verifies the resulting state transition.
  - **Advanced Features**:
    - **Action Chaining**: Allows chaining of multiple button clicks in rapid succession.
    - **Fail-Safe Mechanism**: Retries the click operation upon failure and captures screenshots for debugging.

- **`enter_text.py`**: Inputs text into web forms (e.g., chat or bet entry).
  - **Functionality**:
    - Clears existing text (if necessary) and types in new text.
    - Optionally submits the text by simulating an "Enter" key press.
  - **Advanced Features**:
    - **AI-Enhanced Text Entry**: Leverages NLP to automatically respond with chat messages based on game events.
    - **Form Autofill**: Uses pre-defined templates for automated bet inputs or common chat phrases.

- **`navigate.py`**: Automates page navigation, such as moving between the game lobby and tables.
  - **Functionality**:
    - Navigates to specific URLs or interacts with page elements to load new screens.
    - Verifies that the navigation completes successfully before proceeding.
  - **Advanced Features**:
    - **Multi-URL Handling**: Supports simultaneous navigation across multiple tabs or windows.
    - **Dynamic Wait Mechanism**: Adjusts waiting times based on page load performance.

- **`select_dropdown_option.py`**: Selects an option from a dropdown menu (e.g., choosing game stakes).
  - **Functionality**:
    - Expands the dropdown menu and selects an option by its visible text or value.
    - Ensures the option is successfully selected and logs the action.
  - **Advanced Features**:
    - **Smart Option Recognition**: Uses machine learning to adapt to changes in dropdown structure.
    - **Multi-Option Selection**: Supports selecting multiple options from advanced UI components (e.g., multi-select lists).

- **`scroll_page.py`**: Scrolls the page to bring specific elements into view.
  - **Functionality**:
    - Scrolls vertically by a specified distance or until a target element is visible.
  - **Advanced Features**:
    - **Element-Based Scrolling**: Scrolls intelligently based on element visibility rather than predefined distances.
    - **Smooth Scrolling**: Implements human-like scrolling behavior to avoid detection on certain platforms.

- **`handle_modal.py`**: Detects and interacts with modal dialogs, such as popups or confirmation boxes.
  - **Functionality**:
    - Detects the presence of modals and interacts with confirmation or close buttons.
    - Waits for the modal to disappear before continuing automation.
  - **Advanced Features**:
    - **Custom Modal Handlers**: Adds specialized logic for handling modals with variable content (e.g., ad popups, connection alerts).
    - **AI-Based Modal Detection**: Uses image recognition or text analysis to detect more complex modals that vary across games.

- **`capture_element_screenshot.py`**: Captures a screenshot of a specific web element.
  - **Functionality**:
    - Identifies the web element and takes a high-resolution screenshot of it.
    - Stores the screenshot in the logs for later review.
  - **Advanced Features**:
    - **Automated Screenshot Logging**: Takes periodic screenshots to track game progress and debug issues.
    - **Element-State Capture**: Captures screenshots of elements in different states (e.g., buttons before and after clicks).

- **`hover_over_element.py`**: Simulates hovering over an element, useful for revealing hidden menus or tooltips.
  - **Functionality**:
    - Moves the mouse over a specific element and triggers hover events.
    - Detects and logs any dynamic content that appears after the hover action.
  - **Advanced Features**:
    - **Dynamic Hovering**: Adjusts hover behavior based on content that dynamically changes upon interaction.
    - **Advanced Tooltip Handling**: Captures information from tooltips or popups triggered by hovering.

- **`validate_element_state.py`**: Validates the state of a specific web element (e.g., ensuring a button is enabled).
  - **Functionality**:
    - Checks the element’s properties, such as visibility, enabled state, or selected status.
    - Logs the element’s state for decision-making in the strategy engine.
  - **Advanced Features**:
    - **State Change Detection**: Monitors elements continuously to detect when states change (e.g., bet buttons becoming active).
    - **Real-Time Feedback Loop**: Integrates with the strategy engine to adjust gameplay based on the element's state.

## Key Features

1. **Modularity and Reusability**: Each script is independent and reusable, allowing for flexible automation workflows that can adapt to various poker platforms.
2. **Enhanced Error Handling**: All scripts come with robust error handling to deal with unexpected behaviors such as page timeouts, missing elements, or modals.
3. **AI-Driven Adaptation**: Certain scripts incorporate AI and machine learning to intelligently adapt to dynamic web content and UI changes.
4. **Multi-Tab Management**: Several scripts include support for automating multiple tabs or browser windows, enabling the AI to handle multiple poker tables simultaneously.
5. **Dynamic Element Handling**: Advanced element detection and interaction capabilities allow the system to adjust to changes in the platform’s UI, ensuring continuous automation.

## Usage

1. **Executing Actions Individually**: Each action can be executed as a standalone script or combined with others for more complex tasks.
2. **Combining Actions**: For example, to join a game and place a bet, you can combine `navigate.py`, `select_dropdown_option.py`, `click_button.py`, and `enter_text.py`.
3. **Customizing Parameters**: Each script accepts customizable parameters, allowing for tailored behavior depending on the platform or specific interaction.
4. **Logging for Debugging**: The output of each script includes detailed logs, which can be reviewed to debug issues related to element detection, interaction timing, or page navigation.

## Future Enhancements

1. **Advanced Game State Monitoring**: Implement more sophisticated AI techniques to track the game’s progress by monitoring and analyzing the poker platform’s UI in real time.
2. **Mobile Compatibility**: Extend automation capabilities to mobile platforms by adding support for mobile browser emulation and native app interaction.
3. **Voice Command Integration**: Enable the PokerAI to use voice commands for interacting with voice-enabled poker platforms or automating live dealer interactions.
4. **WebSocket Integration**: Add support for real-time WebSocket communication, allowing PokerAI to react to live updates on the platform without relying solely on page scraping.
5. **Adaptive Decision Trees**: Implement AI-driven decision trees to adjust the action sequences based on dynamic game states, such as changing betting strategies when certain thresholds are met.

---

This directory provides essential building blocks for automating complex poker gameplay interactions. By enhancing the base functionality with AI-based features and error-handling mechanisms, the PokerAI system becomes adaptable, resilient, and capable of interacting with a wide range of poker platforms.
