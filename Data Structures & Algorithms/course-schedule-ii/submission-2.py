class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        indegree = [0] * numCourses
        q = deque()
        graph = defaultdict(list)

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            order.append(node)
            for vertex in graph[node]:
                indegree[vertex] -= 1
                if indegree[vertex] == 0:
                    q.append(vertex)

        return order if len(order) == numCourses else [] # check if cycle