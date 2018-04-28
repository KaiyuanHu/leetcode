# Leetcode 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    glo_max = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traversal(root)
        return self.glo_max

    def traversal(self, node):
        if node is None:
            return 0
        left, right = self.traversal(node.left), self.traversal(node.right)
        sum = node.val + max(0, left) + max(0, right)
        self.glo_max = max(self.glo_max, sum)
        return max(0, left, right) + node.val
