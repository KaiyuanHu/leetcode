# Leetcode 04 Median of Two Sorted Arrays  
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def pop_median(x):
            poped = []

            for i in range(x):
                if not nums1:
                    poped.append(nums2.pop(0))
                elif not nums2:
                    poped.append(nums1.pop(0))
                elif nums1[0] < nums2[0]:
                    poped.append(nums1.pop(0))
                else:
                    poped.append(nums2.pop(0))
            return poped
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            pop_median((total_len//2)-1)
            median = pop_median(2)
        else:
            pop_median((total_len-1)//2 )
            median = pop_median(1)

        return sum(median) / len(median)
