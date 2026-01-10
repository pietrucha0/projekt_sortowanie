import math
import heapq

def insertion_sort_internal(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def heapsort_internal(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def intro_sort(arr):
    if not arr: return arr
    max_depth = 2 * math.floor(math.log2(len(arr)))
    return _introsort_recursive(arr, max_depth)

def _introsort_recursive(arr, depth_limit):
    n = len(arr)
    if n <= 16:
        return insertion_sort_internal(arr)
    if depth_limit == 0:
        return heapsort_internal(arr)
    
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return (_introsort_recursive(left, depth_limit - 1) + 
            middle + 
            _introsort_recursive(right, depth_limit - 1))