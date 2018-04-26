# Leetcode 115 Distinct Subsequences


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        result = [[ 0 for x in range(len(s) + 1)] for y in range(len(t) + 1)]
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                # 相等时的状态转移
                if t[i - 1] == s[j - 1]:
                    result[i][j] = 1 + result[i][j - 1] if i == 1 else result[i][j - 1] + result[i - 1][j - 1]
                # 不等时的状态转移
                else:
                    result[i][j] = result[i][j - 1]
        return result[len(t)][len(s)]
