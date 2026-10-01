class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [3,4,5,CUT, 6,1,2]

        [1,2,3,CUT, 4,5,6]
        
        [5,6,1, CUT, 2,3,4]
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < nums[r]:
                # sorted to the right
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                # sorted to the left
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1