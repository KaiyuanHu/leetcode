# Leetcode 118 Pascal's Triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for line in xrange(numRows):
            temp = []
            for item in xrange(line+1):
                if line <= 1:
                    temp.append(1)
                else:
                    if item == 0 or item == line:
                        temp.append(1)
                    else:
                        temp.append(result[line-1][item-1] + result[line-1][item])

            result.append(temp[:])

        return result
