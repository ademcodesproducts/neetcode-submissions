class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest_sequence, curr_sequence = 0, 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                # start of sequence
                curr_sequence = 1
                while num + 1 in num_set:
                    curr_sequence += 1
                    num = num + 1
            
            longest_sequence = max(longest_sequence, curr_sequence)

        return longest_sequence