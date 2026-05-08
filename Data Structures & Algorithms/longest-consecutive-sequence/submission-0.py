class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        for n in nums:
            length = 1
            current = n
            while current + 1 in nums:
                current += 1
                length += 1
            counter = max(length, counter)
        return counter
            
            