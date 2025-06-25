# example array [2,2,1,0,0,2]

def bucketSort(arr):
    #Assuming arr only contains 0, 1, 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for i in arr:
        counts[i] += 1

    #Fill each bucket in the original array
    k = 0
    for i in range(len(counts)):
        for j in range((counts[i])):
            arr[i] = k
            i += 1
    return arr 


    