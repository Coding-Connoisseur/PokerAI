
# pre_flop_rules.py

"""
Pre-flop strategy engine for PokerAI.
This module determines the optimal action to take pre-flop based on hand strength, table position,
and opponent profiling. The strategy can be adjusted based on the AI's learned experiences.
"""

# Poker hand rankings for pre-flop decisions
POKER_HAND_RANKINGS = {
    'AA': 10, 'KK': 9, 'QQ': 9, 'JJ': 8, 'AKs': 8, 'TT': 7, 'AQs': 7, 'AJs': 7, 'KQs': 7, 
    '99': 6, '88': 6, '77': 5, 'AK': 6, 'AQ': 5, 'AJs': 5, '66': 4, '55': 4, '44': 4,
    '33': 3, '22': 3, 'A2s-A5s': 4  # Example for suited aces
}

# Poker position mapping
POSITION_RANKINGS = {
    'early': -1,   # Tighten range for early position
    'middle': 0,   # Neutral
    'late': 1      # Looser range in late position
}

# Opponent profiling adjustments (placeholders)
OPPONENT_PROFILES = {
    'aggressive': -1,  # Play tighter against aggressive opponents
    'passive': 1,      # Loosen range against passive players
    'neutral': 0       # Neutral play against balanced opponents
}

def evaluate_hand_strength(hand):
    """
    Evaluates the strength of the AI's hand pre-flop based on known hand rankings.
    Args:
        hand (str): The player's hand as a string (e.g., 'AK', '77', 'JTs').
    
    Returns:
        int: A numerical rating of the hand's strength.
    """
    return POKER_HAND_RANKINGS.get(hand, 0)

def evaluate_position(position):
    """
    Adjusts strategy based on table position.
    Args:
        position (str): The player's position at the table ('early', 'middle', 'late').
    
    Returns:
        int: A position adjustment value.
    """
    return POSITION_RANKINGS.get(position, 0)

def evaluate_opponent_profile(profile):
    """
    Adjusts strategy based on opponent profiling.
    Args:
        profile (str): The profile of the key opponents ('aggressive', 'passive', 'neutral').
    
    Returns:
        int: A profile adjustment value.
    """
    return OPPONENT_PROFILES.get(profile, 0)

def make_pre_flop_decision(hand, position, opponent_profile, pot_odds):
    """
    Determines the optimal action to take pre-flop (raise, call, or fold).
    Args:
        hand (str): The player's hand (e.g., 'AK', '77', 'JTs').
        position (str): The player's position at the table ('early', 'middle', 'late').
        opponent_profile (str): The dominant opponent's play style ('aggressive', 'passive', 'neutral').
        pot_odds (float): The current pot odds ratio.

    Returns:
        str: The recommended action ('raise', 'call', 'fold').
    """
    # Evaluate hand strength, position, and opponent profile
    hand_strength = evaluate_hand_strength(hand)
    position_adjustment = evaluate_position(position)
    opponent_adjustment = evaluate_opponent_profile(opponent_profile)

    # Calculate adjusted hand strength
    adjusted_hand_strength = hand_strength + position_adjustment + opponent_adjustment

    # Decision thresholds
    if adjusted_hand_strength >= 9:
        return 'raise'
    elif adjusted_hand_strength >= 5 and pot_odds > 1.5:
        return 'call'
    else:
        return 'fold'

# Example usage
if __name__ == "__main__":
    # Example hand: AI holds 'AK', is in 'late' position, facing a 'passive' opponent, and has pot odds of 2.0
    hand = 'AK'
    position = 'late'
    opponent_profile = 'passive'
    pot_odds = 2.0

    decision = make_pre_flop_decision(hand, position, opponent_profile, pot_odds)
    print(f"Pre-flop decision: {decision}")
