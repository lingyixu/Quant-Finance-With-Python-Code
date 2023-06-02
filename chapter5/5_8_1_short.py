def binary_search(a, x):
    first = 0
    last = len(a) - 1
    while first <= last:
        mid = (first + last) // 2
        if a[mid] < x:
            first = mid + 1
        elif a[mid] > x:
            last = mid - 1
        else:
            return mid
    return -1
