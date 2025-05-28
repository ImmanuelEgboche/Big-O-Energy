"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

"""
def hashmap(x):

    hashmap = {}

    for i in x:
        if i in hashmap:
            return False
        hashmap[i] = True
    return True

# Time complexity is O(n) for iterating through the string and look ups are O(1)

# Space complexity is O(s) s being the length of the string as in worst case we'd need to store all of the unique characters 
# so in terms of ASCII could be 128 charcters alphabet could be 26 Unicode could be 140,000
# so depends on string length 

def nested_for_loop(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                return False
    return True
# outer loop runs O(n) times whereas teh inner loop runs a step ahead well (n-1) + (n-2) + ... + 1 times = n(n-1)/2

"""
Let's say the length of the string is n. Here's how many iterations the inner loop performs for each value of i:

When i = 0: inner loop runs from j = 1 to j = n-1 → (n-1) iterations
When i = 1: inner loop runs from j = 2 to j = n-1 → (n-2) iterations
When i = 2: inner loop runs from j = 3 to j = n-1 → (n-3) iterations
...
When i = n-2: inner loop runs from j = n-1 to j = n-1 → 1 iteration
When i = n-1: inner loop doesn't run (range is empty) → 0 iterations


"""

def sorting_approach(x):
    if not x:
        return True
    sorted_x = sorted(x)
    for i in range(1, len(sorted_x)):
        if sorted_x[i] == sorted_x[i-1]:
            False
    return True

def bit_vector_approach(x):
        # If string length exceeds total possible ASCII chars, must have duplicates
    if len(x) > 128:
        return False
    
    # Create a bit vector (array of 16 bytes = 128 bits)
    checker = 0

    for char in x:
        val = ord(char)

        # Check if bit is already set
        if (checker & (1 << val)) > 0:
            return False
        
        checker |= (1 << val)
    return True

bit_vector_approach("hsgadgs")