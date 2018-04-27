# Leetcode 119 Pascal's Triangle II

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        def f(y, x):
            res = 1
            if x == 0: return res
            for i in xrange(x):
                res = res*(y-i)/(i+1)
            return res

        return [f(rowIndex, x) for x in xrange(rowIndex+1)]
