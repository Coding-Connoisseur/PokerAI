# Tests Directory

The `tests` directory contains unit, integration, and system tests to ensure the functionality, reliability, and performance of the various components of the PokerAI project. Each test script is designed to validate a specific module or feature, making sure that the AI behaves as expected under different scenarios and edge cases. This directory follows industry-standard testing practices, and is structured to cover every major module, including reinforcement learning, strategy engine, browser automation, and NLP chat.

## Directory Structure

- **`/unit_tests/`**: Contains unit tests for individual functions or classes. These tests focus on specific, isolated parts of the codebase to ensure that each function or module behaves as expected.
  - **`test_rl_agent.py`**: Tests individual RL agents, verifying that Q-values, rewards, and policies are being calculated and updated correctly.
  - **`test_strategy_engine.py`**: Ensures that the strategy engine's decision-making logic works correctly for different game states and scenarios (e.g., pre-flop, post-flop).
  - **`test_browser_automation.py`**: Verifies that browser actions such as clicking, navigating, and inputting text work as expected.

- **`/integration_tests/`**: These tests check how different components work together, ensuring that integrated systems (e.g., RL agents interacting with the strategy engine or browser automation) function smoothly.
  - **`test_rl_with_strategy.py`**: Tests the integration of the RL module and strategy engine, ensuring decisions made by the AI are consistent with learned policies.
  - **`test_nlp_with_gameplay.py`**: Verifies that the NLP chat module interacts correctly with the strategy engine, triggering appropriate chat responses based on the AI's in-game decisions.

- **`/performance_tests/`**: Focuses on testing the performance and efficiency of key components, especially during training and simulations. These tests measure how quickly the system can process game states, make decisions, and learn over time.
  - **`test_training_speed.py`**: Measures the time taken by the RL agents to complete a set number of episodes during training.
  - **`test_simulation_throughput.py`**: Evaluates the number of simulated poker games the AI can process per second to ensure scalability.

- **`/system_tests/`**: Full end-to-end tests that simulate real-world scenarios to ensure the PokerAI functions as expected in actual poker games. These tests cover the entire pipeline from game simulation to decision-making and chat interaction.
  - **`test_full_game_play.py`**: Simulates complete poker games, testing the AI's ability to make decisions, interact with the platform, and engage in chat across various stages of the game.
  - **`test_multiplayer_scenario.py`**: Tests the AI’s performance and decision-making when playing against multiple real or simulated opponents in different game configurations.

- **`/test_data/`**: Contains datasets and mock data used during testing. This includes synthetic poker hand histories, mock opponent profiles, and simulated game logs, which help in validating the accuracy of the AI's behavior.
  - **`hand_history_samples.json`**: Example hand histories used to test the processing and decision-making capabilities of the AI.
  - **`mock_opponent_profiles.csv`**: Sample opponent data used in testing the AI's opponent modeling and exploitative strategy functions.

## Key Testing Scenarios

1. **Unit Testing**: Ensures each module and function behaves as expected. For example, the `test_rl_agent.py` script validates that reward values are updated correctly after each game.
2. **Integration Testing**: Validates that the RL, strategy engine, and browser automation work seamlessly together. For instance, testing that RL agents can successfully interact with poker platforms through the browser automation layer.
3. **Performance Testing**: Tests the efficiency of the RL training process, ensuring that the system can handle long training sessions without performance bottlenecks.
4. **End-to-End Testing**: Simulates entire poker games to verify that the AI makes coherent decisions, interacts with the game platform correctly, and executes chat messages through the NLP engine.

## Usage

1. **Run Unit Tests**: Use `pytest` or any other test runner to execute unit tests, ensuring isolated components work as expected.
   - Example: `pytest unit_tests/test_rl_agent.py`
   
2. **Run Integration Tests**: Validate the combined functionality of multiple modules.
   - Example: `pytest integration_tests/test_rl_with_strategy.py`
   
3. **Performance Testing**: Measure the efficiency of training and decision-making.
   - Example: `pytest performance_tests/test_training_speed.py`
   
4. **System Testing**: Simulate full games to validate the entire AI pipeline.
   - Example: `pytest system_tests/test_full_game_play.py`

## Future Enhancements

- **Automated Test Runs**: Integrate continuous testing pipelines using CI/CD tools (e.g., GitHub Actions, Jenkins) to automatically run tests on code commits and ensure consistent functionality.
- **Stress Testing**: Add stress tests that evaluate the system's behavior under heavy load conditions, such as playing multiple games simultaneously or handling long training periods.
- **Advanced Simulation Tests**: Introduce more complex simulation environments that better represent real-world poker games with varying opponent skill levels and unpredictable behaviors.

---

This directory ensures that the PokerAI project is thoroughly tested, allowing for confident development, deployment, and scalability across various platforms.
