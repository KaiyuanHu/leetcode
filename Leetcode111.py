# Leetcode 111 Minimum Depth of Binary Tree
class Solution:
    level = sys.maxsize

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        self.solver(root, 1)
        return self.level


    def solver(self, node, level):
        if(node.left == None and node.right== None):
            self.level = min(self.level, level)
        else:
            print('heelo')
            if(node.left != None):
                self.solver(node.left, level+1)
            if(node.right != None):
                self.solver(node.right, level+1)
