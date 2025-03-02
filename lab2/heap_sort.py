import time
import random
import matplotlib.pyplot as plt
from tabulate import tabulate

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

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
    time_taken = measure_time(heap_sort, arr)
    results.append([size, f"{time_taken:.6f} seconds"])

print(tabulate(results, headers=["Input Size", "Time Taken"], tablefmt="grid"))

sizes = [row[0] for row in results]
times = [float(row[1].split()[0]) for row in results]
plt.plot(sizes, times, marker='o', label="HeapSort")
plt.xlabel("Input Size")
plt.ylabel("Time Taken (seconds)")
plt.title("HeapSort Performance")
plt.legend()
plt.grid(True)
plt.show()
