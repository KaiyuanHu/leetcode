# Leetcode 121 Best Time to Buy and Sell Stock  
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hi, idx  = len(prices)-1, len(prices)-2
        max_val = 0
        while hi >=1 and idx >=0:
            if(prices[hi] - prices[idx] > 0):
                max_val = max(max_val, prices[hi] - prices[idx])
                idx -= 1
            else:
                hi -= 1
                idx = hi-1 
        return max_val
