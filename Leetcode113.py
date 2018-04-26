# Leetcode 113 Path Sum II

# This is a easy backtracking problem
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.solver(root, result, [], 0, sum)
        return result

    def solver(self, node, result, temp, total, sum):
        if node is None:
            return

        if node.left is None and node.right is None:
            if (total + node.val) == sum:
                temp.append(node.val)
                result.append(temp[:])
                temp.pop()
            return

        temp.append(node.val)
        self.solver(node.left, result, temp, total+node.val, sum)
        self.solver(node.right, result, temp, total+node.val, sum)
        temp.pop()
