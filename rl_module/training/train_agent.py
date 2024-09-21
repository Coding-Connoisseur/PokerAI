import os
import numpy as np
import yaml
from rl_module.agents.q_learning_agent import QLearningAgent
from rl_module.agents.dqn_agent import DQNAgent
from rl_module.environment.poker_environment import PokerEnvironment
from rl_module.utils.metrics_logger import MetricsLogger

# Load configuration settings
CONFIG_PATH = './config/rl_config.yaml'

def load_config():
    """
    Load the configuration settings for RL training.
    """
    with open(CONFIG_PATH, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def setup_environment(config):
    """
    Set up the poker environment for training.
    
    Args:
        config (dict): Configuration dictionary with environment parameters.
        
    Returns:
        PokerEnvironment: The poker environment object initialized with configuration.
    """
    return PokerEnvironment(config['environment'])

def initialize_agent(config, environment):
    """
    Initialize the RL agent (Q-Learning or DQN).
    
    Args:
        config (dict): Configuration dictionary with agent parameters.
        environment (PokerEnvironment): The poker environment object.
    
    Returns:
        agent: An instance of QLearningAgent or DQNAgent based on the configuration.
    """
    agent_type = config['agent']['type']
    
    if agent_type == 'q_learning':
        return QLearningAgent(environment, **config['agent']['q_learning'])
    elif agent_type == 'dqn':
        return DQNAgent(environment, **config['agent']['dqn'])
    else:
        raise ValueError(f"Unsupported agent type: {agent_type}")

def train_agent(agent, environment, config):
    """
    Train the RL agent within the poker environment.
    
    Args:
        agent: The RL agent (Q-Learning or DQN).
        environment (PokerEnvironment): The poker environment.
        config (dict): Training configuration parameters.
    """
    episodes = config['training']['episodes']
    max_steps = config['training']['max_steps']
    logger = MetricsLogger(config['logging']['log_dir'])

    for episode in range(episodes):
        state = environment.reset()
        total_reward = 0

        for step in range(max_steps):
            action = agent.select_action(state)
            next_state, reward, done = environment.step(action)

            # Update agent with new experience
            agent.update(state, action, reward, next_state, done)
            total_reward += reward
            state = next_state

            if done:
                break

        # Log the performance of the agent for this episode
        logger.log(episode, total_reward)

        if episode % config['logging']['log_interval'] == 0:
            print(f"Episode {episode}/{episodes} - Total Reward: {total_reward}")

    agent.save(config['training']['save_path'])

def main():
    """
    Main function to load config, setup the environment, initialize the agent, and run training.
    """
    config = load_config()
    environment = setup_environment(config)
    agent = initialize_agent(config, environment)
    train_agent(agent, environment, config)

if __name__ == "__main__":
    main()
