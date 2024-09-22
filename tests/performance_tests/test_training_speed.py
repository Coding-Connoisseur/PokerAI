# test_training_speed.py

import time
import logging
from rl_module.train_agent import train_agent

# Configure logging
logging.basicConfig(filename='tests/system_tests/test_training_speed.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def measure_training_speed(episodes=1000):
    """
    Measures the speed of training for the RL agent. It records the total time taken to 
    complete the training for a specified number of episodes.

    Args:
        episodes (int): The number of training episodes to run. Default is 1000.

    Returns:
        float: Total time taken to complete training in seconds.
    """
    logging.info(f"Starting training speed test with {episodes} episodes.")

    # Start timing
    start_time = time.time()

    # Train the agent for the given number of episodes
    train_agent(episodes)

    # End timing
    e
