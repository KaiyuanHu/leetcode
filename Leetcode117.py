# Leetcode 117 Populating Next Right Pointers in Each Node II

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return

        up_level = root
        cur = up_level.left if up_level.left is not None else up_level.right
        
        while cur is not None:
            sib = cur
            while up_level is not None:
                if up_level.left is not None and sib != up_level.left:
                    sib.next = up_level.left
                    sib = sib.next
                    if up_level.right is not None:
                        sib.next = up_level.right
                        sib = sib.next
                elif up_level.right is not None and sib != up_level.right:
                    sib.next = up_level.right
                    sib = sib.next

                up_level = up_level.next
                
            up_level = cur

            while up_level.next != None and up_level.left is None and up_level.right is None:
                up_level = up_level.next
                
            cur = up_level.left if up_level.left is not None else up_level.right
