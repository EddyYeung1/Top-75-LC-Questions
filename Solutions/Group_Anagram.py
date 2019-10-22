'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

'''
Solution 1: we create a dictionary with a sorted word as a key and a list of anagrams as its value. The key here is by having the sorted word as a key we can easily find other anagrams in the list with constant time. Afterwards all we need to do is append the groups to the answer list. The only issue about this is that it takes O(M * KLogK) because for every word we check out on the list we are also sorting it and thats takes O(K log K) time, yikes. 
'''


def groupAnagrams(strs):
    dic = {}
    ans = []

    for word in strs:
        temp = "".join(sorted(word))
        if temp not in dic:
            dic[temp] = []
        if temp in dic:
            dic[temp].append(word)

    for key in dic:
        ans.append(dic[key])

    return ans


'''
Solution 2: This is essentially the same concept as the above, however instead we are defining an array with 26 letters as its size. We count the frequency of every letter and convert that frequency list into a tuple which becomes a key for the dictionary. We have to convert it to a list because keys have to be immutable and tuples are immutable.
'''


def groupAnagrams(self, strs):
    ans = collections.defaultdict(list)

    for word in strs:
        frequencyList = [0] * 26  # this creates an array in python
        for char in word:
            # ord() returns the ascii val of a char we subtract by ord('a') so we can access the correct indicie in our frequencyList
            # i.e ord('b') - ord('a') = 1, frequencyList[1] = second letter in alphabet
            frequencyList[ord(char) - ord('a')] += 1

        # convert to tuple because key for a dict must be immutable
        # the reason the key has to be immutable is because for hashing to work changing the key would fuck up the mapping
        ans[tuple(frequencyList)].append(word)

    return(ans.values())
