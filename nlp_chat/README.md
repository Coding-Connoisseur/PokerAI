# NLP Chat Module

The `nlp_chat` module enhances the PokerAI by adding conversational abilities, allowing the AI to participate in human-like chat during poker games. Using a GPT-based model, the AI can chat, bluff, and interact with other players, making it more convincing in online poker environments.

## Directory Structure

- **`/conversation_templates/`**: Predefined chat templates for typical poker scenarios.
  - **Bluffing Templates**: Pre-set lines used when bluffing.
  - **Banter and Friendly Chat**: General conversational lines to simulate human interaction.
  - **Strategic Comments**: Statements intended to influence opponents' actions.

- **`/models/`**: Stores the GPT-based model or references to the language models used for chat.
  - **GPT Weights**: Pre-trained GPT model or fine-tuned versions specific to poker chat.
  - **Fine-Tuning Scripts**: Scripts for adapting the GPT model to specific poker language patterns or styles.

- **`/chat_logic/`**: Contains scripts that define the logic for when and how the AI should initiate or respond to chats.
  - **Chat Timing Logic**: Determines appropriate moments to engage in conversation (e.g., after a successful bluff).
  - **Bluffing Behavior**: Dynamically adjusts conversation to align with the AI's strategy engine decisions (e.g., bluffing more against tight players).

- **`/response_generator.py`**: Core script that generates chat responses based on game context and opponent behavior.
  - **Template Selection**: Picks responses from predefined templates.
  - **Custom GPT Responses**: Generates unique chat messages via GPT when no suitable template is available.

- **`/chat_testing/`**: Contains mock games and tools for testing chat functionality in isolated environments.

## How Modules Work Together

The **NLP Chat Module** interacts closely with the following components:
- **Strategy Engine**: Guides when and how the AI engages in conversation based on gameplay context, such as bluffing moments or post-win chats.
- **Opponent Profiling**: Integrates with opponent behavior analysis to adjust chat frequency and style.
- **Browser Automation**: Automates sending chat messages on poker platforms during live play.

For detailed integration with the **Strategy Engine**, see [strategy_engine/README.md](../strategy_engine/README.md).

## Key Configurations

- **Response Delay Settings**: Configured in `chat_logic/` to introduce realistic typing delays, simulating human behavior.
- **Bluffing Frequency**: Defined in `adaptive_strategy.yaml`, this determines how often the AI uses bluffing phrases.
- **Language Model Tuning**: You can fine-tune the GPT model in `/models/` to customize the AI’s tone, language, and bluffing style.

## Essential Scripts and Usage

1. **Start Chat Module**: 
   To initiate the chat system alongside gameplay, ensure that the `response_generator.py` script is running:
   ```bash
   python response_generator.py --game-context <context>
   ```

2. **Fine-Tuning GPT**: 
   If you need to adapt the AI’s language model, run the fine-tuning script located in `/models/`:
   ```bash
   python fine_tune_gpt.py --data <chat_dataset>
   ```

3. **Chat Testing**: 
   To test the chat logic, use mock environments in `/chat_testing/`:
   ```bash
   python test_chat_logic.py --scenario <mock_game>
   ```

## Real-Time Impact of Configurations

- **Bluff Timing**: The AI will engage in bluff chat if the strategy engine signals a bluff opportunity. The specific response depends on the GPT model’s outputs or predefined templates.
- **Opponent-Specific Responses**: Using opponent profiling, the AI adjusts chat styles. For example, against aggressive players, it may attempt to provoke or confuse through specific phrases.

## Cross-References

For further details on how the chat module ties into other parts of the system, refer to:
- [Browser Automation Module](../browser_automation/README.md): See how chat actions are executed in real-time.
- [Opponent Profiling](../config/opponent_profiles/README.md): Learn how the AI adjusts chat strategies based on opponent behavior.

## Future Enhancements

- **Multilingual Chat Support**: Expand the module to handle multiple languages, adapting to different poker platforms globally.
- **Emotion Detection**: Incorporate emotion detection to modify responses based on opponents' emotional states.
- **Advanced Conversation**: Implement more nuanced conversation templates that can mimic specific personality traits.

---

The **NLP Chat Module** is an integral part of making PokerAI appear human-like, using real-time decision-making to enhance both gameplay and psychological interaction.
```

### Improvements Added:
1. **Cross-Referencing**:
   - Linked to relevant modules like the **Strategy Engine** and **Browser Automation**.
   
2. **Detailed Documentation**:
   - Added usage examples for critical scripts like `response_generator.py` and `fine_tune_gpt.py`.

3. **Extended Explanations**:
   - Highlighted the real-time impact of key configurations, such as bluff frequency and chat timing.
