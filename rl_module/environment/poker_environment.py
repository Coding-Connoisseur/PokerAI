import numpy as np
import random

class PokerEnvironment:
    """
    A simulation environment for poker gameplay, designed to interface with reinforcement learning agents.
    This environment handles poker mechanics such as dealing cards, handling betting rounds, and determining winners.
    """

    def __init__(self, num_players=6):
        """
        Initialize the poker environment.

        Args:
            num_players (int): The number of players at the poker table (including the RL agent).
        """
        self.num_players = num_players
        self.deck = self.create_deck()
        self.community_cards = []
        self.player_hands = [[] for _ in range(self.num_players)]
        self.pot = 0
        self.betting_round = 0
        self.agent_position = random.randint(0, self.num_players - 1)
        self.current_player = 0
        self.bets = [0] * self.num_players

    def create_deck(self):
        """
        Creates and shuffles a standard deck of 52 cards.
        
        Returns:
            list: A shuffled deck of cards.
        """
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [f'{rank} of {suit}' for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def reset(self):
        """
        Resets the environment for a new game of poker.

        Returns:
            dict: The initial game state.
        """
        self.deck = self.create_deck()
        self.community_cards = []
        self.player_hands = [[] for _ in range(self.num_players)]
        self.pot = 0
        self.betting_round = 0
        self.bets = [0] * self.num_players
        self.deal_hands()

        return self.get_game_state()

    def deal_hands(self):
        """
        Deals two hole cards to each player.
        """
        for i in range(self.num_players):
            self.player_hands[i] = [self.deck.pop(), self.deck.pop()]

    def deal_community_cards(self, num_cards):
        """
        Deals community cards (flop, turn, or river).
        
        Args:
            num_cards (int): The number of community cards to deal.
        """
        for _ in range(num_cards):
            self.community_cards.append(self.deck.pop())

    def get_game_state(self):
        """
        Retrieves the current game state.

        Returns:
            dict: A dictionary containing the agent's hand, community cards, pot, and betting info.
        """
        return {
            "agent_hand": self.player_hands[self.agent_position],
            "community_cards": self.community_cards,
            "pot": self.pot,
            "bets": self.bets,
            "betting_round": self.betting_round,
            "current_player": self.current_player
        }

    def step(self, action):
        """
        Executes the given action and advances the game.

        Args:
            action (int): The action taken by the current player (fold, call, raise, etc.).

        Returns:
            tuple: A tuple of (next_state, reward, done, info)
        """
        reward = 0
        done = False
        info = {}

        if action == "fold":
            reward = -1
            done = True
        elif action == "call":
            call_amount = max(self.bets) - self.bets[self.current_player]
            self.pot += call_amount
            self.bets[self.current_player] += call_amount
        elif action == "raise":
            raise_amount = random.randint(10, 50)  # Example raise logic
            self.pot += raise_amount
            self.bets[self.current_player] += raise_amount
        else:
            raise ValueError(f"Unknown action: {action}")

        # Move to the next player
        self.current_player = (self.current_player + 1) % self.num_players

        # Check if round is complete (i.e., all players have acted)
        if self.current_player == 0:
            self.betting_round += 1

        # Deal community cards based on betting round
        if self.betting_round == 1:  # Flop
            self.deal_community_cards(3)
        elif self.betting_round == 2:  # Turn
            self.deal_community_cards(1)
        elif self.betting_round == 3:  # River
            self.deal_community_cards(1)

        # Check if the game is finished
        if self.betting_round > 3:
            done = True
            reward = self.calculate_winner()

        next_state = self.get_game_state()
        return next_state, reward, done, info

    def calculate_winner(self):
        """
        Determines the winner of the hand and distributes the pot.

        Returns:
            int: The reward for the agent (based on whether they win or lose).
        """
        # Example random winner determination for simplicity
        winning_player = random.randint(0, self.num_players - 1)
        if winning_player == self.agent_position:
            return self.pot  # Agent wins the pot
        else:
            return -self.pot  # Agent loses the pot
