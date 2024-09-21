# pot_odds_calculator.py

def calculate_pot_odds(pot_size, bet_to_call):
    """
    Calculates the pot odds, which determine whether calling a bet is mathematically profitable.

    Args:
        pot_size (float): The current size of the pot before the bet.
        bet_to_call (float): The amount the AI needs to call to stay in the hand.

    Returns:
        float: The pot odds percentage, which represents how much of a return the AI gets for calling.
    """
    if bet_to_call <= 0:
        raise ValueError("Bet to call must be greater than zero.")
    
    pot_odds = bet_to_call / (pot_size + bet_to_call)
    return pot_odds * 100  # Return as a percentage

def should_call(pot_size, bet_to_call, hand_equity):
    """
    Determines whether the AI should call a bet based on pot odds and hand equity.

    Args:
        pot_size (float): The size of the pot.
        bet_to_call (float): The amount needed to call the current bet.
        hand_equity (float): The estimated probability (in percentage) of winning the hand based on the AI's cards.

    Returns:
        bool: True if the AI should call, False otherwise.
    """
    pot_odds_percentage = calculate_pot_odds(pot_size, bet_to_call)

    # If hand equity (chance of winning) is higher than the pot odds, calling is profitable
    return hand_equity >= pot_odds_percentage

def calculate_implied_odds(pot_size, bet_to_call, future_bet_estimate):
    """
    Calculates implied odds, which consider potential future earnings if the AI completes a strong hand.

    Args:
        pot_size (float): The current size of the pot.
        bet_to_call (float): The amount needed to call the current bet.
        future_bet_estimate (float): An estimate of additional bets the AI expects to win if it improves.

    Returns:
        float: The implied odds percentage.
    """
    total_pot_with_future_bets = pot_size + future_bet_estimate
    implied_odds = bet_to_call / (total_pot_with_future_bets + bet_to_call)
    return implied_odds * 100  # Return as a percentage

# Example usage:
if __name__ == "__main__":
    # Scenario: pot size is $100, opponent bets $25, and the AI estimates a 35% chance of winning the hand
    pot_size = 100.0
    bet_to_call = 25.0
    hand_equity = 35.0  # AI estimates a 35% chance of winning

    pot_odds = calculate_pot_odds(pot_size, bet_to_call)
    print(f"Pot Odds: {pot_odds:.2f}%")

    if should_call(pot_size, bet_to_call, hand_equity):
        print("The AI should call the bet.")
    else:
        print("The AI should fold.")

    # Implied odds calculation: AI estimates it could win an additional $50 if it hits its hand
    future_bet_estimate = 50.0
    implied_odds = calculate_implied_odds(pot_size, bet_to_call, future_bet_estimate)
    print(f"Implied Odds: {implied_odds:.2f}%")
