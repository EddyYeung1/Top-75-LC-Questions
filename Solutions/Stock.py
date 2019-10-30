'''
   Say you have an array for which the ith element is the price of a given stock on day i.

   If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

   Note that you cannot sell a stock before you buy one.

   Example 1:

   Input: [7,1,5,3,6,4]
   Output: 5
   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                Not 7-1 = 6, as selling price needs to be larger than buying price.
   Example 2:

   Input: [7,6,4,3,1]
   Output: 0
   Explanation: In this case, no transaction is done, i.e. max profit = 0.
    '''

'''
Solution 1: The shit solution is for every price you find the max profit you iterate the rest of the prices to see if a new max profit can be found. Basically a double for loop for every price. O(N^2) time

Solution 2: The optimal solution is to find the highest peak and lowest valley in an interval refer to the graph on the leetcode solution. We can keep track of the valley by having a variable to store the mininum price. O(N) time.
'''


def maxProfit(self, prices: List[int]) -> int:

    minPrice = float('inf')
    maxProf = 0

    for i in prices:
        if i < minPrice:
            minPrice = i
        else:
            maxProf = max(maxProf, i - minPrice)

    return maxProf
