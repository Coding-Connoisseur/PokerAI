# performance_test.py

import time
from nlp_chat.response_generator import generate_chat_response  # Assuming there's a function that generates chat responses
import random
import string

def random_prompt(length=10):
    """
    Generates a random string of a given length to simulate chat prompts.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def measure_latency(prompt):
    """
    Measures the time it takes to generate a chat response for a given prompt.
    
    Args:
        prompt (str): The chat prompt to test.
        
    Returns:
        float: The time taken to generate the response in seconds.
    """
    start_time = time.time()
    response = generate_chat_response(prompt)  # Simulated chat response
    end_time = time.time()
    
    return end_time - start_time

def throughput_test(num_prompts=100):
    """
    Simulates multiple chat prompts and measures how many responses the system can handle per second.
    
    Args:
        num_prompts (int): Number of chat prompts to simulate.
    
    Returns:
        float: Responses per second.
    """
    start_time = time.time()
    
    for _ in range(num_prompts):
        prompt = random_prompt()
        generate_chat_response(prompt)  # Simulate response generation
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return num_prompts / elapsed_time

def stress_test(max_prompts=1000, step=100):
    """
    Gradually increases the number of chat requests and measures the performance under load.
    
    Args:
        max_prompts (int): Maximum number of chat requests to simulate.
        step (int): Increment for each iteration of the stress test.
        
    Returns:
        dict: A dictionary with results of the stress test.
    """
    results = {}
    
    for i in range(step, max_prompts + 1, step):
        throughput = throughput_test(i)
        print(f"Processed {i} prompts at {throughput:.2f} responses per second.")
        results[i] = throughput
    
    return results

def main():
    """
    Runs performance tests for the NLP chat system.
    """
    print("Starting latency test...")
    prompt = random_prompt()
    latency = measure_latency(prompt)
    print(f"Latency for generating response: {latency:.4f} seconds")
    
    print("\nStarting throughput test with 100 prompts...")
    throughput = throughput_test(100)
    print(f"Throughput: {throughput:.2f} responses per second")
    
    print("\nStarting stress test...")
    stress_results = stress_test()
    print("Stress test complete. Results:")
    for prompts, throughput in stress_results.items():
        print(f"{prompts} prompts: {throughput:.2f} responses per second")
    
if __name__ == "__main__":
    main()
