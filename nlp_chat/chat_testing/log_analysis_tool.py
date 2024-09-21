# log_analysis_tool.py

import os
import re
import json
from datetime import datetime
import matplotlib.pyplot as plt

# Directory containing chat logs
LOG_DIR = "./nlp_chat/chat_testing/logs/"

# Define patterns for chat-related analysis
BLUFF_PATTERN = r"\bbluff\b"
WIN_PATTERN = r"\bwin\b"
LOSS_PATTERN = r"\blost\b"
TIMESTAMP_PATTERN = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]"

def parse_chat_logs(log_file):
    """
    Parses a single log file to extract chat-related events and timestamps.

    Args:
        log_file (str): Path to the log file.

    Returns:
        list: A list of parsed log entries with timestamps and messages.
    """
    chat_data = []
    with open(log_file, "r") as file:
        for line in file:
            timestamp = re.findall(TIMESTAMP_PATTERN, line)
            if timestamp:
                timestamp = timestamp[0].strip("[]")
                message = re.sub(TIMESTAMP_PATTERN, "", line).strip()
                chat_data.append({
                    "timestamp": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                    "message": message
                })
    return chat_data

def analyze_chat_performance(chat_data):
    """
    Analyzes chat logs to evaluate bluff attempts, win/loss announcements, and timing.

    Args:
        chat_data (list): List of parsed chat data with timestamps and messages.

    Returns:
        dict: A dictionary with statistics on bluffing, win/loss rates, and chat frequency.
    """
    results = {
        "total_messages": 0,
        "bluffs_detected": 0,
        "wins_mentioned": 0,
        "losses_mentioned": 0,
        "chat_frequency": {}
    }
    
    for entry in chat_data:
        message = entry["message"].lower()
        timestamp = entry["timestamp"].strftime("%H:%M")
        results["total_messages"] += 1

        # Detect bluffing attempts
        if re.search(BLUFF_PATTERN, message):
            results["bluffs_detected"] += 1

        # Detect win/loss announcements
        if re.search(WIN_PATTERN, message):
            results["wins_mentioned"] += 1
        elif re.search(LOSS_PATTERN, message):
            results["losses_mentioned"] += 1

        # Track message frequency by time
        if timestamp not in results["chat_frequency"]:
            results["chat_frequency"][timestamp] = 1
        else:
            results["chat_frequency"][timestamp] += 1
    
    return results

def visualize_chat_data(stats):
    """
    Visualizes the analyzed chat data using matplotlib.

    Args:
        stats (dict): Dictionary containing chat performance statistics.
    """
    # Bar chart for bluffing, wins, and losses
    categories = ['Bluffs', 'Wins', 'Losses']
    counts = [stats["bluffs_detected"], stats["wins_mentioned"], stats["losses_mentioned"]]
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, counts, color=['blue', 'green', 'red'])
    plt.title('Bluffing, Wins, and Losses Detected in Chat')
    plt.ylabel('Count')
    plt.show()

    # Line chart for chat frequency over time
    times = sorted(stats["chat_frequency"].keys())
    frequencies = [stats["chat_frequency"][time] for time in times]
    
    plt.figure(figsize=(12, 6))
    plt.plot(times, frequencies, marker='o')
    plt.title('Chat Frequency Over Time')
    plt.xlabel('Time (HH:MM)')
    plt.ylabel('Message Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def analyze_logs_in_directory(log_dir):
    """
    Analyzes all log files in a given directory.

    Args:
        log_dir (str): Path to the directory containing chat logs.
    """
    all_stats = {
        "total_messages": 0,
        "bluffs_detected": 0,
        "wins_mentioned": 0,
        "losses_mentioned": 0,
        "chat_frequency": {}
    }

    for filename in os.listdir(log_dir):
        if filename.endswith(".log"):
            file_path = os.path.join(log_dir, filename)
            chat_data = parse_chat_logs(file_path)
            stats = analyze_chat_performance(chat_data)

            # Aggregate stats across logs
            all_stats["total_messages"] += stats["total_messages"]
            all_stats["bluffs_detected"] += stats["bluffs_detected"]
            all_stats["wins_mentioned"] += stats["wins_mentioned"]
            all_stats["losses_mentioned"] += stats["losses_mentioned"]
            
            # Merge chat frequency data
            for time, count in stats["chat_frequency"].items():
                if time not in all_stats["chat_frequency"]:
                    all_stats["chat_frequency"][time] = count
                else:
                    all_stats["chat_frequency"][time] += count

    # Visualize the aggregated data
    visualize_chat_data(all_stats)

if __name__ == "__main__":
    # Analyze all logs in the LOG_DIR directory
    analyze_logs_in_directory(LOG_DIR)
