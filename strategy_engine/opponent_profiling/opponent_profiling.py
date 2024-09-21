# opponent_profiling.py

import json
import os

class OpponentProfile:
    """
    A class to represent and manage an opponent's profile, tracking their behavior over time.
    """

    def __init__(self, player_id):
        self.player_id = player_id
        self.hands_played = 0
        self.aggressiveness = 0.0
        self.passiveness = 0.0
        self.bluffing_frequency = 0.0
        self.fold_frequency = 0.0
        self.bet_sizes = []
        self.opponent_type = "Unknown"

    def update_profile(self, action, bet_size=None):
        """
        Updates the opponent profile based on the action taken by the opponent in the game.

        Args:
            action (str): The action taken by the opponent (e.g., 'raise', 'fold', 'check', 'bet', 'bluff').
            bet_size (float, optional): The size of the opponent's bet if applicable.
        """
        self.hands_played += 1

        if action == "raise":
            self.aggressiveness += 1
        elif action == "fold":
            self.fold_frequency += 1
        elif action == "bluff":
            self.bluffing_frequency += 1
        elif action == "check":
            self.passiveness += 1
        elif action == "bet" and bet_size:
            self.bet_sizes.append(bet_size)

        self.classify_opponent()

    def classify_opponent(self):
        """
        Classifies the opponent based on the collected data. Opponents are classified into four types:
        - Aggressive
        - Passive
        - Tight
        - Loose
        """
        if self.hands_played == 0:
            return

        agg_ratio = self.aggressiveness / self.hands_played
        fold_ratio = self.fold_frequency / self.hands_played
        passive_ratio = self.passiveness / self.hands_played

        if agg_ratio > 0.6:
            self.opponent_type = "Aggressive"
        elif fold_ratio > 0.6:
            self.opponent_type = "Tight"
        elif passive_ratio > 0.6:
            self.opponent_type = "Passive"
        else:
            self.opponent_type = "Loose"

    def get_profile(self):
        """
        Returns a dictionary containing the opponent's profile.
        """
        return {
            "player_id": self.player_id,
            "hands_played": self.hands_played,
            "aggressiveness": self.aggressiveness,
            "passiveness": self.passiveness,
            "bluffing_frequency": self.bluffing_frequency,
            "fold_frequency": self.fold_frequency,
            "bet_sizes": self.bet_sizes,
            "opponent_type": self.opponent_type
        }


class OpponentProfiler:
    """
    A class responsible for managing multiple opponent profiles and updating them in real-time.
    """

    def __init__(self):
        self.opponent_profiles = {}

    def load_profiles(self, file_path):
        """
        Loads existing opponent profiles from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing opponent profiles.
        """
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.opponent_profiles = json.load(file)

    def save_profiles(self, file_path):
        """
        Saves the current opponent profiles to a JSON file.

        Args:
            file_path (str): Path to the JSON file where profiles will be saved.
        """
        with open(file_path, 'w') as file:
            json.dump(self.opponent_profiles, file, indent=4)

    def update_opponent(self, player_id, action, bet_size=None):
        """
        Updates the profile of a specific opponent based on their latest action.

        Args:
            player_id (str): The unique identifier of the opponent.
            action (str): The action taken by the opponent (e.g., 'raise', 'fold', 'check', 'bet', 'bluff').
            bet_size (float, optional): The size of the opponent's bet if applicable.
        """
        if player_id not in self.opponent_profiles:
            self.opponent_profiles[player_id] = OpponentProfile(player_id).get_profile()

        # Update the opponent's profile with new action
        profile = OpponentProfile(player_id)
        profile.__dict__ = self.opponent_profiles[player_id]
        profile.update_profile(action, bet_size)

        # Save the updated profile back to the dictionary
        self.opponent_profiles[player_id] = profile.get_profile()

    def classify_all_opponents(self):
        """
        Classifies all known opponents based on their current behavior profiles.
        """
        for player_id, profile_data in self.opponent_profiles.items():
            profile = OpponentProfile(player_id)
            profile.__dict__ = profile_data
            profile.classify_opponent()
            self.opponent_profiles[player_id] = profile.get_profile()

    def get_opponent_type(self, player_id):
        """
        Returns the classified type of a specific opponent.

        Args:
            player_id (str): The unique identifier of the opponent.

        Returns:
            str: The classified type of the opponent (e.g., 'Aggressive', 'Passive').
        """
        if player_id in self.opponent_profiles:
            return self.opponent_profiles[player_id]["opponent_type"]
        return "Unknown"


# Example usage
if __name__ == "__main__":
    profiler = OpponentProfiler()

    # Load existing profiles from file
    profiler.load_profiles('opponent_profiles.json')

    # Update an opponent profile
    profiler.update_opponent(player_id='player_123', action='raise')
    profiler.update_opponent(player_id='player_123', action='fold')
    profiler.update_opponent(player_id='player_123', action='bluff')

    # Classify all opponents
    profiler.classify_all_opponents()

    # Save the updated profiles to file
    profiler.save_profiles('opponent_profiles.json')

    # Get the type of a specific opponent
    print(profiler.get_opponent_type('player_123'))
