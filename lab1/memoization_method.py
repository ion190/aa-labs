import time
import matplotlib.pyplot as plt
from tabulate import tabulate

# Memoization dictionary
memo = {}

def fibonacci_memoization(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]

# Function to measure execution time
def measure_time(func, n):
    global memo
    memo = {}  # Clear the memo for each run to ensure accurate timing
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Input series of Fibonacci terms to be looked up
limited_scope = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
bigger_scope = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Combine the two series into one
all_terms = limited_scope + bigger_scope

# Store results
results = []

# Measure time for each term
for n in all_terms:
    result_memo, time_memo = measure_time(fibonacci_memoization, n)
    results.append([n, time_memo])

# Output results in table format
headers = ["n-th Term", "Memoization Time (s)"]
print(tabulate(results, headers=headers, tablefmt="grid"))

# Plot the graph
n_values = [row[0] for row in results]
memoization_times = [row[1] for row in results]

plt.plot(n_values, memoization_times, label="Memoization Method")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time (seconds)")
plt.title("Performance of Fibonacci Memoization")
plt.legend()
plt.grid()
plt.show()
