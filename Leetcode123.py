# Leetcode 123 Best Time to Buy and Sell Stock III

# Greedy Solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1, buy2, sell1, sell2 = float('-inf'), float('-inf'), 0, 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, price+buy1)
            buy2 = max(buy2, sell1-price)
            sell2 = max(sell2, price+buy2)

        return sell2
