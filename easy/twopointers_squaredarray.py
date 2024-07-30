# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


def bad_answer(nums): #time complexity is O(nlogn)
    for index in range(len(nums)):
        nums[index] = nums[index] **2 
    return sorted(nums)

def answer_twopointers(nums):
    left, right = 0, len(nums) -1 #because the largest number in the array is already at the last position
    new_list = []
    while left <=right:
        if abs(nums[left]) <= abs(nums[right]):
            new_list.append(nums[right]**2)
            right -= 1
        else:
            new_list.append(nums[left]**2)
            left += 1
    return new_list[::-1]

test = [-7,-3,2,3,11]
#first iteration:
#nums[0] = -7 & nums[3] = 3 --> absolute value gives left pointer value > right pointer value
#> else state -> square using left arrow and move the left arrow to next position

#second iteraiton
#nums[1] = -3 & nums[3] = 3 --> absolute value gives equal --> match else condition
#> else statement --> square using left arrow and move left arrow to next position

#third iteration
#nums[2] = 2 & nums[3] = 3 --> match the if condition
#>if statement --> square the right arrow nad move right arrow to next position
#new_list is now: [49 9 9]
print(answer_twopointers(test))