# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

arrays = [2,3,1,2,4,3]
target = 7

arrays1 = [1,1,1,1,1,1,1,1]
target1=11

def answer(nums,target):
    left = right = 0 #indexing
    total_nums = len(nums)
    sum = 0
    min_array_len = float('inf')
    while right < total_nums:
        sum +=nums[right]
        while sum >= target:
            min_array_len = min(min_array_len, right - left + 1) #right- left = differences between two pointers, +1 is for inclusively []
            sum -=nums[left]
            left+=1
        right +=1
    return min_array_len if min_array_len != float('inf') else 0

print(answer(arrays1,target1))
