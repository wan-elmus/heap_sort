
## For Q1

This program defines a MaxHeap class and provides methods to perform operations on a heap data structure. The MaxHeap class has the following methods:

~ __init__(self): Initializes an empty heap.

~ parent(self, i): Returns the index of the parent node of the node at index i.

~ leftChild(self, i): Returns the index of the left child of the node at index i.

~ rightChild(self, i): Returns the index of the right child of the node at index i.

~ maxHeapify(self, i, heapSize): Maintains the max-heap property of the heap rooted at the node with index i by recursively swapping nodes if necessary. The heapSize parameter is the size of the heap.

~ insert(self, value): Inserts a value into the heap while maintaining the max-heap property.

~ Print(self): Prints the heap in level order.

~ maxHeap(self, array): Constructs a max heap from an array.

~ remove(self): Removes the maximum value from the heap and maintains the max-heap property.

There are also two functions to sort movies based on their ratings:

The *sort_movies_batch(names, ratings)* : Sorts movies based on their ratings using batch processing. First, the ratings are added to the heap using the maxHeap method of the MaxHeap class. Then, the maximum rating is removed from the heap and the corresponding movie name is appended to a list. The process is repeated until all movies are sorted. The function returns the sorted movie names in decreasing order of ratings.

The *sort_movies_incre* function takes two lists, names and ratings, but instead of initializing a MaxHeap object with the entire ratings list, it inserts each rating into the heap one by one. It then repeatedly removes the maximum rating from the heap, finds the corresponding movie name in the names list, and appends it to a sorted_names list. It returns the sorted_names list in increasing order of ratings.

## For Q2


