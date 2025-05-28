"""Given two strings, write a method to decide if one is a permutation of the
other."""

def CheckPerm(s1,s2):
    x =sorted(s1)
    y =sorted(s2)

    return x == y 
    
