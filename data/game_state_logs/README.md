# Game State Logs Configuration

The `game_state_logs` configuration file is responsible for controlling how the PokerAI logs, stores, and manages the state of poker games during gameplay. This data is critical for tracking the evolution of the game, analyzing AI decision-making, and providing feedback for further reinforcement learning. The game state logs capture information such as player actions, hand outcomes, pot size, and opponent behaviors. This configuration allows for customization of the logging behavior to suit different use cases, such as debugging, training, or real-time monitoring.

## Directory Structure

- **`/logs/`**: This folder stores all game state log files, including detailed logs of each hand played by the AI.
  - **`session_logs/`**: Contains logs of complete poker sessions. Each session log records all actions from the start of the game to the end, including decisions made by the AI and the outcomes of hands.
  - **`hand_logs/`**: Stores individual hand logs, which capture detailed information about each hand played, including cards dealt, actions taken, and results.
  - **`opponent_logs/`**: Tracks opponent behavior and tendencies over time. This data is used to build opponent profiles and improve the AI’s decision-making during play.

- **`/errors/`**: A sub-directory where error logs are stored. This folder captures any issues encountered during game state logging, such as missing data, failed game state updates, or unexpected browser behavior.

## Configuration Parameters

- **`log_level`**: Controls the level of detail captured in the game state logs. Options include:
  - `DEBUG`: Captures all possible data, including game states, individual actions, AI decisions, and intermediate calculations.
  - `INFO`: Captures essential game state information, including final outcomes, player actions, and AI decisions, but omits intermediate details.
  - `ERROR`: Only logs errors or issues encountered during gameplay.

- **`log_format`**: Defines the format in which logs are stored. Options include:
  - `JSON`: Logs are saved in structured JSON files, which are easily parsed and analyzed by external tools.
  - `CSV`: Logs are saved in CSV format for easy import into spreadsheets or databases.
  - `TEXT`: Simple text logs, which are human-readable and suitable for quick reviews.

- **`log_rotation_policy`**: Specifies how logs are managed over time.
  - `size`: Rotate logs once they exceed a certain size (e.g., 10MB).
  - `time`: Rotate logs daily, weekly, or monthly.
  - `none`: No rotation; logs will grow indefinitely unless manually deleted.

- **`session_timeout`**: The maximum duration for a single session before automatically logging it as complete and rotating to a new log file.

- **`include_opponent_profile`**: Boolean parameter indicating whether to include detailed opponent profiling data in the logs. This is useful for advanced analysis of opponent behavior but can increase log size significantly.

- **`replay_mode`**: Enables the logging of game states in a format suitable for replaying poker sessions. When enabled, the log files are structured to allow for step-by-step replays of game sessions.

## Usage Scenarios

1. **Debugging**: Set `log_level` to `DEBUG` to capture detailed logs that include every decision made by the AI. This is useful when diagnosing issues with the AI's decision-making or browser automation.
2. **Training**: During training, logs can be set to `INFO` to capture enough detail for analysis without overwhelming the system with data.
3. **Performance Monitoring**: Set `log_format` to `CSV` or `JSON` for structured logs that can be fed into analytics tools to measure AI performance over time.
4. **Opponent Analysis**: Enable `include_opponent_profile` to track opponent behavior and use it for training or strategy refinement.

## Example Configuration

```yaml
log_level: DEBUG
log_format: JSON
log_rotation_policy: time
session_timeout: 60m
include_opponent_profile: true
replay_mode: true
```

## Future Enhancements

- **Real-Time Log Streaming**: Enable real-time streaming of game state logs to external monitoring systems or dashboards for live performance tracking.
- **Cloud Log Storage**: Add support for storing logs in cloud-based storage solutions such as AWS S3 or Google Cloud Storage for centralized data access and analysis.
- **Advanced Log Filtering**: Introduce more granular filtering options to capture only specific events or data points, such as certain betting rounds or decisions.
- **Log Compression**: Implement automatic log compression to save disk space, especially during long training sessions or real-world gameplay.

---

By using this configuration, you can fully control how the PokerAI logs its gameplay, making it easy to debug, analyze, and improve the AI over time.
```

### Key Additions:
1. **Replay Mode**: Enables logs to be structured for session replays.
2. **Real-Time Log Streaming**: A future feature for live monitoring of logs.
3. **Cloud Log Storage**: A future enhancement for centralized storage of logs.
4. **Advanced Log Filtering**: Filtering specific game events for more focused analysis.
5. **Log Compression**: A future option for saving disk space during long sessions.
