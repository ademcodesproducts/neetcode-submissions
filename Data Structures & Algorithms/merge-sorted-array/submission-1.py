class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n - 1
        j = m - 1
        k = m + n - 1

        while i >= 0:
            if j >= 0 and nums2[i] < nums1[j]:
                nums1[k] = nums1[j]
                j -= 1
            else:
                nums1[k] = nums2[i]
                i -= 1
            k -= 1

        return nums1        