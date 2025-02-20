import time
import matplotlib.pyplot as plt
from tabulate import tabulate

def fibonacci_fast_doubling(n):
    if n == 0:
        return 0

    def fib_helper(n):
        if n == 0:
            return (0, 1)
        a, b = fib_helper(n // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fib_helper(n)[0]

# Function to measure execution time
def measure_time(func, n):
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
    result_fast_doubling, time_fast_doubling = measure_time(fibonacci_fast_doubling, n)
    results.append([n, time_fast_doubling])

# Output results in table format
headers = ["n-th Term", "Fast Doubling Time (s)"]
print(tabulate(results, headers=headers, tablefmt="grid"))

# Plot the graph
n_values = [row[0] for row in results]
fast_doubling_times = [row[1] for row in results]

plt.plot(n_values, fast_doubling_times, label="Fast Doubling Method")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time (seconds)")
plt.title("Performance of Fibonacci Fast Doubling")
plt.legend()
plt.grid()
plt.show()
