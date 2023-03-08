import math

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return math.floor((i-1)/2)
    
    def leftChild(self, i):
        return 2*i + 1
    
    def rightChild(self, i):
        return 2*i + 2
    
    def maxHeapify(self, i, heapSize):
        largest = i
        left = self.leftChild(i)
        right = self.rightChild(i)
        
        if left < heapSize and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < heapSize and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest, heapSize)
            
    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
            
    #print nodes from top to down, left to right
    def Print(self):
        print(self.heap)
    
    #construct a max heap from array
    def maxHeap(self, array):
        self.heap = array.copy() # make a copy of the input list
        heapSize = len(self.heap)
        for i in range(math.floor(heapSize/2), -1, -1):
            self.maxHeapify(i, heapSize)

    
    def remove(self):
        if len(self.heap) < 1:
            return None
        
        max_value = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap = self.heap[:-1]
        self.maxHeapify(0, len(self.heap))
        
        return max_value
    
def sort_movies_batch(names, ratings):
    heap = MaxHeap()
    heap.maxHeap(ratings.copy()) # make a copy of the ratings list
    sorted_names = []
    for i in range(len(ratings)):
        max_rating = heap.remove()
        max_rating_index = ratings.index(max_rating)
        sorted_names.append(names[max_rating_index])
        ratings[max_rating_index] = -1 # to avoid duplicates in case of same ratings
    
    return sorted_names[::-1] #return in decreasing order


def sort_movies_incre(names, ratings):
    heap = MaxHeap()
    for i in range(len(ratings)):
        heap.insert(ratings[i])
    
    sorted_names = []
    while len(sorted_names) < len(names):
        # Retrieve the correct index of the movie based on its rating
        max_rating = heap.remove()
        max_rating_indices = [i for i, rating in enumerate(ratings) if rating == max_rating]
        for index in max_rating_indices:
            sorted_names.append(names[index])
            ratings[index] = -1 # to avoid duplicates in case of same ratings
        
    return sorted_names


# names = ['Dont Look Up', 'Spider-Man: No way Home', 'Attack on Titan', 'Nightmare Alley', 'Encanto', 'The Book of Boba Fett', 'All of Us Are Dead', 'Dune', 'Breaking Bad', 'Reacher', 'Ghostbusters: afterlife', 'Peacemaker', 'The Frog', 'Sing', 'The Mandalorian', 'The Matrix', 'Avengers: infinity war', 'Forrest Gump', 'Inception', 'After Life', 'Dexter: New Blood', 'Nobody', 'Avengers:Endgame', 'Fight Club', 'The Witcher', 'Euphoria', 'Joker', 'Free Guy', 'The Tinder Swindler', 'Ozark', 'Interstellar', 'The Shawshank Redemption', 'Hawkeye', 'The Dark Knight', 'Game of Thrones', 'No Time to Die', 'Squid Game', 'Scream', 'The Last Duel', 'Arcane', 'Archive 81' ]

# ratings = [7.2, 8.7, 9.0, 7.2, 7.3, 7.8, 7.7, 8.1, 9.4, 8.6, 7.3, 8.4, 8.5, 7.5, 8.8, 8.7, 8.4, 8.8, 8.8, 8.5, 8.3, 7.4, 8.4, 8.8, 8.2, 8.4, 8.4, 7.2, 7.4, 8.4, 8.6, 9.3, 7.7, 9.0, 9.2, 7.4, 8.0, 7.1, 7.4, 9.1, 7.5]

# movies = sort_movies_batch(names, ratings)
# print("\033[1;33m" +"Movies sorted in decreasing order of ratings:" + "\033[0m")
# for name in movies:
#     print(name)

# print()

# movies = sort_movies_incre(names, ratings)
# print("\033[1;33m" + "Movies sorted in increasing order of ratings:" + "\033[0m")
# for name in movies:
#     print(name)
