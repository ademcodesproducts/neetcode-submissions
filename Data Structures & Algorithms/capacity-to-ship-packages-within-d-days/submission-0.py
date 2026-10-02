class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search over answer space, looking at the capacity
        # Pointers represent the space where smallest weight capactiy is included
        # left pointer is the minimum, it can't be less than the highest weight
        # right poiinter is maximum, it can't be more than all the weights combine
        # the loops should test that all the weights from left to right can fit 
        # in the given days


        l, r = max(weights), sum(weights)

        while l < r:
            capacity = (l + r) // 2
            time = 1 # start at one since you calculate start not completion
            curr_sum = 0
            for w in weights:
                if curr_sum + w > capacity:
                    time += 1
                    curr_sum = 0
                curr_sum += w

            if time <= days:
                r = capacity
            else:
                l = capacity + 1

        return l