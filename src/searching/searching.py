# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start <= end:
        middle = (start + end) // 2

        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            return binary_search(arr, target, start, middle - 1)
        elif target > arr[middle]:
            return binary_search(arr, target, middle + 1, end)

    return -1



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    switched = False

    if arr[high] <= arr[low]:
        switched = True
        arr.reverse()

    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            if switched:
                value = arr[mid]
                arr.reverse()
                return arr.index(value)
            else:
                return mid
        if target < arr[mid]:
            high = mid - 1
        if target > arr[mid]:
            low = mid + 1

    return -1