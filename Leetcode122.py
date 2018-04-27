# Leetcode 122 Best Time to Buy and Sell Stock II

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_val = 0
        if prices is None or len(prices) <= 1: return max_val
        for idx in range(1, len(prices)):
            if(prices[idx] > prices[idx-1] ):
                max_val = max_val + prices[idx] - prices[idx-1]
        return max_val
