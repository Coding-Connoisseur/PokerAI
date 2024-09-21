# metrics_logger.py

import os
import json
import logging
from datetime import datetime

# Set up logging
LOG_DIR = "./rl_module/evaluation/logs/"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "metrics.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MetricsLogger:
    def __init__(self, log_file="metrics.json"):
        """
        Initializes the metrics logger.
        
        Args:
            log_file (str): Name of the file to save logged metrics.
        """
        self.log_file = os.path.join(LOG_DIR, log_file)
        self.metrics = {
            "episodes": [],
            "rewards": [],
            "win_rate": [],
            "cumulative_rewards": [],
            "average_q_values": []
        }
    
    def log_episode(self, episode_num, reward, win_rate, avg_q_value):
        """
        Logs metrics for each episode.

        Args:
            episode_num (int): The current episode number.
            reward (float): The reward obtained in this episode.
            win_rate (float): The win rate after this episode.
            avg_q_value (float): The average Q-value for the current episode.
        """
        logging.info(f"Episode {episode_num}: Reward: {reward}, Win Rate: {win_rate}, Avg Q-value: {avg_q_value}")
        
        self.metrics["episodes"].append(episode_num)
        self.metrics["rewards"].append(reward)
        self.metrics["win_rate"].append(win_rate)
        self.metrics["cumulative_rewards"].append(sum(self.metrics["rewards"]))
        self.metrics["average_q_values"].append(avg_q_value)
        
        # Save metrics to file after each episode
        self.save_metrics()

    def save_metrics(self):
        """
        Saves the current metrics to a JSON file.
        """
        with open(self.log_file, 'w') as f:
            json.dump(self.metrics, f, indent=4)
    
    def load_metrics(self):
        """
        Loads existing metrics from the log file (if available).
        """
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                self.metrics = json.load(f)

    def display_latest_metrics(self):
        """
        Displays the latest metrics (last logged episode).
        """
        if self.metrics["episodes"]:
            episode_num = self.metrics["episodes"][-1]
            reward = self.metrics["rewards"][-1]
            win_rate = self.metrics["win_rate"][-1]
            avg_q_value = self.metrics["average_q_values"][-1]
            
            print(f"Episode {episode_num}:")
            print(f" - Reward: {reward}")
            print(f" - Win Rate: {win_rate}")
            print(f" - Average Q-Value: {avg_q_value}")
            print(f" - Cumulative Reward: {self.metrics['cumulative_rewards'][-1]}")
        else:
            print("No metrics logged yet.")
    
    def visualize_metrics(self):
        """
        Visualizes the tracked metrics using matplotlib.
        """
        import matplotlib.pyplot as plt

        # Plot cumulative rewards
        plt.figure(figsize=(10, 6))
        plt.plot(self.metrics["episodes"], self.metrics["cumulative_rewards"], label="Cumulative Rewards")
        plt.title("Cumulative Rewards over Episodes")
        plt.xlabel("Episodes")
        plt.ylabel("Cumulative Rewards")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot win rate
        plt.figure(figsize=(10, 6))
        plt.plot(self.metrics["episodes"], self.metrics["win_rate"], label="Win Rate", color='green')
        plt.title("Win Rate over Episodes")
        plt.xlabel("Episodes")
        plt.ylabel("Win Rate")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot average Q-values
        plt.figure(figsize=(10, 6))
        plt.plot(self.metrics["episodes"], self.metrics["average_q_values"], label="Average Q-Value", color='orange')
        plt.title("Average Q-Value over Episodes")
        plt.xlabel("Episodes")
        plt.ylabel("Average Q-Value")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    logger = MetricsLogger()
    logger.load_metrics()

    # Example usage: logging an episode
    # These values would typically be computed during RL training.
    logger.log_episode(episode_num=10, reward=100, win_rate=0.75, avg_q_value=5.2)
    
    # Display latest metrics
    logger.display_latest_metrics()

    # Visualize metrics
    logger.visualize_metrics()
