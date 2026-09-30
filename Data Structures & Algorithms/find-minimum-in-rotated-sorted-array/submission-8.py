class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search since logn within boundary l, r
        # my interval should always have the smalles number of the array in it
        # Since I need to throw away half the array at each step, 
        # I need to prove that array split does NOT contain minimum
        # I throw away the mid - r section if nums[mid] < nums[r]
        # other section I keep

        l, r = 0, len(nums) - 1
        curr_min = float("inf")

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
                curr_min = min(curr_min, nums[mid])
            else:
                l = mid + 1
                curr_min = min(curr_min, nums[mid])
            
        return curr_min