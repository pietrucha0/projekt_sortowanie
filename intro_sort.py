import math
import heapq
#zaczyna sortowac metoda quicksort ale przelacza na hepsort lub insertion sort 
#gdy zauwazy ze praca idzie za wolno lub danych jest tak malo ze mozna to zrobic szybciej

# sortowanie przez wstawianie dla malych tablic
def insertion_sort_internal(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# zamienia liste na kopiec i wyciaga najmniejszy element az ebdzie lista pusta
def heapsort_internal(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# jesliu przkroczy limit czyli (zwykle 2 * log2(n)) to przełączymy się na Heapsort
def intro_sort(arr):
    if not arr: return arr
    max_depth = 2 * math.floor(math.log2(len(arr)))
    return _introsort_recursive(arr, max_depth)

# jesli tablica ma mniej niz 16 elementow to uzywamy sortowania przez wstawianie
def _introsort_recursive(arr, depth_limit):
    n = len(arr)
    if n <= 16:
        return insertion_sort_internal(arr)
    if depth_limit == 0:
        return heapsort_internal(arr)
    
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot] # elementy mniejsze
    middle = [x for x in arr if x == pivot] # elementy rowne
    right = [x for x in arr if x > pivot] # elementy wieksze
    
    return (_introsort_recursive(left, depth_limit - 1) + 
            middle + 
            _introsort_recursive(right, depth_limit - 1))

