from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins
import timeit

# Example usage
amount = 113

# Using find_coins_greedy to find coins using the greedy algorithm and printing the result
print("Greedy Algorithm (find_coins_greedy) Result:", find_coins_greedy(amount))

# Using find_min_coins to find coins using dynamic programming for minimal coins and printing the result
print("Dynamic Programming (find_min_coins) Result:", find_min_coins(amount))

num_repeats = 10000

time_greedy = timeit.timeit(
    "find_coins_greedy(amount)", globals=globals(), number=num_repeats
)

time_dynamic = timeit.timeit(
    "find_min_coins(amount)", globals=globals(), number=num_repeats
)

# Result of analysis
print(
    f"Time taken by Greedy Algorithm (find_coins_greedy) for {num_repeats} repeats: {time_greedy:.6f} seconds"
)
print(
    f"Time taken by Dynamic Programming (find_min_coins) for {num_repeats} repeats: {time_dynamic:.6f} seconds"
)
