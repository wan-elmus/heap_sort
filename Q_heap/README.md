
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

The MaxHeap class has an instance variable heap that is initially an empty list. The methods parent, leftChild, and rightChild are used to calculate the indices of a node's parent, left child, and right child nodes, respectively.

The maxHeapify method is used to maintain the MaxHeap property after a value has been removed from the heap. It takes an index i and the size of the heap n as arguments, and recursively swaps nodes in the heap until the MaxHeap property is restored.

The insert method is used to insert a value into the heap. It adds the value to the end of the heap and then swaps it with its parent node until the MaxHeap property is restored.

The Print method is used to print the contents of the heap.

The maxHeap method is used to build a MaxHeap from a given list of values. It starts from the middle of the list and recursively calls maxHeapify to ensure that each subtree is a MaxHeap.

The remove method is used to remove the maximum value from the heap. It swaps the maximum value with the last value in the heap, removes the last value, and then calls maxHeapify to restore the MaxHeap property.

The sort_movies_batch function takes two lists as arguments: names and ratings. It sorts the list of names based on the list of ratings using a MaxHeap. It starts by building a MaxHeap from the list of ratings, then iteratively removes the maximum value from the heap and adds the corresponding name to a new list. Finally, it returns the sorted list of names in ascending order.

The sort_movies_incre function is similar to sort_movies_batch, but it inserts the values into the heap one at a time rather than building the heap from a list. It starts by inserting all the ratings into the heap, then iteratively removes the maximum value from the heap and adds the corresponding name to a new list. Finally, it returns the sorted list of names in ascending order.


## For Q3



