def quickSort(arr: list[int], s:int, e:int) -> list[int]:
    if e -s + 1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s #pointer for the left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left+=1
    
    # Move pivot in-between left and right sides
    arr[e] = arr[left]
    arr[left] = pivot

    #Quick sort left side
    quickSort(arr, s, left -1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr

