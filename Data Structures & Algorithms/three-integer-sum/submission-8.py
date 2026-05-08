class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1 
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if  target == 0:
                    result.add(tuple(sorted([nums[i], nums[l], nums[r]]))) 
                    l += 1
                    r -= 1
                
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1

        return list(result)

            