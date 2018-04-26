# Leetcode 116 Populating Next Right Pointers in Each Node

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        while root.left:
            cur = root.left
            right_sib = root
            prev = None
            while right_sib is not None:
                if prev is not None:
                    prev.right.next = right_sib.left
                right_sib.left.next = right_sib.right
                prev = right_sib
                right_sib = right_sib.next
            root = root.left
