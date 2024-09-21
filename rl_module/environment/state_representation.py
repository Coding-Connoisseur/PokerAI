# state_representation.py

import numpy as np

class StateRepresentation:
    def __init__(self, num_players=6):
        """
        Initializes the state representation with default values.
        
        Args:
            num_players (int): The number of players at the poker table.
        """
        self.num_players = num_players
        self.state_size = self.get_state_size()

    def get_state_size(self):
        """
        Calculates the size of the state representation vector based on the number of players
        and game elements (e.g., cards, pot size, betting actions).
        
        Returns:
            int: Size of the state representation vector.
        """
        # State vector includes hand cards, community cards, pot size, current bets, player positions, etc.
        hand_size = 2  # Two cards for the AI player
        community_cards_size = 5  # Up to five community cards
        pot_size = 1  # Single value for the pot size
        current_bet_size = 1  # Single value for current bet
        player_info_size = 3 * self.num_players  # For each player: [stack, current bet, is_active]
        
        return hand_size + community_cards_size + pot_size + current_bet_size + player_info_size

    def encode_hand(self, hand):
        """
        Encodes the player's hand into a numeric format.
        
        Args:
            hand (list): List containing two card values for the player's hand.
        
        Returns:
            list: Numeric representation of the hand.
        """
        # Convert hand cards into a numerical representation, e.g., (rank, suit)
        return [self.encode_card(card) for card in hand]

    def encode_card(self, card):
        """
        Encodes a single card into a numerical format.
        
        Args:
            card (str): The card represented as a string (e.g., "AS" for Ace of Spades).
        
        Returns:
            int: Numeric representation of the card.
        """
        rank_conversion = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        suit_conversion = {'H': 1, 'D': 2, 'C': 3, 'S': 4}  # Hearts, Diamonds, Clubs, Spades

        rank = rank_conversion[card[0]]
        suit = suit_conversion[card[1]]
        return rank * 10 + suit  # Combine rank and suit as a unique value

    def encode_community_cards(self, community_cards):
        """
        Encodes the community cards into a numeric format.
        
        Args:
            community_cards (list): List containing up to five card values for the community cards.
        
        Returns:
            list: Numeric representation of the community cards.
        """
        encoded_community_cards = [self.encode_card(card) for card in community_cards]
        while len(encoded_community_cards) < 5:
            encoded_community_cards.append(0)  # Add padding for fewer than 5 cards
        return encoded_community_cards

    def encode_players(self, player_data):
        """
        Encodes the opponent player data (stack, current bet, active status) into numeric form.
        
        Args:
            player_data (list): A list of dictionaries with player information for each opponent.
        
        Returns:
            list: A numeric representation of all player statuses.
        """
        encoded_players = []
        for player in player_data:
            encoded_players.append(player["stack"])
            encoded_players.append(player["current_bet"])
            encoded_players.append(1 if player["is_active"] else 0)  # Active = 1, Inactive = 0
        return encoded_players

    def get_state_representation(self, hand, community_cards, pot_size, current_bet, player_data):
        """
        Combines all the game elements into a single state vector.

        Args:
            hand (list): The player's hand cards.
            community_cards (list): The community cards.
            pot_size (float): The total pot size.
            current_bet (float): The current bet in the round.
            player_data (list): Information about other players (stack sizes, bets, and activity).

        Returns:
            np.array: A state vector representing the entire game state.
        """
        state_vector = []
        
        # Encode the AI's hand
        state_vector.extend(self.encode_hand(hand))
        
        # Encode community cards
        state_vector.extend(self.encode_community_cards(community_cards))
        
        # Add pot size and current bet to the state vector
        state_vector.append(pot_size)
        state_vector.append(current_bet)
        
        # Encode opponent player data
        state_vector.extend(self.encode_players(player_data))
        
        # Return the final state vector as a NumPy array
        return np.array(state_vector)
