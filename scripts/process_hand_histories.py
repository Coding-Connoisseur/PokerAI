import os
import pandas as pd
import json

# Path to the directory containing hand history files
HAND_HISTORY_DIR = "./data/hand_history/"
PROCESSED_DATA_DIR = "./data/processed/"

def load_hand_history(file_path):
    """
    Loads a single hand history file (in JSON or CSV format) and returns it as a DataFrame.
    
    Args:
        file_path (str): Path to the hand history file.
        
    Returns:
        pd.DataFrame: DataFrame containing the parsed hand history data.
    """
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return pd.json_normalize(data)
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Only .json and .csv are supported.")

def process_hand_history(df):
    """
    Cleans and processes the hand history DataFrame to ensure it is ready for training or analysis.
    
    Args:
        df (pd.DataFrame): DataFrame containing raw hand history data.
        
    Returns:
        pd.DataFrame: Cleaned and processed DataFrame.
    """
    # Drop unnecessary columns
    columns_to_keep = ['hand_id', 'player_id', 'action', 'amount', 'result', 'timestamp', 'card_1', 'card_2']
    df = df[columns_to_keep]

    # Convert timestamps to datetime objects
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Handle missing values
    df = df.dropna()

    # Convert card values to numeric (e.g., 'Ace' -> 14, 'King' -> 13)
    card_mapping = {
        'Ace': 14, 'King': 13, 'Queen': 12, 'Jack': 11,
        '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
    }
    df['card_1'] = df['card_1'].map(card_mapping)
    df['card_2'] = df['card_2'].map(card_mapping)

    return df

def save_processed_data(df, output_file):
    """
    Saves the processed DataFrame to the processed data directory as a CSV file.
    
    Args:
        df (pd.DataFrame): Cleaned and processed hand history data.
        output_file (str): Path to the output CSV file.
    """
    if not os.path.exists(PROCESSED_DATA_DIR):
        os.makedirs(PROCESSED_DATA_DIR)
    
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

def process_all_hand_histories():
    """
    Processes all hand history files in the hand history directory and saves the cleaned data.
    """
    for filename in os.listdir(HAND_HISTORY_DIR):
        file_path = os.path.join(HAND_HISTORY_DIR, filename)
        if filename.endswith('.json') or filename.endswith('.csv'):
            print(f"Processing {filename}...")
            df = load_hand_history(file_path)
            processed_df = process_hand_history(df)
            output_file = os.path.join(PROCESSED_DATA_DIR, f"processed_{filename}.csv")
            save_processed_data(processed_df, output_file)
        else:
            print(f"Skipping unsupported file: {filename}")

if __name__ == "__main__":
    process_all_hand_histories()
