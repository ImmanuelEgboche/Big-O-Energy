# implementation of mergesort
def merge(arr, s, m, e):
    # Copy the sorted left and rigth halfs to the temp arrays
    L = arr[s: m+1]
    R = arr[m+1:e]

    i = 0 # index fro L 
    j = 0 # index for R 
    k = s # index for arr

    """
    we have three pointers, k, j and i.
    k keeps track of where the next element in arr needs to be placed.
    i points to the element in the leftSubarray that is currently being compared to the 
    j element in the rightSubarray.
    One of i or j will increment depending on which element in smaller.
    k will increment regardless because arr will have an element placed inside of it 
    regardless of which one of i or j increments.
    """
    
    # Merge the two sorted halfs into the orginal array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j +=1
        k+=1
    
    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i +=1
        k +=1
    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1

def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

     #The middle index of the array
    m = (s+e) // 2
    
    # Sprt the left half
    mergeSort(arr, s,m)

    # Sort the right half
    mergeSort(arr, m+1, e)

    merge(arr, s, m, e)

    return arr


