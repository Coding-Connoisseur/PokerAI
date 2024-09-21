# hand_evaluation.py

from itertools import combinations

# Define standard poker hand rankings
HAND_RANKINGS = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10
}

def evaluate_hand(player_hand, community_cards):
    """
    Evaluates the strength of the AI's hand after the flop.
    
    Args:
        player_hand (list): A list of two cards held by the player (e.g., ['9H', 'KD']).
        community_cards (list): A list of five community cards on the board (e.g., ['3H', '4S', '5D', '8H', 'KH']).
        
    Returns:
        dict: A dictionary containing the best hand type, value, and the combination of cards used.
    """
    all_cards = player_hand + community_cards
    best_hand = {"type": "High Card", "value": HAND_RANKINGS["High Card"], "cards": []}

    # Check for different hand combinations
    if is_royal_flush(all_cards):
        best_hand = {"type": "Royal Flush", "value": HAND_RANKINGS["Royal Flush"], "cards": all_cards}
    elif is_straight_flush(all_cards):
        best_hand = {"type": "Straight Flush", "value": HAND_RANKINGS["Straight Flush"], "cards": all_cards}
    elif is_four_of_a_kind(all_cards):
        best_hand = {"type": "Four of a Kind", "value": HAND_RANKINGS["Four of a Kind"], "cards": get_hand(all_cards, 4)}
    elif is_full_house(all_cards):
        best_hand = {"type": "Full House", "value": HAND_RANKINGS["Full House"], "cards": get_hand(all_cards, 3, 2)}
    elif is_flush(all_cards):
        best_hand = {"type": "Flush", "value": HAND_RANKINGS["Flush"], "cards": get_flush_cards(all_cards)}
    elif is_straight(all_cards):
        best_hand = {"type": "Straight", "value": HAND_RANKINGS["Straight"], "cards": get_straight(all_cards)}
    elif is_three_of_a_kind(all_cards):
        best_hand = {"type": "Three of a Kind", "value": HAND_RANKINGS["Three of a Kind"], "cards": get_hand(all_cards, 3)}
    elif is_two_pair(all_cards):
        best_hand = {"type": "Two Pair", "value": HAND_RANKINGS["Two Pair"], "cards": get_two_pair(all_cards)}
    elif is_pair(all_cards):
        best_hand = {"type": "One Pair", "value": HAND_RANKINGS["One Pair"], "cards": get_hand(all_cards, 2)}

    return best_hand

def is_flush(cards):
    """
    Checks if the hand is a flush (5 cards of the same suit).
    
    Args:
        cards (list): List of cards in the hand.
        
    Returns:
        bool: True if the hand is a flush, False otherwise.
    """
    suits = [card[-1] for card in cards]
    return max(suits.count(suit) for suit in set(suits)) >= 5

def is_straight(cards):
    """
    Checks if the hand is a straight (5 cards in sequence).
    
    Args:
        cards (list): List of cards in the hand.
        
    Returns:
        bool: True if the hand is a straight, False otherwise.
    """
    ranks = sorted([card_value(card[:-1]) for card in cards])
    return any(all(ranks[i + j] == ranks[i] + j for j in range(5)) for i in range(len(ranks) - 4))

def is_straight_flush(cards):
    """
    Checks if the hand is a straight flush (5 consecutive cards of the same suit).
    
    Args:
        cards (list): List of cards in the hand.
        
    Returns:
        bool: True if the hand is a straight flush, False otherwise.
    """
    return is_flush(cards) and is_straight(cards)

def is_royal_flush(cards):
    """
    Checks if the hand is a royal flush (10, J, Q, K, A of the same suit).
    
    Args:
        cards (list): List of cards in the hand.
        
    Returns:
        bool: True if the hand is a royal flush, False otherwise.
    """
    return is_straight_flush(cards) and set(card_value(card[:-1]) for card in cards) == {10, 11, 12, 13, 14}

def is_four_of_a_kind(cards):
    return has_same_rank(cards, 4)

def is_full_house(cards):
    return has_same_rank(cards, 3) and has_same_rank(cards, 2)

def is_three_of_a_kind(cards):
    return has_same_rank(cards, 3)

def is_two_pair(cards):
    return len([rank for rank in set(card_value(card[:-1]) for card in cards) if cards.count(rank) == 2]) >= 2

def is_pair(cards):
    return has_same_rank(cards, 2)

def has_same_rank(cards, count):
    ranks = [card_value(card[:-1]) for card in cards]
    return any(ranks.count(rank) == count for rank in set(ranks))

def get_hand(cards, primary_count, secondary_count=None):
    """
    Returns the cards that form the best combination for a hand, such as a Full House or Four of a Kind.
    """
    ranks = sorted([card_value(card[:-1]) for card in cards], reverse=True)
    if secondary_count:
        return ranks[:primary_count] + ranks[-secondary_count:]
    return ranks[:primary_count]

def card_value(card):
    """
    Converts card rank into numerical values. E.g., A -> 14, K -> 13, Q -> 12, J -> 11.
    
    Args:
        card (str): The rank of the card as a string.
        
    Returns:
        int: The numerical value of the card rank.
    """
    if card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 11
    else:
        return int(card)

def get_flush_cards(cards):
    """
    Returns the cards that form a flush.
    """
    suits = [card[-1] for card in cards]
    flush_suit = max(set(suits), key=suits.count)
    return [card for card in cards if card[-1] == flush_suit]

def get_straight(cards):
    """
    Returns the cards that form a straight.
    """
    ranks = sorted([card_value(card[:-1]) for card in cards])
    for i in range(len(ranks) - 4):
        if all(ranks[i + j] == ranks[i] + j for j in range(5)):
            return ranks[i:i + 5]
    return None

if __name__ == "__main__":
    # Example usage:
    player_hand = ['9H', 'KD']
    community_cards = ['3H', '4S', '5D', '8H', 'KH']
    result = evaluate_hand(player_hand, community_cards)
    print(f"Best hand: {result['type']}, Cards: {result['cards']}")
