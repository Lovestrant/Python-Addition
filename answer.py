#########QUESTION 1

def Exercise1(num):
    # Initialize L and R arrays
    L = [1] * len(num)
    R = [1] * len(num)

    # Fill in L array
    for i in range(1, len(num)):
        L[i] = L[i - 1] * num[i - 1]

    # Fill in R array in reverse
    for i in reversed(range(len(num) - 1)):
        R[i] = R[i + 1] * num[i + 1]

    # Calculate answer
    ans = [L[i] * R[i] for i in range(len(num))]
    return ans

#TEST CODE
print(Exercise1([1, 2, 3, 4]))  # Should print [24, 12, 8, 6]


######### QUESTION 2
def Exercise2(matrix):
    # Initialize boundaries and result list
    up, right, down, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
    result = []
    
    # Loop until matrix is completely traversed
    while up <= down and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[up][i])
        up += 1
        
        # Traverse from up to down
        for i in range(up, down + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse from right to left if needed
        if up <= down:
            for i in reversed(range(left, right + 1)):
                result.append(matrix[down][i])
            down -= 1
        
        # Traverse from down to up if needed
        if left <= right:
            for i in reversed(range(up, down + 1)):
                result.append(matrix[i][left])
            left += 1
    
    return result

#TEST CODE
print(Exercise2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Should print [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(Exercise2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # Should print [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


######### QUESTION 3
def Exercise3(nums1, nums2, nums3, nums4):
    # Populate nums4 into a dictionary
    nums4_dict = {}
    for num in nums4:
        if num in nums4_dict:
            nums4_dict[num] += 1
        else:
            nums4_dict[num] = 1
    
    # Initialize counter
    counter = 0
    
    # Loop through nums1, nums2, and nums3
    for num1 in nums1:
        for num2 in nums2:
            for num3 in nums3:
                # Check if the complement of num1 + num2 + num3 exists in nums4_dict
                if -(num1 + num2 + num3) in nums4_dict:
                    counter += nums4_dict[-(num1 + num2 + num3)]
    
    return counter

#TEST CODE
print(Exercise3([1, 2], [-2, -1], [-1, 2], [0, 2]))  # Should print 2
print(Exercise3([0], [0], [0], [0]))  # Should print 1

########## QUESTION 4
def Exercise4(height):
    # Initialize pointers and max_area
    left, right = 0, len(height) - 1
    max_area = 0
    
    # Loop until pointers meet
    while left < right:
        # Calculate area
        area = min(height[left], height[right]) * (right - left)
        
        # Update max_area if necessary
        max_area = max(max_area, area)
        
        # Move pointers
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

#TEST CODE
print(Exercise4([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Should print 49

########## QUESTION 5
def Exercise5(nums):
    # Return 0 if nums is empty
    if not nums:
        return 0
    
    # Sort nums
    nums.sort()
    
    # Initialize variables
    longest, current = 1, 1
    
    # Loop through nums
    for i in range(1, len(nums)):
        # Check if current number extends the sequence
        if nums[i] == nums[i - 1] + 1:
            current += 1
        # If not, check if current sequence is the longest so far
        elif nums[i] != nums[i - 1]:
            longest = max(longest, current)
            current = 1
    
    # Return the maximum of the current sequence and the longest one
    return max(longest, current)

#TEST CODE
print(Exercise5([100, 4, 200, 1, 3, 2]))  # Should print 4
print(Exercise5([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Should print 9

########## QUESTION 6
def Exercise6(nums):
    # Sort nums
    nums.sort()
    
    # Loop through nums
    for i in range(1, len(nums)):
        # If current number is equal to the previous, return it
        if nums[i] == nums[i - 1]:
            return nums[i]

#TEST CODE
print(Exercise6([1, 3, 4, 2, 2]))  # Should print 2
print(Exercise6([3, 1, 3, 4, 2]))  # Should print 3

########## QUESTION 7
def Exercise7(s, k):
    # Initialize variables
    left, right, max_length = 0, 0, 0
    window = {}
    
    # Loop until right pointer reaches the end of s
    while right < len(s):
        # Add character at right pointer to the window
        window[s[right]] = window.get(s[right], 0) + 1
        
        # If the window contains more than k distinct characters
        if len(window) > k:
            # Remove character at left pointer from the window
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            
            # Move left pointer to the right
            left += 1
        
        # Update max_length if necessary
        max_length = max(max_length, right - left + 1)
        
        # Move right pointer to the right
        right += 1
    
    return max_length

#TEST CODE
print(Exercise7("eceba", 2))  # Should print 3
print(Exercise7("aa", 1))  # Should print 2


########## QUESTION 8
def Exercise8(nums, k):
    # Initialize variables
    max_nums = []
    window = nums[:k]
    
    # Loop through nums
    for i in range(len(nums) - k + 1):
        # Append maximum of the window to max_nums
        max_nums.append(max(window))
        
        # If the end of nums has not been reached, update window
        if i + k < len(nums):
            window.pop(0)
            window.append(nums[i + k])
    
    return max_nums

#TEST CODE
print(Exercise8([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Should print [3, 3, 5, 5, 6, 7]
print(Exercise8([1], 1))  # Should print [1]


########## QUESTION 9
def Exercise9(s, t):
    # Initialize variables
    window = ""
    min_window = s
    t_chars = {}
    
    # Create dictionary of characters in t and their frequencies
    for char in t:
        if char in t_chars:
            t_chars[char] += 1
        else:
            t_chars[char] = 1
    
    # Loop through s
    for i in range(len(s)):
        # Add character to window
        window += s[i]
        
        # Decrement frequency of character in t_chars
        if s[i] in t_chars:
            t_chars[s[i]] -= 1
        
        # If all characters in t_chars have a frequency of 0, check if window is minimum
        if all(value == 0 for value in t_chars.values()):
            if len(window) < len(min_window):
                min_window = window
    
    # Check if a valid window was found
    if all(value <= 0 for value in t_chars.values()):
        return min_window
    else:
        return ""

#TEST CODE
print(Exercise9("ADOBECODEBANC", "ABC"))  # Should print "BANC"
print(Exercise9("a", "a"))  # Should print "a"
print(Exercise9("a", "aa"))  # Should print ""


########## QUESTION 10
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

