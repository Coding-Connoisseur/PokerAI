# timing_manager.py

import random
import time

class TimingManager:
    """
    The TimingManager is responsible for managing the timing of chat messages during gameplay. It introduces
    delays between chat messages to simulate natural human-like interaction and prevent the AI from appearing too robotic.
    """

    def __init__(self, min_delay=1.0, max_delay=5.0, variability_factor=0.5):
        """
        Initialize the TimingManager with default values for delay times.

        Args:
        - min_delay (float): Minimum delay in seconds between chat messages.
        - max_delay (float): Maximum delay in seconds between chat messages.
        - variability_factor (float): Factor by which to randomize the timing delays for more natural variations.
        """
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.variability_factor = variability_factor

    def calculate_delay(self, urgency_level="normal"):
        """
        Calculate a delay based on the urgency of the situation (e.g., post-flop bluff chat vs casual table banter).
        
        Args:
        - urgency_level (str): A string indicating the urgency ("urgent", "normal", "low").
        
        Returns:
        - float: The calculated delay in seconds.
        """
        if urgency_level == "urgent":
            base_delay = self.min_delay
        elif urgency_level == "low":
            base_delay = self.max_delay
        else:
            base_delay = random.uniform(self.min_delay, self.max_delay)
        
        # Add random variability to make the timing more human-like.
        variability = random.uniform(-self.variability_factor, self.variability_factor)
        final_delay = max(0, base_delay + variability)  # Ensure delay is non-negative

        return final_delay

    def execute_with_delay(self, func, *args, urgency_level="normal", **kwargs):
        """
        Execute a function after a calculated delay to simulate natural typing or pauses between chat messages.
        
        Args:
        - func (callable): The function to execute after the delay (e.g., a chat message sender).
        - urgency_level (str): The urgency level of the situation which affects the delay.
        - *args, **kwargs: Arguments to pass to the function being delayed.
        
        Returns:
        - The result of the function execution after the delay.
        """
        delay = self.calculate_delay(urgency_level)
        print(f"Delaying execution by {delay:.2f} seconds for {func.__name__} with urgency '{urgency_level}'")
        time.sleep(delay)
        return func(*args, **kwargs)

    def chat_typing_simulation(self, message):
        """
        Simulates a typing delay for chat messages, introducing a natural pause based on message length.
        
        Args:
        - message (str): The chat message to be "typed".
        
        Returns:
        - float: Simulated typing duration.
        """
        typing_speed = random.uniform(0.05, 0.2)  # Simulated time per character in seconds
        typing_duration = len(message) * typing_speed
        print(f"Simulating typing for {len(message)} characters, taking {typing_duration:.2f} seconds.")
        return typing_duration

    def execute_with_typing_delay(self, func, message, urgency_level="normal", *args, **kwargs):
        """
        Simulates typing for a chat message, followed by a pause, then executes the chat sending function.
        
        Args:
        - func (callable): The function to execute after the typing delay.
        - message (str): The chat message to be typed and sent.
        - urgency_level (str): The urgency level of the situation which affects the overall delay.
        - *args, **kwargs: Arguments to pass to the function being delayed.
        
        Returns:
        - The result of the function execution after the delay.
        """
        # Simulate typing time based on the message length.
        typing_delay = self.chat_typing_simulation(message)
        time.sleep(typing_delay)

        # Add an additional pause based on urgency level.
        return self.execute_with_delay(func, message, urgency_level=urgency_level, *args, **kwargs)

# Example usage of TimingManager in chat
if __name__ == "__main__":
    def send_chat_message(message):
        print(f"Sending chat message: {message}")

    # Initialize TimingManager with custom delay ranges
    timing_manager = TimingManager(min_delay=1.5, max_delay=4.0)

    # Simulate sending a message with normal urgency
    timing_manager.execute_with_typing_delay(send_chat_message, "I'm not sure about this one...", urgency_level="normal")

    # Simulate sending a message with low urgency
    timing_manager.execute_with_typing_delay(send_chat_message, "Nice hand!", urgency_level="low")

    # Simulate sending a message with high urgency
    timing_manager.execute_with_typing_delay(send_chat_message, "I'm all-in!", urgency_level="urgent")
