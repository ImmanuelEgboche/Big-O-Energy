"""Implement Insertion Sort and return intermediate states.

Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right. It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

Objective:

Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list."""



def insertionSort(arr):
    if len(arr) <=1:
        return [arr[:]]
    
    # making a copy to not modify the original
    result_arr = arr[:]
    states = []

    # Add inital state
    states.append(result_arr[:])

    #Traverse through 1 to len(arr)
    for i in range(1, len(result_arr)):
        # Current element to be inserted 
        current = result_arr[i]
        j = i - 1


        while j >= 0 and result_arr[j+1] < result_arr[j]:
            result_arr[j+1] = result_arr[j]
            j-=1

        result_arr[j + 1] = current

        states.append(result_arr[:])
    
    return states

