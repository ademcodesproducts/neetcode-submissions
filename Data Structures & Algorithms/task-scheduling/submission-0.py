class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        heap = [(-c, t) for t, c in count.items()]
        heapq.heapify(heap)

        itr = 0
        q = deque()
        while heap or q: 
            itr += 1

            if q and itr == q[0][2]:
                task, count, _ = q.popleft()
                heapq.heappush(heap, (count, task))

            if heap:
                c, t = heapq.heappop(heap)
                c += 1 # reverse counting
                if c < 0:
                    q.append((t, c, itr + n + 1))
            else:
                continue
            
        return itr