import math

class MaxHeap:
 
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1)//2

    def leftChild(self, i):
        return (2 * i) + 1

    def rightChild(self, i):
        return (2 * i) + 2
 
    def maxHeapify(self, i, n):
        largest = i
        l = self.leftChild(i)
        r = self.rightChild(i)
        
        if l < n and self.heap[l] > self.heap[largest]:
            largest = l
 
        if r < n and self.heap[r] > self.heap[largest]:
            largest = r
 
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest, n)
 
    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while (i != 0 and self.heap[self.parent(i)] < self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
 
    #print nodes from top to down, left to right
    def Print(self):
        n = len(self.heap)
        for i in range(n):
            print(self.heap[i], end = " ")
        print()
    
    #construct a max heap from array
    def maxHeap(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.maxHeapify(i, n)
    
    def remove(self):
        n = len(self.heap)
        if n == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[n-1]
        self.heap.pop()
        self.maxHeapify(0, len(self.heap))
        return root

def sort_movies_batch(names, ratings):
    n = len(ratings)
    heap = MaxHeap()
    heap.maxHeap(ratings)
    sorted_names = []
    for i in range(n-1, -1, -1):
        max_score = heap.remove()
        idx = ratings.index(max_score)
        sorted_names.append(names[idx])
        ratings.pop(idx)
        names.pop(idx)
    sorted_names.reverse()
    return sorted_names

def sort_movies_incre(names, ratings):
    n = len(ratings)
    heap = MaxHeap()
    sorted_names = []
    for i in range(n):
        heap.insert(ratings[i])
    for i in range(n):
        max_score = heap.remove()
        idx = ratings.index(max_score)
        sorted_names.append(names[idx])
        ratings.pop(idx)
        names.pop(idx)
    return sorted_names
