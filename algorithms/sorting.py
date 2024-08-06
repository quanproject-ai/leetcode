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
    2. Use a pointer traverse along the array, compare the current value and the next value then swap them if
    next value is larger than current value.
    3. For each entire array passes, the last position will be the largest value, and the loop updates with the last
    position with one position - number of passes less
    """
    max_index = len(arr)
    for n in range(max_index): #tracking the total time the sorting passes
        for pointer in range(0,max_index-n-1): #update the last position. compare from begining to the latest unsorted position
            if arr[pointer] > arr[pointer+1]:
                arr[pointer], arr[pointer+1] = arr[pointer+1], arr[pointer]
    print('Total passes:',n)
    return arr



# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10,64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)