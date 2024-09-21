# evaluate_model.py

import argparse
import os
import numpy as np
from rl_module.agents import DQNAgent, QLearningAgent  # Assuming these are implemented
from environment.poker_environment import PokerEnvironment  # Assuming this environment exists
from rl_module.metrics_logger import MetricsLogger  # Assuming this handles logging
import matplotlib.pyplot as plt

def load_agent(agent_type, model_path, env):
    """
    Loads the specified RL agent and its trained model.

    Args:
        agent_type (str): Type of agent ('dqn' or 'qlearning').
        model_path (str): Path to the trained model.
        env (PokerEnvironment): Poker environment for evaluation.

    Returns:
        agent: The loaded RL agent.
    """
    if agent_type == "dqn":
        agent = DQNAgent(env)
        agent.load_model(model_path)
    elif agent_type == "qlearning":
        agent = QLearningAgent(env)
        agent.load_q_table(model_path)
    else:
        raise ValueError(f"Unsupported agent type: {agent_type}")
    
    return agent

def evaluate_agent(agent, env, episodes=100):
    """
    Evaluates the performance of the agent over a specified number of episodes.

    Args:
        agent: The RL agent to evaluate.
        env (PokerEnvironment): The environment to run evaluations in.
        episodes (int): Number of episodes to run.

    Returns:
        dict: Performance metrics including win rates and rewards.
    """
    total_rewards = []
    wins = 0

    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_reward = 0

        while not done:
            action = agent.act(state)
            next_state, reward, done, info = env.step(action)
            episode_reward += reward
            state = next_state

            if done:
                if info.get('win', False):
                    wins += 1

        total_rewards.append(episode_reward)

    win_rate = wins / episodes
    avg_reward = np.mean(total_rewards)

    return {
        "win_rate": win_rate,
        "average_reward": avg_reward,
        "total_rewards": total_rewards
    }

def visualize_results(results):
    """
    Generates visualizations for the evaluation results.

    Args:
        results (dict): The evaluation metrics (win_rate, total_rewards, etc.).
    """
    plt.figure(figsize=(10, 5))

    # Plot reward curve
    plt.subplot(1, 2, 1)
    plt.plot(results["total_rewards"], label='Rewards per episode')
    plt.title('Episode Rewards')
    plt.xlabel('Episodes')
    plt.ylabel('Rewards')
    plt.legend()

    # Plot win rate
    plt.subplot(1, 2, 2)
    plt.bar(['Win Rate'], [results['win_rate']], color='green')
    plt.ylim(0, 1)
    plt.title('Win Rate')
    
    plt.tight_layout()
    plt.show()

def save_results(results, output_dir):
    """
    Saves the evaluation results to a log file and visualizations.

    Args:
        results (dict): Evaluation metrics.
        output_dir (str): Directory to save the results.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Save the metrics to a log file
    log_path = os.path.join(output_dir, 'evaluation_results.txt')
    with open(log_path, 'w') as f:
        f.write(f"Win Rate: {results['win_rate']:.2f}\n")
        f.write(f"Average Reward: {results['average_reward']:.2f}\n")
        f.write(f"Total Rewards: {results['total_rewards']}\n")

    print(f"Results saved to {log_path}")

def main(agent_type, model_path, output_dir, episodes):
    """
    Main function to evaluate the RL model.

    Args:
        agent_type (str): Type of RL agent (either 'dqn' or 'qlearning').
        model_path (str): Path to the trained model file.
        output_dir (str): Directory to save evaluation results.
        episodes (int): Number of episodes to run for evaluation.
    """
    # Initialize the environment
    env = PokerEnvironment()

    # Load the trained agent
    agent = load_agent(agent_type, model_path, env)

    # Evaluate the agent's performance
    results = evaluate_agent(agent, env, episodes)

    # Visualize results
    visualize_results(results)

    # Save results
    save_results(results, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a trained RL model")
    parser.add_argument('--agent_type', type=str, required=True, help="Type of agent ('dqn' or 'qlearning')")
    parser.add_argument('--model_path', type=str, required=True, help="Path to the trained model file")
    parser.add_argument('--output_dir', type=str, default="./results", help="Directory to save evaluation results")
    parser.add_argument('--episodes', type=int, default=100, help="Number of episodes to run for evaluation")

    args = parser.parse_args()

    main(args.agent_type, args.model_path, args.output_dir, args.episodes)
