"""Find out if a string is a palindrome """

def palindrome(s1,s2):
    if s1[::-1] != s2:
        return False
    return True

def improvedpalindrome(s1):

    left = 0
    right = len(s1) -1

    while left < right:
        if s1[left] != s1[right]:
            return False
        
        left +=1 
        right -= 1

    return True




print(improvedpalindrome('racecar'))