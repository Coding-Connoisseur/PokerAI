# fine_tuning_script.py

import os
import torch
from datasets import load_dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments

# Check if GPU is available
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

# Function to load the dataset for fine-tuning
def load_poker_dataset(data_path):
    """
    Load the poker-related dataset for fine-tuning the model.
    The dataset should contain examples of poker chat (e.g., bluffing, banter).
    Args:
        data_path (str): Path to the dataset file.
    Returns:
        dataset: A tokenized dataset ready for fine-tuning.
    """
    dataset = load_dataset('text', data_files={'train': data_path})
    return dataset

# Tokenizer and Model setup
def setup_model_and_tokenizer():
    """
    Initialize the GPT-2 model and tokenizer.
    Returns:
        model: GPT-2 model for fine-tuning.
        tokenizer: GPT-2 tokenizer.
    """
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2').to(device)
    return model, tokenizer

# Tokenize the dataset
def tokenize_function(examples, tokenizer):
    """
    Tokenize the dataset using GPT-2 tokenizer.
    Args:
        examples: A batch of text examples from the dataset.
        tokenizer: The GPT-2 tokenizer.
    Returns:
        dict: Tokenized inputs and attention masks.
    """
    return tokenizer(examples['text'], padding='max_length', truncation=True, max_length=128)

# Fine-tune the model
def fine_tune_model(model, tokenizer, dataset):
    """
    Fine-tune the GPT-2 model on the poker-specific dataset.
    Args:
        model: The GPT-2 model.
        tokenizer: The GPT-2 tokenizer.
        dataset: The poker-related dataset.
    """
    # Tokenize the dataset
    tokenized_dataset = dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./nlp_chat/models/",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=500,
        save_total_limit=2,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="steps",
        eval_steps=500,
    )

    # Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
        tokenizer=tokenizer,
    )

    # Train the model
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained("./nlp_chat/models/fine_tuned_poker_gpt2")
    tokenizer.save_pretrained("./nlp_chat/models/fine_tuned_poker_gpt2")

# Main function to run the fine-tuning script
def main():
    # Load dataset
    data_path = "./nlp_chat/data/poker_chat.txt"  # Path to your poker-related text data
    dataset = load_poker_dataset(data_path)

    # Set up model and tokenizer
    model, tokenizer = setup_model_and_tokenizer()

    # Fine-tune the model
    fine_tune_model(model, tokenizer, dataset)

if __name__ == "__main__":
    main()
