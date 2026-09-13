class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        arr = sorted(set(nums))

        longest_sequence, curr_sequence = 1, 1

        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1] - 1:
                curr_sequence += 1
            else:
                curr_sequence = 1

            longest_sequence = max(longest_sequence, curr_sequence)

        return longest_sequence