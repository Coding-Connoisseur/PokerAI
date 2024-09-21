# evaluate_agent.py

import os
import json
import numpy as np
from rl_module.agents.q_learning_agent import QLearningAgent
from rl_module.environment.poker_environment import PokerEnvironment
from rl_module.metrics_logger import MetricsLogger

# Directory for loading agent models and logging evaluation results
MODEL_DIR = "./rl_module/models/"
LOG_DIR = "./rl_module/evaluation/logs/"

# Evaluation parameters
NUM_EPISODES = 100  # Number of test episodes to evaluate the agent

def load_agent(model_path):
    """
    Loads a pre-trained RL agent from the specified model path.

    Args:
        model_path (str): Path to the model file.

    Returns:
        agent (QLearningAgent): The loaded agent.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    
    with open(model_path, 'r') as file:
        agent_data = json.load(file)
    
    agent = QLearningAgent(**agent_data['config'])
    agent.q_table = np.array(agent_data['q_table'])
    
    return agent

def evaluate_agent(agent, environment, num_episodes):
    """
    Evaluates the RL agent by running it through a series of test episodes.

    Args:
        agent (QLearningAgent): The agent to be evaluated.
        environment (PokerEnvironment): The poker environment to test in.
        num_episodes (int): The number of episodes to run.

    Returns:
        dict: A dictionary containing evaluation metrics (e.g., win rate, cumulative rewards).
    """
    total_rewards = 0
    wins = 0
    losses = 0
    metrics = {
        'total_rewards': 0,
        'wins': 0,
        'losses': 0,
        'actions': []
    }

    for episode in range(num_episodes):
        state = environment.reset()
        done = False
        episode_reward = 0

        while not done:
            action = agent.select_action(state)
            next_state, reward, done, info = environment.step(action)
            state = next_state
            episode_reward += reward

            # Log the action
            metrics['actions'].append({
                'episode': episode,
                'state': state.tolist(),
                'action': action,
                'reward': reward
            })

        total_rewards += episode_reward
        metrics['total_rewards'] = total_rewards

        if episode_reward > 0:
            wins += 1
        else:
            losses += 1

    # Calculate win rate and loss rate
    metrics['win_rate'] = wins / num_episodes
    metrics['loss_rate'] = losses / num_episodes
    return metrics

def log_evaluation_results(metrics, log_dir):
    """
    Logs the evaluation metrics into a JSON file for future analysis.

    Args:
        metrics (dict): The evaluation metrics to be logged.
        log_dir (str): Directory where the log files will be stored.
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file_path = os.path.join(log_dir, 'evaluation_metrics.json')
    
    with open(log_file_path, 'w') as log_file:
        json.dump(metrics, log_file, indent=4)
    
    print(f"Evaluation results logged at {log_file_path}")

def main():
    """
    Main function to load the agent, run the evaluation, and log the results.
    """
    model_path = os.path.join(MODEL_DIR, 'trained_agent.json')
    
    print("Loading agent...")
    agent = load_agent(model_path)
    
    print("Setting up poker environment...")
    environment = PokerEnvironment()
    
    print(f"Evaluating agent over {NUM_EPISODES} episodes...")
    metrics = evaluate_agent(agent, environment, NUM_EPISODES)
    
    print("Logging evaluation results...")
    log_evaluation_results(metrics, LOG_DIR)
    
    print("Evaluation complete!")

if __name__ == "__main__":
    main()
