import time
import random
import matplotlib.pyplot as plt
from tabulate import tabulate

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

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
    time_taken = measure_time(merge_sort, arr)
    results.append([size, f"{time_taken:.6f} seconds"])

print(tabulate(results, headers=["Input Size", "Time Taken"], tablefmt="grid"))

sizes = [row[0] for row in results]
times = [float(row[1].split()[0]) for row in results]
plt.plot(sizes, times, marker='o', label="MergeSort")
plt.xlabel("Input Size")
plt.ylabel("Time Taken (seconds)")
plt.title("MergeSort Performance")
plt.legend()
plt.grid(True)
plt.show()
