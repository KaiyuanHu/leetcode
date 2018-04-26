# Leetcode 112 Path Sum

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.solver(root, 0, sum)

    def solver(self, node, total, sum):
        if node is None:
            return False
        # add up from root to leaf
        if(node.left is None and node.right is None):
            if((total + node.val) == sum):
                return True
            else:
                return False

        return self.solver(node.left, total+node.val, sum) or self.solver(node.right, total+node.val, sum)
