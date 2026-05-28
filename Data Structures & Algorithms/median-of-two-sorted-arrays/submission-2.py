class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        m, n = len(A), len(B)
        half = (m + n) // 2

        l, r = 0, m

        while l <= r:
            mid = (l + r) // 2

            Aleft = A[mid - 1] if mid > 0 else float('-inf')
            Aright = A[mid] if mid < m else float('inf')

            j = half - mid

            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:

                if (m + n) % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1