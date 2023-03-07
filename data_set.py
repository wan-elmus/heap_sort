import time
import random
import matplotlib.pyplot as plt

# Generate data
data_sizes = [1000, 10000, 100000]
datasets = []
for size in data_sizes:
    names = [f"Movie {i}" for i in range(size)]
    ratings = [random.uniform(0, 10) for _ in range(size)]
    datasets.append((names, ratings))

# Sort data using heap sort and measure runtime
heap_sort_runtimes = []
for names, ratings in datasets:
    start_time = time.time()
    sort_movies_batch(names, ratings)
    end_time = time.time()
    heap_sort_runtimes.append(end_time - start_time)

# Sort data using Python's built-in sorting method and measure runtime
builtin_sort_runtimes = []
for names, ratings in datasets:
    start_time = time.time()
    sorted(zip(names, ratings), key=lambda x: x[1])
    end_time = time.time()
    builtin_sort_runtimes.append(end_time - start_time)

# Plot results
plt.plot(data_sizes, heap_sort_runtimes, label='Heap Sort')
plt.plot(data_sizes, builtin_sort_runtimes, label='Built-in Sort')
plt.xlabel('Data Size')
plt.ylabel('Runtime (seconds)')
plt.legend()
plt.show()
