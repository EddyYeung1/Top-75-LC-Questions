'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
'''

'''
Solution: To solve this problem we have to keep a stack of all opening parenthesis. The basic concept is everytime we encounter an opening parenthese we add it to the stack and anytime we encounter a closing bracket we pop the stack and make sure it corresponds with its opening bracket. In my implementation I use a dictionary to make the code more clean, but we don't actually need to use that. This takes O(N) time and O(N) space for the stack. 
'''


def validParens(s):
    mapping = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for i in s:
        if i in mapping:  # if i is an opening bracket add it to the stack
            stack.append(i)
        if i not in mapping:  # we encountered a closing bracket
            if not stack:  # if stack is empty there is no opening bracket to correspond with it
                return False
            check = stack.pop()
            if mapping[check] != i:  # make sure the mapping is correct
                return False

    if stack:  # we have an unclosed opening bracket
        return False

    return True  # we gucci
