# NLP Chat Module

The `nlp_chat` directory contains all components responsible for the natural language processing (NLP) functionalities of the PokerAI. This module enables the AI to engage in human-like chat interactions during poker games. These interactions may include bluffing, friendly banter, and strategic conversation to influence other players' actions. The NLP chat system is powered by GPT models and designed to create a more realistic poker experience by adding psychological tactics.

## Directory Structure

- **`/conversation_templates/`**: Contains pre-defined chat templates that the AI can use for quick responses. These templates are designed to mimic human-like behavior and include common poker chat phrases, bluffing lines, and casual conversation topics. They are categorized based on situations:
  - **Bluff Responses**: Lines used when the AI is attempting a bluff (e.g., "I've got this one in the bag").
  - **Friendly Banter**: Phrases for casual chat to make the AI appear more human (e.g., "Nice hand!" or "Tough luck").
  - **Strategic Comments**: Comments that may be used to influence other players, such as inducing a fold (e.g., "You might want to fold this one").

- **`/models/`**: This folder stores the trained GPT models or links to external language models used for generating real-time chat responses.
  - **GPT Model Weights**: Pre-trained weights for the language model, which powers the chat capabilities.
  - **Fine-Tuning Scripts**: Scripts that allow developers to fine-tune the GPT model based on specific poker conversations or scenarios.

- **`/chat_logic/`**: The core logic for determining when and how the AI should engage in conversation. This logic determines:
  - **Chat Triggers**: Situations in which the AI should initiate or respond to a chat (e.g., after a successful bluff or a big win).
  - **Bluff Detection**: Determines when the AI should use bluff-related chat phrases, based on the current state of the game and the strategy in use.
  - **Opponent Profiling Integration**: Customizes responses based on the opponent's playing style (aggressive, passive, etc.). For example, against a passive player, the AI may use more intimidating chat lines.

- **`/response_generator.py`**: This script dynamically generates chat responses using the GPT model. It selects the appropriate template or triggers the language model to produce a unique response based on the game context.
  - **Template Selection**: Chooses a response from the `conversation_templates/` based on the current scenario.
  - **Custom Response Generation**: In more complex situations, generates an original response using the GPT model and game data.
  - **Timing Logic**: Introduces delays between messages to simulate a natural human typing speed.

- **`/chat_testing/`**: Contains tools and scripts for testing the NLP system. This includes simulated poker environments where the chat module can be tested in isolation.
  - **Mock Games**: Scripts that simulate poker scenarios to test how the AI engages in conversation.
  - **Test Logs**: Stores logs of chat interactions for analysis and debugging.

## Functionality Overview

1. **Conversation Flow**: The AI engages in chat during poker games to simulate realistic human interactions, enhance the psychological aspects of the game, and potentially influence opponent behavior.
2. **Bluffing and Strategy**: The AI uses strategic phrases and banter to support its in-game actions, such as bluffing or creating false impressions of hand strength.
3. **Real-Time Response Generation**: Depending on the game state, the AI either selects a response from pre-defined templates or generates an original response using the GPT model.

## Future Enhancements

- **Adaptive Chat**: Fine-tune the model to learn from interactions and adjust chat behavior dynamically, adapting to new opponents or unusual strategies.
- **Emotion Detection**: Add sentiment analysis to detect the emotional state of opponents and adjust the chat responses accordingly.
- **Multilingual Support**: Expand the module to include multiple languages, enabling the AI to communicate with players from different regions.

## Usage

1. **Load GPT Models**: Ensure the trained GPT models are loaded from the `/models/` directory.
2. **Initiate Chat Module**: Run the `response_generator.py` to activate the chat logic.
3. **Monitor Logs**: Use the `chat_testing/` tools to log chat responses and debug any unexpected behavior.
4. **Customize Chat Templates**: Modify or extend the templates in the `conversation_templates/` folder to add new responses or adjust for specific game scenarios.

---

The NLP chat module creates a more engaging and psychologically complex poker experience by mimicking human conversational behavior.

