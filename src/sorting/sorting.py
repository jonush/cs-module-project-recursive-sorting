# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    i = j = 0

    for _ in range(num_elements):
        if i < len(arrA) and j < len(arrB):
            if arrA[i] < arrB[j]:
                merged_arr.append(arrA[i])
                i += 1
            else:
                merged_arr.append(arrB[j])
                j += 1
        elif i == len(arrA):
            merged_arr.append(arrB[j])
            j += 1
        elif j == len(arrB):
            merged_arr.append(arrA[i])
            i += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass