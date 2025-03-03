def pivot_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    # Partition the array into two subarrays:
    # - left: elements less than the pivot
    # - right: elements greater than or equal to the pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    # Recursively sort the subarrays and concatenate them with the 
    return pivot_sort(left) + [pivot] + pivot_sort(right)