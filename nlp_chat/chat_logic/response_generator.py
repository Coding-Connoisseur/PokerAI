# response_generator.py

import random
import time
import yaml
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load GPT-based model for generating chat responses
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Load conversation templates from config
with open('../config/chat_config.yaml', 'r') as file:
    chat_config = yaml.safe_load(file)

# Load specific categories of responses
BLUFF_RESPONSES = chat_config['bluff_responses']
BANTER_RESPONSES = chat_config['banter_responses']
STRATEGIC_RESPONSES = chat_config['strategic_responses']
RESPONSE_DELAY = chat_config['response_delay']

class ResponseGenerator:
    """
    Class responsible for generating NLP-based chat responses during poker games.
    The responses are either template-based or dynamically generated using GPT.
    """
    def __init__(self, game_state):
        """
        Initializes the response generator with the current game state.
        :param game_state: A dictionary or object containing relevant game state data.
        """
        self.game_state = game_state

    def generate_gpt_response(self, prompt):
        """
        Generates a dynamic response using GPT based on a game situation.
        :param prompt: The context or prompt based on which GPT will generate a response.
        :return: Generated chat response.
        """
        inputs = tokenizer.encode(prompt, return_tensors='pt')
        outputs = model.generate(inputs, max_length=100, do_sample=True, temperature=0.7)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def select_template_response(self, situation):
        """
        Selects an appropriate template-based response based on the game situation.
        :param situation: A string indicating the current game situation (e.g., 'bluff', 'banter', 'strategic').
        :return: A response string from the corresponding category.
        """
        if situation == 'bluff':
            return random.choice(BLUFF_RESPONSES)
        elif situation == 'banter':
            return random.choice(BANTER_RESPONSES)
        elif situation == 'strategic':
            return random.choice(STRATEGIC_RESPONSES)
        else:
            return "Let's play!"

    def send_response(self, response):
        """
        Simulates sending a chat message to the poker table, with a delay to mimic human-like interaction.
        :param response: The chat message to be sent.
        """
        time.sleep(RESPONSE_DELAY)  # Simulate typing delay
        print(f"AI Chat: {response}")  # Replace this with the actual chat system interface

    def determine_situation(self):
        """
        Determines the current game situation based on the game state.
        This can include situations like bluffing, friendly banter, or strategic moves.
        :return: A string indicating the determined situation ('bluff', 'banter', 'strategic').
        """
        # Example of determining situations (expand based on actual game logic)
        if self.game_state['ai_action'] == 'bluff':
            return 'bluff'
        elif self.game_state['recent_win']:
            return 'banter'
        elif self.game_state['opponent_move'] == 'big_raise':
            return 'strategic'
        else:
            return 'banter'

    def generate_response(self):
        """
        Main function to generate a response based on the current game situation.
        It will either use a template or generate a response dynamically using GPT.
        :return: The generated chat response.
        """
        situation = self.determine_situation()
        
        if situation in ['bluff', 'banter', 'strategic']:
            # Select a template-based response
            response = self.select_template_response(situation)
        else:
            # If no suitable template, generate a GPT-based response
            prompt = f"The AI is playing poker and {self.game_state['ai_action']} just happened."
            response = self.generate_gpt_response(prompt)
        
        return response

# Example usage:
if __name__ == "__main__":
    # Mock game state to test the response generator
    game_state = {
        'ai_action': 'bluff',
        'recent_win': False,
        'opponent_move': 'big_raise'
    }

    # Initialize response generator with game state
    response_gen = ResponseGenerator(game_state)
    
    # Generate and send response
    chat_response = response_gen.generate_response()
    response_gen.send_response(chat_response)
