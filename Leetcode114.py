# Leetcode 114 Flatten Binary Tree to Linked List


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.rotate(root)

    def rotate(self, node):
        if node is None:
            return

        if node.left:
            # 记录当前节点的右节点
            temp = node.right

            # 找出当前节点左节点的最右子节点
            end = node.left
            while(end.right != None):
                end = end.right

            # 将当前节点的右节点链接在当前节点左节点的最右子节点之后
            end.right = temp

            # 将当前节点的左节点设为右节点
            node.right = node.left

        # 将当前节点的左节点设为None
        node.left = None

        node = node.right
        self.rotate(node)
