class LRUCacheBruteForce:
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        print(f"GET {key}: Searching through {self.cache}")

        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                print(f" Found at index {i}, moved to end: {self.cache}")
                return tmp[1]
        print(f" Key {key} not found")
        return -1
    
    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[i] = value
                self.cache.append(tmp)
                print(f"Updated exisisting key moved to end: {self.cache}")
                return
            
        if len(self.cache) == self.capacity:
            removed = self.cache.pop(0)
            print(f"Cache full, removed LRU item {removed}")
        
        self.cache.append([key, value])
        print(f"Added new item: {self.cache}")

print("=== DEMONSTRATING BRUTE FORCE APPROACH ===")
cache = LRUCacheBruteForce(3)
cache.put(1, 10)
cache.put(2, 20)  
cache.put(3, 30)
print(f"GET 2: {cache.get(2)}")  # Should move 2 to end
cache.put(4, 40)  # Should evict 1 (least recently used)
print(f"GET 1: {cache.get(1)}")  # Should return -1


print("\n" + "="*60)
print("WHY THE BRUTE FORCE IS O(n):")
print("="*60)
print("❌ get(): Must search through entire list to find key")
print("❌ put(): Must search through entire list to check if key exists")  
print("❌ pop(0): Removing from front requires shifting all elements")
print("❌ pop(i): Removing from middle requires shifting elements")


print("\n" + "="*60)
print("THE OPTIMAL O(1) SOLUTION NEEDS:")
print("="*60)
print("✓ Hash Map: O(1) lookup to find if key exists")
print("✓ Doubly Linked List: O(1) insertion/deletion anywhere")
print("✓ Combined: Hash map points to nodes in linked list")

class Node:
    """
    Doubly linked list Node
    Each node store key, value and pointers to prev/ next nodes
    """
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheOptimal:
    """
    Optimal O(1) combine hash map and doubly linked list

    Hash map for O(1) look up 

    Doubly linked list for O(1) insertion and deletion
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}

        