'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

'''
*You could easily just do [::-1] or use .reversed(), but that is cheating. Your interviewer doesn't give a fuck that you know how to use python's built in functions. 

Solution 1: Reconstruct the string by iterating through the back. This takes O(N) time, but O(N) space is to reconstruct the string, bad. 
Solution 2: Have two pointers, one in the front and one in the back they should match up if its a palindrome, return False if it ever doesn't.

The stupid part about the problem is you have to strip the non-alphanumeric chars. There is a way to do this without pre-processing it first, but I didn't feel like doing that.
'''


def isPalindrome(self, s):
    # got this off stack overflow, it removes all non-alpha numerics
    s = ''.join(ch for ch in s if ch.isalnum())
    back = len(s)-1
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[back]:
            print(s[i], s[back])
            return False
        back -= 1

    return True
