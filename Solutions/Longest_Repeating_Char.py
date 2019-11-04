from collections import defaultdict
'''
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Input:
s = "ABAB", k = 2
Output:
4

Input:
s = "AABABBA", k = 1
Output:
4
'''

'''
Solution 1: Another sliding window problem, but this one is a bit less intuitive than others. The key to remember for this problem is the size of your window - your most frequent character will get you a substring with k replacements.

'''


def characterReplacement(self, s, k):
    maxLen, start, cnt, maxCount = 0, 0, defaultdict(int), 0
    for i, c in enumerate(s):
        cnt[c] += 1
        maxCount = max(maxCount, cnt[c])
        if i - start + 1 - maxCount > k:
            # remove the element at the start of our window so we can slide
            cnt[s[start]] -= 1
            start += 1  # slide window forward
        maxLen = max(maxLen, i - start + 1)
    return maxLen
