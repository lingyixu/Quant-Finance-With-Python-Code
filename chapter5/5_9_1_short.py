def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_loc, min_val = i, arr[i]
        for j in range(i + 1, n):
            if arr[j] < min_val:
                min_loc, min_val = j, arr[j]
        arr[i], arr[min_loc] = arr[min_loc], arr[i]
    
    return arr

