class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)
        for i in range(len(nums)):
            multiplication = 1
            for j in range(len(nums)):
                if i != j:
                    multiplication *= nums[j]
            output[i] = multiplication
        return output
        