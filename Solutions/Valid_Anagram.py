'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

'''
Solution 1: you could just do sorted(t) == sorted(s), but that would be O(n log n) time which we can do better than
Solution 2: put all letters of one of them in a dictionary whilst also keep a count of how many time the letter appears. After iterate through the other word and decrement the count for each letter. We finally iterate through our dictionary one more time and if it has any key with a value that is not 0 it is false. This is O(N) time and O(1) space even though we use a dictionary. The reason it is still constant space is because we have a constant amount of possible input which is 26 lowercase chars. 
'''


def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    dic = {}
    for i in s:  # put everything in dic and count all chars
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in t:  # go through the other word and decrement chars
        if i not in dic:  # found letter that isn't in previous word hence making it not a anagram
            return False
        else:
            dic[i] -= 1

    for i in dic:  # if any key isn't 0 its not an anagram
        if dic[i] != 0:
            return False

    return True
