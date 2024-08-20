arr = ["racecar", "ada", "ad23"]
valpal = "A man, a plan, a canal: Panama"


def isPalindrome(words: list) -> bool:
    left = 0
    right = len(words) - 1
    while left < right:
        if words[left] != words[right]:
            return False
        left += 1
        right -= 1
    return True


def validPalindrome(word: str):
    left = 0
    right = len(word) - 1
    while left < right:
        if not word[left].isalnum():
            left += 1
        elif word[right].isalnum():
            right -= 1
        elif word[left].lower() == word[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


print(validPalindrome(valpal))
