def tim_sort(arr):
    min_run = 32
    n = len(arr)

    # 1. Sortowanie małych fragmentów (Runów)
    for i in range(0, n, min_run):
        end = min(i + min_run - 1, n - 1)
        for j in range(i + 1, end + 1):
            key = arr[j]
            k = j - 1
            while k >= i and key < arr[k]:
                arr[k + 1] = arr[k]
                k -= 1
            arr[k + 1] = key

    # 2. Scalanie (Merge)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)
            
            if mid < right:
                len1, len2 = mid - left + 1, right - mid
                left_part = arr[left:mid + 1]
                right_part = arr[mid + 1:right + 1]
                
                i, j, k = 0, 0, left
                while i < len1 and j < len2:
                    if left_part[i] <= right_part[j]:
                        arr[k] = left_part[i]
                        i += 1
                    else:
                        arr[k] = right_part[j]
                        j += 1
                    k += 1
                
                while i < len1:
                    arr[k] = left_part[i]
                    k += 1
                    i += 1
                while j < len2:
                    arr[k] = right_part[j]
                    k += 1
                    j += 1
        size *= 2
    return arr