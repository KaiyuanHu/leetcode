# Leetcode 109 Convert Sorted List to Binary Search Tree
class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while(head is not None):
            arr.append(head.val)
            head = head.next
        node = self.solver(arr)
        return node

    def solver(self, lst):
        if lst is None or len(lst) == 0:
            return None

        mid = int(len(lst)/2)
        node = TreeNode(lst[mid])
        node.left = self.solver(lst[:mid])
        node.right = self.solver(lst[mid+1:])
        return node
