import random


def quick_sort(arr) -> list:
    """
    check out Leetcode problem 912 
    divide and conquere method
    1. pick a point within an array that any value is lesser than that value is kept to the left then vice versa.
    2. left and right arrays would do #1 until the array contains 1 single element
    """
    # Base case: an empty or single-element list is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here we choose any random value) 
    pivot = random.choice(arr)
    
    # Partition the array into three parts: less, equal, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively apply quicksort to the left and right parts, then combine
    return quick_sort(left) + middle + quick_sort(right)



def merge_sort(arr):
    """
    divide and conquer
    1. divide the array in half
    2.  recursively doing the dividing
    3. merge together by comparing the values of each "halves" and keep order
    """
    #this step is prevent recursion error and if array has less than or equal to 2 values, return array
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half =  arr[mid:]
    
    #recursively
    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)
    return  _heplper_merge_sort(sorted_left_half,sorted_right_half)

def _heplper_merge_sort(left,right):
    """Function merge two halves of merge_sort alogrithms together using iterations among two arrays

    Args:
        left (array): _description_
        right (array): _description_

    Returns:
        array: sorted arrays
    """
    merged = []
    i = j = 0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    #  Append any remaining elements in the left half
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Append any remaining elements in the right half
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def bubble_sort(arr):
    """
    1.Traverse the entire arrays
    2. Use two pointers where 1 slow pointer goes from begining to the end and 1 fast pointer going from beginnig to 
    max(array) - slow pointer's index - 1
    comparing the value with slow pointer's value
    3. Swap the position for smaller pointer to larger pointer
    4. recursive
    """
    max_index = len(arr)

    for slow_pointer in range(max_index):
        for fast_pointer in range(0,max_index-slow_pointer-1):
            if arr[fast_pointer] > arr[fast_pointer+1]:
                arr[fast_pointer], arr[fast_pointer+1] = arr[fast_pointer+1], arr[fast_pointer]
    return arr



# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10,64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)