class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip
            j, k = i + 1, len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k] 
                if three_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while k > j and nums[k + 1] == nums[k]:
                        k -= 1
                    
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1

        return res