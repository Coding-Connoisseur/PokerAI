# NLP Chat Module

The `nlp_chat` module allows the PokerAI to engage in conversational interactions during poker games using natural language processing (NLP). This system is designed to simulate human-like chat behavior, including bluffing, friendly banter, and strategic comments, enhancing the psychological aspects of poker.

## Directory Structure

### `/conversation_templates/`
This directory contains pre-defined chat templates that the AI uses for quick, context-based responses. These templates simulate real-time chat interactions during poker games. Files include:
- **bluff_responses.json**: Phrases used when the AI is bluffing.
- **friendly_banter.json**: Common conversational lines to maintain a human-like appearance.
- **strategic_comments.json**: Chat lines aimed at influencing opponents’ decisions, such as inducing folds.
- **default_responses.json**: Generic responses for various situations where specific responses are unnecessary.

### `/models/`
This directory contains pre-trained language models or configurations used to generate real-time chat responses using GPT-based technology. Files include:
- **gpt_model_weights.pth**: Pre-trained weights for the GPT model.
- **model_config.yaml**: Configuration settings for the NLP model, such as max tokens, temperature, etc.
- **fine_tuning_script.py**: Script for fine-tuning the model on specific poker-related conversations.
- **tokenizer_config.json**: The configuration used for tokenizing input text for the model.

### `/chat_logic/`
This directory contains the logic and decision-making scripts responsible for deciding when and how to respond to opponents during gameplay. The AI uses these scripts to determine the right context for each response. Files include:
- **response_generator.py**: Dynamically generates chat responses based on game state and conversation context.
- **chat_trigger_logic.py**: Defines when the AI should send chat messages, based on in-game events (e.g., a big bet, a win, or a bluff).
- **bluffing_chat_logic.py**: Decides when to bluff through chat and selects the appropriate bluffing response.
- **timing_manager.py**: Simulates human-like response timing by delaying responses to avoid appearing automated.

### `/chat_testing/`
This folder contains scripts and test cases for evaluating the performance of the NLP chat module. It simulates poker interactions to verify that the AI generates appropriate and contextually relevant responses. Files include:
- **test_chat_responses.py**: Simulates conversations during poker games to verify that chat responses are accurate.
- **mock_game_state.json**: Mock data to simulate different poker game scenarios for testing chat responses.
- **performance_test.py**: Tests the efficiency and performance of real-time chat generation during gameplay.
- **log_analysis_tool.py**: Analyzes chat logs for debugging and improving response quality.

## Functionality Overview

1. **Conversation Flow**: The AI engages in conversation during poker games to mimic realistic human interaction, including bluffs and banter.
2. **Bluffing and Strategy**: The AI uses strategic chat lines to complement its in-game actions, like bluffing or inducing a fold.
3. **Real-Time Chat Generation**: Responses are generated either from pre-defined templates or dynamically using GPT models, depending on the situation.
4. **Testing & Debugging**: The `chat_testing/` directory contains tools for validating the system’s response accuracy and efficiency in real-time scenarios.

## Future Enhancements

- **Advanced Opponent Analysis**: Add capabilities to analyze opponent chat patterns and respond accordingly.
- **Emotion Detection**: Integrate sentiment analysis to detect emotions in chat and adjust responses based on opponent behavior.
- **Multilingual Support**: Expand the system to support multiple languages for global poker platforms.

---

This `nlp_chat` module adds a psychological layer to PokerAI, making it more competitive and human-like by using natural language for real-time communication during poker games.
