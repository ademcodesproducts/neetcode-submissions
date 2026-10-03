from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # same task -> separate by n CPU cycle
        # return minimum number of CPU cylce
        # for every loop we increase cycle by 1
        # if no tasks -> return 0
        # O(n) or O(nlogn)
        # deque
        # x -> 2 key value
        """
        freq = key -> value: counter -> tasks
        maxHeap = - -> (freq, tasks)
        q = (end_time, tasks)
        """

        freq = Counter(tasks)
        maxHeap = [(-c, t) for t, c in freq.items()]
        heapq.heapify(maxHeap)

        cycle = 0
        waiting_queue = deque()
        while maxHeap or waiting_queue:
            cycle += 1
            while waiting_queue and waiting_queue[0][0] <= cycle:
                _, task = waiting_queue.popleft()
                heapq.heappush(maxHeap, (-freq[task], task))
            
            if maxHeap:
                _, task = heapq.heappop(maxHeap)
                freq[task] -= 1

                if freq[task] > 0:
                    ending_time = cycle + n + 1
                    waiting_queue.append((ending_time, task))

        return cycle