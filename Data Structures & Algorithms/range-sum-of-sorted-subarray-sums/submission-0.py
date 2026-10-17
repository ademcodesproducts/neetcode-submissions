class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 1000000007
        res = []

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                res.append(curr_sum)
        
        res.sort()
        return sum(res[left - 1:right]) % mod