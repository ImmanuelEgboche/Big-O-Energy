"""
Given two strings, write a method to decide if one is a permutation of the 
other.
"""

def is_permutation(s1, s2):

    if len(s1) != len(s2):
        return False
    
    
    freq = {}
    for c in s1:
        freq[c] = freq.get(c,0) + 1

    for c in s2: 
        if c not in freq or freq[c] == 0:
            return False
        freq[c] -=1

    
    return True 

print(is_permutation('abc','bca'))
