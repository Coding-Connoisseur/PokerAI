# run_simulation.py

"""
This script runs a full poker simulation using the trained reinforcement learning (RL) agents
and the strategy engine. The simulation can be used to evaluate the AI’s performance in a real-world poker environment.
This script integrates the RL agent, strategy engine, and browser automation.
"""

import argparse
from rl_module.train_agent import load_trained_agent
from strategy_engine.decision_maker import DecisionMaker
from browser_automation.scripts.enter_game import enter_poker_game
from browser_automation.scripts.place_bet import place_bet
from browser_automation.scripts.read_game_state import get_game_state
from nlp_chat.response_generator import generate_chat_response

def run_poker_simulation(agent, num_hands=100):
    """
    Simulates a poker game for a specified number of hands.

    Args:
        agent: The trained RL agent used for decision-making.
        num_hands: Number of hands to simulate (default: 100).
    
    Steps:
    - Enters the poker game using browser automation.
    - For each hand, reads the game state and decides whether to fold, raise, call, or bluff.
    - Places bets using the browser automation module.
    - Generates chat responses using the NLP engine.
    - Logs results and performance metrics for each hand.
    """
    print(f"Starting poker simulation with {num_hands} hands...")
    
    # Step 1: Enter the poker game using browser automation
    enter_poker_game()

    # Step 2: Run the simulation for the specified number of hands
    for hand_number in range(1, num_hands + 1):
        print(f"Simulating hand {hand_number}...")

        # Read the current game state from the poker table
        game_state = get_game_state()

        # Get the AI's decision based on the game state using the RL agent and strategy engine
        action = agent.make_decision(game_state)

        # Log the action and game state
        print(f"Game state: {game_state}")
        print(f"AI's action: {action}")

        # Place the bet in the browser based on the AI’s decision
        place_bet(action)

        # Generate a chat response using NLP if appropriate
        chat_response = generate_chat_response(game_state, action)
        if chat_response:
            print(f"AI chat response: {chat_response}")
        
        # (Optional) Log or store the results of each hand for analysis

    print("Simulation complete.")

def main():
    """
    Main function to set up and run the poker simulation.
    Handles command-line arguments for agent selection and number of hands.
    """
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Run a poker simulation with the trained AI agent.")
    parser.add_argument('--agent', type=str, required=True, help="Path to the trained agent model file.")
    parser.add_argument('--hands', type=int, default=100, help="Number of hands to simulate (default: 100).")

    args = parser.parse_args()

    # Step 1: Load the trained RL agent
    agent = load_trained_agent(args.agent)

    # Step 2: Run the poker simulation
    run_poker_simulation(agent, num_hands=args.hands)

if __name__ == "__main__":
    main()
