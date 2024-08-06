def binary_search_insert_position(arr,target):
    """ Apply on sorted array
    1. Using indexes,Two pointers at the begining and -1 position from the end of the array are compared for value
    2. Algorithm find the mid indexes based on the left and right pointers
    3. Use the mid index to find mid value and compare with the target
    4. If mid value is lesser than target, discard the left half of the array
        i.e. [1,3,4,5,6,7,8] target is 6
            if mid = (0+5)//2 = 2 -> arr[2] = 4 which is smaller than 6
            discard left by changing left = mid + 1 = 2 + 1 = 3
            --> array become [6,7,8] where [1,3,4,5] are discarded
    """
    left, right = 0 , len(arr) -1
    while left <=right:
        mid = (left + right) //2
        if arr[mid] < target:
            left = mid + 1 #target is greater than mid, so ignore the left half
        elif arr[mid] == target and arr[mid-1] !=target:
            return mid
        else:
            right = mid - 1
    return left

def linear_search(arr, target):
    """Apply on unsorted array
    """
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return len(arr) -1 

sorted_array = [2, 3, 4, 10, 40]

target = 50
answer = linear_search(sorted_array,target)
print(f"target either found or can insert at index {answer}")