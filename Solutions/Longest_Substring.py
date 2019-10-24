'''
   Given a string, find the length of the longest substring without repeating characters.

   Example 1:

   Input: "abcabcbb"
   Output: 3 
   Explanation: The answer is "abc", with the length of 3. 
   Example 2:

   Input: "bbbbb"
   Output: 1
   Explanation: The answer is "b", with the length of 1.
   Example 3:

   Input: "pwwkew"
   Output: 3
   Explanation: The answer is "wke", with the length of 3. 
                Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    '''

'''
Solution 1: There is a brute force way in which you check every substring to see if it has duplicate chars. That way takes O(N^3) time very very bad.
Solution 2: We can decrease this to linear time by using the sliding window technique with a dictionary. This variation of the sliding window technique involves a dynamically resizing window with an auxillary data structure to help us. For every character we need to store its latest index as a value in the dictionary. We want to do this because that how we can decide where to resize the left side of our window. Basically, if we encounter a repeated character we must also check that we are not going into that if statement just because we saw it. For example "t m m x y t v", when we find m our start=2, when we reach t we do not want to move our window because our window no longer includes that first t at the beginning and is not considered a duplicate of our current substring.  
'''


def lengthOfLongestSubstring(self, s):
    usedChars = {}
    maxSum = startIndex = 0

    for index, letter in enumerate(s):
        if letter in usedChars and startIndex <= usedChars[letter]:
            # moving our window by increasing the left pointer by one
            startIndex = usedChars[letter] + 1
        else:
            # index is our right pointer, start index is our left pointer, and we add 1 because we started iterating from 0
            maxSum = max(maxSum, index - startIndex + 1)

        usedChars[letter] = index

    return maxSum
