"""
Given two strings, write a method to decide if one is a permutation of the 
other.
"""

def is_permutation(s1, s2):

    # if the strings are not teh same length, immediate not a permutation
    if len(s1) != len(s2):
        return False
    
    """
    freq is a hash map that stores character counts
    .get(c,0) is a safe way to get access to values without getting key errors
    if key exists you get freq[c] , if it doesnt exist you get a default value of 0 and then adds 1 for the occurance
    then the freq[c] stores the new count for that key
    """
    freq = {}
    for c in s1:
        freq[c] = freq.get(c,0) + 1

    """
    A seperate for loop for the second string that checks the key is in the hashmap and the value is not 0
    then decremnts the occurence is 
    """
    for c in s2: 
        if c not in freq or freq[c] == 0:
            return False
        freq[c] -=1

    
    return True 

print(is_permutation('abc','bca'))
