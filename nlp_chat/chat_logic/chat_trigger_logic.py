# chat_trigger_logic.py

import random
import time
from nlp_chat.models.chat_model import generate_response  # Assuming there's a model file for chat generation

class ChatTriggerLogic:
    """
    This class handles logic for triggering appropriate chat responses during a poker game based on game events
    such as wins, losses, bluffing, and other significant in-game actions.
    """

    def __init__(self):
        # Predefined chat templates for different scenarios
        self.bluff_templates = [
            "I’m going to take this one down!", 
            "You won't believe what I have.", 
            "Are you sure you want to call?"
        ]
        self.win_templates = [
            "Nice hand!", 
            "That was a close one.", 
            "Better luck next time!"
        ]
        self.lose_templates = [
            "You got me this time!", 
            "I’ll get you on the next one.", 
            "Well played!"
        ]
        self.general_templates = [
            "Good luck everyone!", 
            "Feeling good about this one.", 
            "Let's see those cards!"
        ]

    def trigger_chat(self, game_state):
        """
        Triggers chat based on the current game state.
        
        :param game_state: Dictionary containing current game information (e.g., AI hand, opponent actions, round).
        :return: Chat response string
        """
        if self._detect_bluff(game_state):
            return self._send_bluff_message()
        elif self._detect_win(game_state):
            return self._send_win_message()
        elif self._detect_loss(game_state):
            return self._send_loss_message()
        else:
            return self._send_general_message()

    def _detect_bluff(self, game_state):
        """
        Detects if the AI is bluffing based on the game state.
        :param game_state: Dictionary with game details (e.g., AI hand strength, bet size, opponent actions).
        :return: Boolean indicating whether the AI is bluffing.
        """
        # Simplified bluff detection logic
        return game_state.get('ai_is_bluffing', False)

    def _detect_win(self, game_state):
        """
        Detects if the AI has won the hand.
        :param game_state: Dictionary with game details (e.g., round outcome).
        :return: Boolean indicating if AI has won.
        """
        return game_state.get('ai_won_hand', False)

    def _detect_loss(self, game_state):
        """
        Detects if the AI has lost the hand.
        :param game_state: Dictionary with game details (e.g., round outcome).
        :return: Boolean indicating if AI has lost.
        """
        return game_state.get('ai_lost_hand', False)

    def _send_bluff_message(self):
        """
        Sends a random bluff message from the predefined template.
        :return: String containing the bluff chat message.
        """
        message = random.choice(self.bluff_templates)
        self._simulate_typing_delay(message)
        return message

    def _send_win_message(self):
        """
        Sends a random win message from the predefined template.
        :return: String containing the win chat message.
        """
        message = random.choice(self.win_templates)
        self._simulate_typing_delay(message)
        return message

    def _send_loss_message(self):
        """
        Sends a random loss message from the predefined template.
        :return: String containing the loss chat message.
        """
        message = random.choice(self.lose_templates)
        self._simulate_typing_delay(message)
        return message

    def _send_general_message(self):
        """
        Sends a random general chat message.
        :return: String containing a general chat message.
        """
        message = random.choice(self.general_templates)
        self._simulate_typing_delay(message)
        return message

    def _simulate_typing_delay(self, message):
        """
        Simulates a delay between when a chat message is triggered and when it is sent, 
        to mimic natural typing behavior.
        
        :param message: The chat message to be sent.
        """
        typing_speed = random.uniform(1.0, 2.5)  # Simulate a delay of 1 to 2.5 seconds
        time.sleep(typing_speed)
        print(f"Chat message sent: {message}")

# Example usage:
# chat_logic = ChatTriggerLogic()
# game_state = {'ai_is_bluffing': True, 'ai_won_hand': False, 'ai_lost_hand': False}
# response = chat_logic.trigger_chat(game_state)
# print(response)
