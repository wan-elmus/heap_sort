import math
import time
import random
import string
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
        if max_rating is not None and max_rating[0] not in sorted_names:
            sorted_names.append(names[max_rating[1]])
    return sorted_names[::-1]


def sort_movies_incre(names, ratings):
    heap = MaxHeap()
    sorted_names = []
    for rating, name in zip(ratings, names):
        heap.insert(rating)
    for i in range(len(ratings)):
        sorted_names.append(names[ratings.index(heap.remove())])
    return sorted_names[::-1]

# Generate the dataset
def generate_data(size):
    names = [''.join(random.choices(string.ascii_uppercase, k=10)) for _ in range(size)]
    ratings = [random.uniform(0, 10) for _ in range(size)]
    return names, ratings

names_1000, ratings_1000 = generate_data(1000)
names_10000, ratings_10000 = generate_data(10000)
names_100000, ratings_100000 = generate_data(100000)

# sort_movies_batch on 1,000 input size
start = time.time()
sort_movies_batch(names_1000, ratings_1000)
end = time.time()
print(f"Runtime for 1,000 input size: {end - start:.6f} seconds")

# sort_movies_batch on 10,000 input size
start = time.time()
sort_movies_batch(names_10000, ratings_10000)
end = time.time()
print(f"Runtime for 10,000 input size: {end - start:.6f} seconds")

# sort_movies_batch on 100,000 input size
start = time.time()
sort_movies_batch(names_100000, ratings_100000)
end = time.time()
print(f"Runtime for 100,000 input size: {end - start:.6f} seconds")

# sort_movies_incre on 1,000 input size
start = time.time()
sort_movies_incre(names_1000, ratings_1000)
end = time.time()
print(f"Runtime for sort_movies_incre on 1,000 input size: {end - start:.6f} seconds")

# built-in sorting methods on 1,000 input size
start = time.time()
sorted_names = [name for _, name in sorted(zip(ratings_1000, names_1000))]
end = time.time()
print(f"Runtime for sorted function on 1,000 input size: {end - start:.6f} seconds")

start = time.time()
ratings_1000.sort()
sorted_names = [name for _, name in sorted(zip(ratings_1000, names_1000))]
end = time.time()
print(f"Runtime for list.sort method on 1,000 input size: {end - start:.6f} seconds")