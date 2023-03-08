import math
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
        smallest = i
        l = self.leftChild(i)
        r = self.rightChild(i)

        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l

        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.maxHeapify(smallest, n)

    def insert(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
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


# def sort_movies_batch(names, ratings):
#     n = len(ratings)
#     heap = MaxHeap()
#     heap.maxHeap(ratings)
#     sorted_names = []
#     for i in range(n-1, -1, -1):
#         max_score = heap.remove()
#         for j, rating in enumerate(ratings):
#             if rating == max_score:
#                 sorted_names.append(names[j])
#                 ratings.pop(j)
#                 names.pop(j)
#                 break
#     sorted_names.reverse()
#     return sorted_names

def sort_movies_batch(names, ratings):
    n = len(ratings)
    heap = MaxHeap()
    heap.maxHeap(ratings)
    sorted_names = []
    ratings_copy = ratings[:]  # make a copy of ratings
    for i in range(n-1, -1, -1):
        max_score = heap.remove()
        for j, rating in enumerate(ratings_copy):
            if rating == max_score:
                sorted_names.append(names[j])
                ratings_copy.pop(j)
                names.pop(j)
                break
    sorted_names.reverse()
    return sorted_names

def sort_movies_incre(names, ratings):
    heap = MaxHeap()
    sorted_names = []
    for i in range(len(ratings)):
        heap.insert(ratings[i]) # Insert the ratings in the heap
    for i in range(len(ratings)):
        max_rating = heap.remove() # Remove the maximum rating from the heap
        max_index = ratings.index(max_rating) # Get the index of the movie with maximum rating
        sorted_names.append(names[max_index]) # Append the name of the movie to the sorted list
        del ratings[max_index] # Remove the rating of the movie from the list
        del names[max_index] # Remove the name of the movie from the list
    return sorted_names




names = ['Dont Look Up', 'Spider-Man: No way Home', 'Attack on Titan', 'Nightmare Alley', 'Encanto', 'The Book of Boba Fett', 'All of Us Are Dead', 'Dune', 'Breaking Bad', 'Reacher', 'Ghostbusters: afterlife', 'Peacemaker', 'The Frog', 'Sing', 'The Mandalorian', 'The Matrix', 'Avengers: infinity war', 'Forrest Gump', 'Inception', 'After Life', 'Dexter: New Blood', 'Nobody', 'Avengers:Endgame', 'Fight Club', 'The Witcher', 'Euphoria', 'Joker', 'Free Guy', 'The Tinder Swindler', 'Ozark', 'Interstellar', 'The Shawshank Redemption', 'Hawkeye', 'The Dark Knight', 'Game of Thrones', 'No Time to Die', 'Squid Game', 'Scream', 'The Last Duel', 'Arcane', 'Archive 81' ]

ratings = [7.2, 8.7, 9.0, 7.2, 7.3, 7.8, 7.7, 8.1, 9.4, 8.6, 7.3, 8.4, 8.5, 7.5, 8.8, 8.7, 8.4, 8.8, 8.8, 8.5, 8.3, 7.4, 8.4, 8.8, 8.2, 8.4, 8.4, 7.2, 7.4, 8.4, 8.6, 9.3, 7.7, 9.0, 9.2, 7.4, 8.0, 7.1, 7.4, 9.1, 7.5]

movies = sort_movies_batch(names, ratings)
print("\033[1;33m" +"Movies sorted in decreasing order of ratings:" + "\033[0m")
for name in movies:
    print(name)

print()

movies = sort_movies_incre(names, ratings)
print("\033[1;33m" + "Movies sorted in increasing order of ratings:" + "\033[0m")
for name in movies:
    print(name)