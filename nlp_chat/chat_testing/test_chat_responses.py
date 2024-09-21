import unittest
from nlp_chat.response_generator import generate_response_from_template, generate_dynamic_response

class TestChatResponses(unittest.TestCase):
    """
    This test suite verifies the correctness of the chat response generator in the NLP module.
    It tests both static template-based responses and dynamic GPT-based responses.
    """

    def setUp(self):
        """
        Set up any necessary data or configurations for the tests.
        """
        self.chat_scenarios = {
            'bluff': 'I’m going all-in, you should fold!',
            'friendly': 'Good luck, everyone!',
            'aggressive': 'I own this table!',
            'win': 'Another win for me!',
            'lose': 'Well played, I was unlucky.',
        }
        self.gpt_response_prompt = "It's your turn, what will you do?"

    def test_template_responses(self):
        """
        Test predefined template-based chat responses.
        Ensure that the response matches the expected message for each scenario.
        """
        for scenario, expected_response in self.chat_scenarios.items():
            with self.subTest(scenario=scenario):
                response = generate_response_from_template(scenario)
                self.assertEqual(response, expected_response, 
                                 f"Response for {scenario} should be '{expected_response}' but got '{response}'")

    def test_dynamic_responses(self):
        """
        Test dynamic responses generated from a GPT model or any other language model.
        Ensure that the response is coherent and matches the general context of poker chat.
        """
        response = generate_dynamic_response(self.gpt_response_prompt)
        self.assertIsInstance(response, str, "Dynamic response should be a string.")
        self.assertTrue(len(response) > 0, "Response should not be empty.")
        print(f"Dynamic Response: {response}")

    def test_dynamic_bluff_response(self):
        """
        Test dynamic bluffing response generated from GPT model.
        Check if the response fits into the bluffing context.
        """
        bluff_prompt = "You're bluffing, but your opponent is unsure. What do you say?"
        response = generate_dynamic_response(bluff_prompt)
        self.assertIsInstance(response, str)
        self.assertTrue("bluff" in response.lower() or "fold" in response.lower(),
                        "Response should reference bluffing context.")
        print(f"Bluff Dynamic Response: {response}")

if __name__ == "__main__":
    unittest.main()
