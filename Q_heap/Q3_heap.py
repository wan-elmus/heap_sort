import math
import time
import random
import matplotlib.pyplot as plt

class MaxHeap:
 
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def maxHeapify(self, i):
        left = self.leftChild(i)
        right = self.rightChild(i)
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[i]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    #print nodes from top to down, left to right
    def Print(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" ")
        print()

    #construct a max heap from array
    def maxHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self.maxHeapify(i)

    def remove(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.maxHeapify(0)
        return root

def sort_movies_batch(names, ratings):
    heap = MaxHeap()
    heap.maxHeap([(rating, i) for i, rating in enumerate(ratings)])
    sorted_names = []
    while heap.heap:
        max_rating, index = heap.remove()
        if max_rating is not None and max_rating not in sorted_names:
            same_rating_movies = [(names[i], ratings[i]) for i in range(len(names)) if ratings[i] == max_rating]
            same_rating_movies = sorted(same_rating_movies, key=lambda x: x[1])
            sorted_names.extend([movie[0] for movie in same_rating_movies])
            sorted_names = list(set(sorted_names))
    return sorted_names[::-1]


def sort_movies_incre(names, ratings):
    heap = MaxHeap()
    sorted_names = []
    for rating, name in zip(ratings, names):
        heap.insert(rating)
    for i in range(len(ratings)):
        sorted_names.append(names[ratings.index(heap.remove())])
    return sorted_names[::-1]

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
    runtime = end_time - start_time
    heap_sort_runtimes.append(runtime)
    print(f"Heap sort runtime for dataset size {len(names)}: {runtime}")

# Sort data using Python's built-in sorting method and measure runtime
builtin_sort_runtimes = []
for names, ratings in datasets:
    start_time = time.time()
    sorted(zip(names, ratings), key=lambda x: x[1])
    end_time = time.time()
    runtime = end_time - start_time
    builtin_sort_runtimes.append(runtime)
    print(f"Built-in sort runtime for dataset size {len(names)}: {runtime}")


# Plot results
plt.plot(data_sizes, heap_sort_runtimes, label='Heap Sort')
plt.plot(data_sizes, builtin_sort_runtimes, label='Built-in Sort')
plt.xlabel('Data Size')
plt.ylabel('Runtime (seconds)')
plt.legend()
plt.show()
