
# **AI Poker Player - Reinforcement Learning and Poker Strategy Engine**

## Overview

This project is a comprehensive AI-powered poker-playing system that combines **Reinforcement Learning (RL)** with a sophisticated **Poker Strategy Engine** to simulate a user that can play poker autonomously. The AI is designed to not only follow optimal poker strategies but also adapt and learn through thousands of simulated games, improving its performance over time.

### Key Features:
- **Game Logic & Strategy Engine**: Evaluates hand strength, calculates pot odds, and incorporates advanced strategies like bluffing, value betting, and opponent profiling.
- **Reinforcement Learning (RL)**: Trains the AI over multiple game episodes to continuously improve its decision-making using Q-learning or Deep Q-Networks (DQN).
- **Browser Automation (Selenium)**: Simulates user interactions, including logging into poker platforms, making decisions, and performing actions like betting, folding, and chatting with other players.
- **NLP Chat (GPT)**: Enhances human-like behavior by participating in game chats, bluffing, and interacting naturally with other players.

---

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Features](#features)
   - [Poker Strategy Engine](#poker-strategy-engine)
   - [Reinforcement Learning Module](#reinforcement-learning-module)
   - [Browser Interaction Module](#browser-interaction-module)
   - [NLP Chat Module](#nlp-chat-module)
4. [How It Works](#how-it-works)
5. [Training the AI](#training-the-ai)
6. [Usage](#usage)
7. [Future Enhancements](#future-enhancements)
8. [License](#license)

---

## Installation

### Requirements

- **Python 3.7+**
- **Selenium** (for browser automation)
- **OpenAI GPT** (for natural language processing)
- **TensorFlow/PyTorch** (for Deep Q-Networks, if using DQN)
- **NumPy** (for matrix operations in Q-learning)
- **Other Dependencies**:
  - `pip install -r requirements.txt`

### Steps to Install:

1. Clone the repository:

   ```bash
   git clone https://github.com/Coding-Connoisseur/ai-poker-player.git
   cd ai-poker-player
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up OpenAI API credentials for the **NLP Chat Module**:
   
   - Create an account on [OpenAI](https://beta.openai.com/signup/).
   - Get your API key and set it in your environment:
     ```bash
     export OPENAI_API_KEY='your-api-key'
     ```

4. Install a **WebDriver** (e.g., ChromeDriver for Selenium):

   - Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system’s PATH.

---

## Project Structure

```plaintext
├── README.md           # Project documentation
├── requirements.txt    # Project dependencies
├── src
│   ├── ai_poker_player.py       # Main execution script
│   ├── strategy_engine.py       # Poker logic and strategy engine
│   ├── reinforcement_learning.py# Q-learning or DQN logic
│   ├── browser_interaction.py   # Selenium automation for poker platforms
│   ├── nlp_chat.py              # GPT-based chat module
│   ├── train.py                 # AI training script
│   └── utils.py                 # Helper functions
```

---

## Features

### 1. **Poker Strategy Engine**

- **Hand Evaluation**: Assesses the player's hand and determines its strength relative to community cards.
- **Pot Odds Calculation**: Determines whether calling a bet is profitable based on pot odds.
- **Advanced Strategies**:
  - **Bluffing**: The AI decides when to bluff based on the board texture and opponent profiling.
  - **Value Betting**: Bets based on maximizing value when holding strong hands.
  - **Opponent Profiling**: Tracks opponent tendencies (tight/aggressive/loose/passive) and adjusts strategies accordingly.

### 2. **Reinforcement Learning Module**

- **Q-Learning**: Standard reinforcement learning algorithm for learning from experience.
- **Deep Q-Networks (DQN)** (optional): Uses a neural network to estimate Q-values for complex environments with a large state space.
- **Reward System**: Assigns rewards based on hand outcomes (win/lose, successful bluff, optimal fold).

### 3. **Browser Interaction Module**

- **Selenium**: Automates user interaction with poker platforms, including logging in, reading game states, and performing actions (e.g., bet, fold, raise).
- **Anti-Detection Mechanisms**: Adds randomized delays and actions to simulate human behavior and evade bot detection.

### 4. **NLP Chat Module**

- **GPT-based Conversation**: Uses GPT to generate human-like responses in poker chat. This helps the AI blend in with human players, engage in casual conversation, and potentially bluff via chat interactions.
- **Randomized Chat**: Generates varying conversation topics, greetings, and bluff cues to make interactions less repetitive.

---

## How It Works

1. **Initialization**: The browser automation starts and logs into the poker platform using Selenium. The AI observes the current game state, including cards, pot size, and opponent actions.
   
2. **Decision Making**: The AI's **Strategy Engine** makes decisions based on hand strength, pot odds, and opponent tendencies.

3. **Reinforcement Learning**: Based on the outcome of each hand, the AI learns from its mistakes and adjusts its strategy over time.

4. **Human-Like Behavior**: The **NLP Chat Module** interacts with other players using GPT to generate human-like responses, contributing to the realism of the AI's behavior.

---

## Training the AI

The AI can be trained in two environments:
- **Simulated Poker Games**: Train the AI with thousands of hands in a controlled environment.
- **Real Online Poker Platforms**: (Legal and ethical constraints apply) Test and improve the AI's strategy in real-time against human players.

### Running the Training Loop

```bash
python src/train.py
```

The training loop plays through multiple poker games, updating the Q-table (or neural network for DQN) after each hand. The AI continuously improves by learning from its experiences.

---

## Usage

To run the AI in a live game environment:

1. Start the browser interaction with the poker platform:

   ```bash
   python src/ai_poker_player.py --platform [platform-name]
   ```

2. The AI will log in, monitor the game, and make decisions autonomously.

3. Chat interactions will be generated using GPT for human-like conversations.

---

## Future Enhancements

1. **Multi-Table Support**: Expand the AI's capabilities to handle multiple tables at once.
2. **Advanced Opponent Profiling**: Use machine learning techniques to profile and predict opponents' future actions.
3. **Ethical AI**: Implement fail-safes to ensure compliance with platform rules and prevent misuse of AI in online gaming environments.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

### **Contributors**

- **Your Name** - David Travers
- **OpenAI API** - GPT-4 for chat interactions
- **Selenium Community** - For browser automation assistance
