def bubble_sort(arr):
    n = len(arr)
    
    has_swap = False
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                has_swap = True
        if not has_swap:
            break
            
    return arr
