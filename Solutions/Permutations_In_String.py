'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab" s2 = "eidboaoo"
Output: False
'''

'''
Solution 1: Very similar concept to find all anagrams in string. Use the sliding window technique for a fixed window and you are gucci. O(N) time O(1) space.
'''


def checkInclusion(self, s1, s2):
    wordArr = [0] * 26
    for i in s1:
        wordArr[ord(i) - ord('a')] += 1

    tempArr = [0] * 26
    winSize = 0

    for i, e in enumerate(s2):
        tempArr[ord(e) - ord('a')] += 1
        winSize += 1
        # once we reach the size of our window check if the window is a premutation of our word
        if winSize == len(s1):
            if tempArr == wordArr:
                return True
            tempArr[ord(s2[i-len(s1)+1]) - ord('a')] -= 1
            winSize -= 1

    return False
