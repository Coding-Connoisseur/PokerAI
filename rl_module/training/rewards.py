# rewards.py

class RewardCalculator:
    """
    Calculates the rewards for the AI agent based on the outcome of each hand of poker.
    The rewards are designed to guide the reinforcement learning agent towards optimal decision-making
    by assigning positive or negative values based on the result of the game state.
    """

    def __init__(self, win_reward=1.0, lose_penalty=-1.0, fold_penalty=-0.5, bluff_reward=0.5):
        """
        Initializes the RewardCalculator with the following parameters:
        
        Args:
            win_reward (float): The reward for winning a hand.
            lose_penalty (float): The penalty for losing a hand.
            fold_penalty (float): The penalty for folding (optional, to encourage aggressive play).
            bluff_reward (float): The reward for successfully bluffing opponents.
        """
        self.win_reward = win_reward
        self.lose_penalty = lose_penalty
        self.fold_penalty = fold_penalty
        self.bluff_reward = bluff_reward

    def calculate_reward(self, action, game_state):
        """
        Calculates the reward based on the current game state and the action taken by the AI.
        
        Args:
            action (str): The action taken by the agent (e.g., 'win', 'lose', 'fold', 'bluff').
            game_state (dict): The current state of the poker game, containing necessary game details.

        Returns:
            float: The reward value.
        """
        if action == 'win':
            return self.win_reward
        elif action == 'lose':
            return self.lose_penalty
        elif action == 'fold':
            return self.fold_penalty
        elif action == 'bluff' and game_state.get("bluff_success", False):
            return self.bluff_reward
        else:
            return 0  # No reward or penalty for actions that aren't specified

    def adjust_for_pot_size(self, reward, pot_size):
        """
        Adjusts the reward based on the size of the pot to encourage higher-stakes play.
        
        Args:
            reward (float): The base reward value.
            pot_size (float): The size of the current pot in the game.
            
        Returns:
            float: Adjusted reward based on pot size.
        """
        return reward * (1 + pot_size / 100)  # Scale the reward proportionally to the pot size

    def calculate_final_reward(self, action, game_state):
        """
        Combines all reward calculations to determine the final reward for the agent's action.
        
        Args:
            action (str): The action taken by the agent (e.g., 'win', 'lose', 'fold', 'bluff').
            game_state (dict): The current game state.

        Returns:
            float: The final reward value for the agent's action.
        """
        base_reward = self.calculate_reward(action, game_state)
        pot_size = game_state.get("pot_size", 0)
        final_reward = self.adjust_for_pot_size(base_reward, pot_size)
        return final_reward

# Example Usage:
if __name__ == "__main__":
    reward_calculator = RewardCalculator()

    # Simulating different game scenarios
    game_state_win = {"pot_size": 100, "bluff_success": False}
    game_state_bluff = {"pot_size": 50, "bluff_success": True}
    game_state_lose = {"pot_size": 80, "bluff_success": False}

    # Calculating rewards for different actions
    print("Win Reward:", reward_calculator.calculate_final_reward('win', game_state_win))
    print("Bluff Reward:", reward_calculator.calculate_final_reward('bluff', game_state_bluff))
    print("Lose Reward:", reward_calculator.calculate_final_reward('lose', game_state_lose))
