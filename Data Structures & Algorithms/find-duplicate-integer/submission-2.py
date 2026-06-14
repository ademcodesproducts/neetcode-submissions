class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        new_slow = 0
        while new_slow != fast:
            new_slow = nums[new_slow]
            fast = nums[fast]

        return new_slow
        