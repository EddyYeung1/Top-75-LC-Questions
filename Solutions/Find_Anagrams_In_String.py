'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

'''
Solution 1: My first approach was to use the sorted word as a key in a dictionary. Then with the string itself splice the string and then sort it and compare to the dictionary. However this method is extremely inefficient. Sorting costs O(N log N) time and I have to do that for every substring I splice so overall its O(K * N Log N).
Solution 2: I was able to improve the above method to O(N), but instead using a frequency table of a fixed array sized 26 for the size of the alphabet. I then used the sliding window technique to maintain my linear time complexity. 
'''


def findAnagrams(self, s, p):
    ans = []
    pFrequencyList = [0] * 26
    for i in p:
        # create the frequency table for the word to compare with each substring in the word
        pFrequencyList[ord(i) - ord('a')] += 1

    tempList = [0] * 26

    for i in range(len(s)):
        # start counting the letters in the substring frequency table
        tempList[ord(s[i]) - ord('a')] += 1

        if (i >= len(p)-1):  # once we reach the size of our window (the size of the word)
            # compare the frequency lists typically this would take O(N) time, but since they are a constant 26 chars its actually O(1)
            if tempList == pFrequencyList:
                ans.append(i-(len(p)-1))  # add start index
            # move our sliding window by decrementing the front of our windo
            tempList[ord(s[i-(len(p)-1)]) - ord('a')] -= 1

    return ans
