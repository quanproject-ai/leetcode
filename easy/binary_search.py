# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

def answer(nums,target):
    left, right = 0, len(nums)-1 
    while left <= right:
        mid = (left+right)//2 
        if nums[mid] < target: 
            left = mid + 1 
        else:
            if nums[mid] == target and nums[mid-1] !=target: 
                return mid 
            else:
                right = mid -1
    return left

def answer_without_binary_search(nums,target):
    index = 0
    if target > max(nums): #handle target is larger than max of nums
        return len(nums) #return the position of the largest number in nums
    if len(nums) > 0 and target <= max(nums): #handle target is < than max of nums
        while nums[index] < target and index < len(nums)-1: #looping index from 0 that satisfy both conditions
            index +=1 #keep increment index until the loop breaks
    return index

num = [1,3,5,6]
targeto = [0,2,5,7]

print(answer(num,2))