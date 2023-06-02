def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
        
    return arr
