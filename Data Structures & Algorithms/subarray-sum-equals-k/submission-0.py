class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # At every position, what previous prefix sum would make my current subarray equal k?
        count_equals_k = 0
        prefixSum = 0
        seen = {0: 1}

        for num in nums:
            prefixSum += num
            if prefixSum - k in seen:
                count_equals_k += seen[prefixSum - k]
                
            if prefixSum in seen:
                seen[prefixSum] += 1
            else:
                seen[prefixSum] = 1

                

        return count_equals_k
