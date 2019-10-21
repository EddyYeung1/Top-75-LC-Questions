'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
'''

'''
Solution 1: Brute Force, for every number loop through the rest of the numbers to see if it adds to target O(n^2) time, O(1) space
Solution 2: Two Pass Hashmap, put everything in hashmap first then find complement in second iteration O(N) time, O(N) space
Solution 3: One Pass hashmap, we can do it in one run O(N) time, O(N) space
'''


def twoSum(nums, target):
    dic = {}  # a hashmap provides us constant time look up
    ans = []
    for i in range(len(nums)):

        # calculate the complement for every indicie, if its already in the dic we can return it
        complement = target - nums[i]

        if complement in dic:  # key here is the constant time look up here gives us linear time
            ans.append(i)
            ans.append(dic[complement])
            return ans

        dic[nums[i]] = i
