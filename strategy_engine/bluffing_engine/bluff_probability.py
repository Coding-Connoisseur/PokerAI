# bluff_probability.py

import random

class BluffProbabilityCalculator:
    def __init__(self, opponent_profile, hand_strength, pot_odds, aggression_level, game_stage):
        """
        Initializes the bluff probability calculator with relevant factors.
        
        Args:
            opponent_profile (str): The type of opponent (e.g., aggressive, passive).
            hand_strength (float): Numerical value representing the relative strength of the AI's hand.
            pot_odds (float): Current pot odds that might encourage or discourage bluffing.
            aggression_level (float): A dynamic aggression level based on AI's recent actions.
            game_stage (str): The current stage of the game (e.g., pre-flop, post-flop, river).
        """
        self.opponent_profile = opponent_profile
        self.hand_strength = hand_strength
        self.pot_odds = pot_odds
        self.aggression_level = aggression_level
        self.game_stage = game_stage
    
    def calculate_bluff_probability(self):
        """
        Calculates the probability of bluffing based on various factors such as opponent type,
        hand strength, game stage, and aggression level.
        
        Returns:
            float: A probability value between 0 and 1 indicating the likelihood of bluffing.
        """
        base_bluff_chance = self._base_bluff_chance()
        opponent_modifier = self._opponent_modifier()
        hand_strength_modifier = self._hand_strength_modifier()
        pot_odds_modifier = self._pot_odds_modifier()
        game_stage_modifier = self._game_stage_modifier()
        
        # Final bluff probability with all modifiers applied
        bluff_probability = base_bluff_chance * (opponent_modifier + hand_strength_modifier + pot_odds_modifier + game_stage_modifier)
        
        # Clip the bluff probability between 0 and 1
        bluff_probability = min(max(bluff_probability, 0.05), 0.95)  # Always leave a 5-95% chance
        
        return bluff_probability
    
    def _base_bluff_chance(self):
        """
        Establishes a base bluff chance depending on AI's aggression level.
        
        Returns:
            float: Base bluff chance.
        """
        return max(0.1, min(0.4 + self.aggression_level, 0.8))  # Base range from 10% to 80% based on aggression
    
    def _opponent_modifier(self):
        """
        Modifies bluff probability based on the opponent's profile.
        
        Returns:
            float: A multiplier based on opponent type.
        """
        if self.opponent_profile == 'aggressive':
            return 0.8  # Bluff less often against aggressive players
        elif self.opponent_profile == 'passive':
            return 1.2  # Bluff more often against passive players
        elif self.opponent_profile == 'tight':
            return 1.1  # Tight players fold often, so bluff more
        elif self.opponent_profile == 'loose':
            return 0.9  # Loose players call frequently, reduce bluffing
        else:
            return 1.0  # Neutral multiplier for unknown opponents
    
    def _hand_strength_modifier(self):
        """
        Adjusts bluff probability based on the strength of the AI's hand.
        
        Returns:
            float: A modifier value based on hand strength.
        """
        if self.hand_strength > 0.8:  # Strong hand, less need to bluff
            return 0.5
        elif self.hand_strength < 0.3:  # Weak hand, more likely to bluff
            return 1.5
        else:
            return 1.0  # Neutral modifier for medium strength hands
    
    def _pot_odds_modifier(self):
        """
        Modifies bluff probability based on the current pot odds.
        
        Returns:
            float: A modifier based on pot odds.
        """
        if self.pot_odds < 0.2:  # Small pot, more incentive to bluff
            return 1.3
        elif self.pot_odds > 0.5:  # Large pot, less bluffing
            return 0.8
        else:
            return 1.0  # Neutral modifier for average pot odds
    
    def _game_stage_modifier(self):
        """
        Adjusts bluff probability based on the stage of the game.
        
        Returns:
            float: A multiplier based on the game stage.
        """
        if self.game_stage == 'pre-flop':
            return 0.9  # Less bluffing early in the game
        elif self.game_stage == 'flop':
            return 1.1  # Moderate bluffing during the flop
        elif self.game_stage == 'turn':
            return 1.2  # More bluffing on the turn
        elif self.game_stage == 'river':
            return 1.4  # High bluff frequency on the river
        else:
            return 1.0  # Neutral modifier for undefined stages

# Example Usage
if __name__ == "__main__":
    # Example: Bluff probability calculation for an aggressive player, weak hand, and favorable pot odds
    calculator = BluffProbabilityCalculator(
        opponent_profile='aggressive',
        hand_strength=0.2,
        pot_odds=0.3,
        aggression_level=0.7,
        game_stage='river'
    )
    
    bluff_prob = calculator.calculate_bluff_probability()
    print(f"Bluff Probability: {bluff_prob:.2f}")
