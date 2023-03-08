class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

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
            if self.heap[largest] == self.heap[i]:
                if l < n and self.heap[l] > self.heap[r]:
                    self.maxHeapify(l, n)
                elif r < n:
                    self.maxHeapify(r, n)
            else:
                self.maxHeapify(largest, n)

    def insert(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def Print(self):
        n = len(self.heap)
        for i in range(n):
            print(self.heap[i], end=" ")
        print()

    def maxHeap(self, arr):
        n = len(arr)
        self.heap = arr
        for i in range(n//2 - 1, -1, -1):
            self.maxHeapify(i, n)

    def remove(self):
        n = len(self.heap)
        if n == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.maxHeapify(0, n-1)
        return root


def sort_movies_batch(names, ratings):
    heap = MaxHeap()
    heap.maxHeap(ratings)
    sorted_names = []
    for i in range(len(ratings)-1, -1, -1):
        max_rating = heap.remove()
        max_index = ratings.index(max_rating)
        sorted_names.append(names[max_index])
        del ratings[max_index]
        del names[max_index]
    return sorted_names[::-1]


def sort_movies_incre(names, ratings):
    heap = MaxHeap()
    sorted_names = []
    for i in range(len(ratings)):
        heap.insert(ratings[i])
    for i in range(len(ratings)):
        max_rating = heap.remove()
        max_index = ratings.index(max_rating)
        sorted_names.append(names[max_index])
        del ratings[max_index]
        del names[max_index]
    return sorted_names
