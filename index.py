class Cache:
    def __init__(self, capacity):
        # Initialize the cache with the given capacity
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key):
        # Return the value for the given key if it exists, otherwise return -1
        if key in self.cache:
            # Update the key's position in the LRU list
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        # If the key already exists, update its value and position in the LRU list
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
        else:
            # If the key does not exist, add it to the cache and the LRU list
            self.cache[key] = value
            self.lru.append(key)
            # If the number of keys exceeds the capacity, remove the least recently used key
            if len(self.cache) > self.capacity:
                del self.cache[self.lru.pop(0)]

#USAGE OF THE CACHE CLASS
# Create a new cache with capacity 2
cache = Cache(2)

# Put the key-value pair (1, 1) in the cache
cache.put(1, 1)

# The cache now contains {1: 1}
print(cache.cache)

# Put the key-value pair (2, 2) in the cache
cache.put(2, 2)

# The cache now contains {1: 1, 2: 2}
print(cache.cache)

# Get the value for key 1
print(cache.get(1)) # Output: 1

# Put the key-value pair (3, 3) in the cache
cache.put(3, 3)

# The cache now contains {2: 2, 3: 3}
print(cache.cache)

# Get the value for key 1
print(cache.get(1)) # Output: -1

# Put the key-value pair (4, 4) in the cache
cache.put(4, 4)

# The cache now contains {3: 3, 4: 4}
print(cache.cache)

# Get the value for key 2
print(cache.get(2)) # Output: -1
