# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true


# Example 3:
# Input: s = "(]"
# Output: false
def isValid(self, strings_symbols):
    symbols_dict = {"(": ")", "{": "}", "[": "]"}
    if len(strings_symbols) == 0:
        return True
    if len(strings_symbols) == 1:
        return False
    stack = []
    for symbol in strings_symbols:
        if symbols_dict.get(symbol):  # Checking left brackets in string
            stack.append(symbol)  # store it in a data structure.
        else:  # The moment we hit a right bracket
            try:
                # check was the last left braket that we saw correspondingly in shape to the current right bracket.
                last_left_bracket = stack.pop()
                correspond_bracket = symbols_dict.get(last_left_bracket)
                if symbol != correspond_bracket:
                    return False
            except:  # if the first bracket in string is the right bracket then return false
                return False
    # If string is corresponding then stack data structure will empty else stack will still have some elements
    return len(stack) == 0
