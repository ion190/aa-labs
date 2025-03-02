import time
import random
import matplotlib.pyplot as plt
from tabulate import tabulate

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    return time.time() - start_time

def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]



sizes = [100, 500, 1000, 5000, 10000]
results = []

for size in sizes:
    arr = generate_random_array(size)
    time_taken = measure_time(quicksort, arr)
    results.append([size, f"{time_taken:.6f} seconds"])

print(tabulate(results, headers=["Input Size", "Time Taken"], tablefmt="grid"))

sizes = [row[0] for row in results]
times = [float(row[1].split()[0]) for row in results]
plt.plot(sizes, times, marker='o', label="QuickSort")
plt.xlabel("Input Size")
plt.ylabel("Time Taken (seconds)")
plt.title("QuickSort Performance")
plt.legend()
plt.grid(True)
plt.show()

