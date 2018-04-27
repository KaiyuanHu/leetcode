# Leetcode 120 Triangle

# time limit execeed on last test case
class Solution(object):
    min = 100000

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.solver(0, 0, 0, triangle)
        return self.min

    def solver(self, level, pos, total, triangle):
        if level == len(triangle):
            self.min = min(total, self.min)
            return
        for idx in range(pos, min(pos + 2, len(triangle[level]))):
            total += triangle[level][idx]
            self.solver(level + 1, idx, total, triangle)
            total -= triangle[level][idx]

# Then think bottom up solution
class Solution(object):
    def minimumTotal(self, triangle):
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] = min(triangle[row][col]+ triangle[row+1][col], triangle[row][col]+ triangle[row+1][col+1])

        return triangle[0][0]
