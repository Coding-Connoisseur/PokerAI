# test_simulation_throughput.py

import time
import pytest
from rl_module.train_agent import simulate_poker_game

def test_simulation_throughput():
    """
    This test measures how many poker simulations can be run in a fixed period,
    helping to assess system throughput during high-demand gameplay.
    """
    num_simulations = 100  # Define the number of poker games to simulate
    start_time = time.time()  # Start the timer
    
    for _ in range(num_simulations):
        simulate_poker_game()  # Simulate a poker game (mocked or real)
    
    end_time = time.time()  # End the timer
    duration = end_time - start_time  # Total time taken
    
    print(f"Ran {num_simulations} simulations in {duration:.2f} seconds.")
    
    # Ensure throughput meets performance criteria (e.g., at least 10 games/second)
    assert duration <= (num_simulations / 10), "Throughput too low!"

if __name__ == "__main__":
    pytest.main([__file__])
