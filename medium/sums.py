def twosums(arr, target):
    """Using a hashmap to find sums of two numbers in array
    1. use for loop through an array
    2. appending into the hashmap using key as value from array and value is index of array
        i.e. (using example below) {3,0} means that first index 0 value is 3
    3. use complement value by using target - arr[i] and check if the complement value presents in the hashmap as key,
    4. return the a list that contains the indexes from the array that the sum is equal to target

    Returns:
        list: indexes of arr
    """
    hashmap = {}
    for i in range(0, len(arr)):
        if target - arr[i] in hashmap:
            return [hashmap[target - arr[i]], i]
        hashmap[arr[i]] = i
    return []


def threesums(arr, target=0):
    """Condition:
    Given an integer array arr, return all the triplets
    [arr[i], arr[j], arr[k]] such that i != j, i != k, and j != k, and arr[i] + arr[j] + arr[k] == 0.
    1. Sort the array from smallest to largests
    2. establish a set to record result
    3. Looping through the array
    4. Set up 2nd pointer with +1 position and 3rd pointer starting from the end
    5. Create a While loop with the 2nd pointer position is lesser than 3rd pointer position
    6. Checkout condition
        6a. If sum < target, move the 2nd pointer forward
        6b. If sum > target, move the 3rd pointer backward
        6c. If sum = target, record the index positions. then move 2nd pointer forward and move 3rd pointer backward
    """
    arr.sort()
    s = set()
    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == target:
                s.add((arr[i], arr[j], arr[k]))
                j += 1
                k -= 1
            elif sum < target:
                j += 1
            else:
                k -= 1
    return list(s)


def threeSumclosest(arr):
    arr.sort()
    answer = arr[0] + arr[1] + arr[2]
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if abs(current_sum - target) < abs(answer - target):
                answer = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    return answer


##
arr = [3, 21, 2, 3, 5, 6, 8, 1, 2, 3, 4, 5, 8, 0, 9]
target = 9
print(twosums(arr, target))
